#!/usr/bin/env python3
# ════════════════════════════════════════════════════════════════════
# ⚠️  NOT IN USE — KEPT FOR REFERENCE ONLY  ⚠️
# ════════════════════════════════════════════════════════════════════
#
# STATUS: Shelved. This tool is NOT deployed, NOT called by pipeline.yml,
# and NOT wired into VM2's crontab. /home/ubuntu/rsync_from_vm1.sh (the
# original bash script) is the live, production sync mechanism on VM2 —
# it works correctly and is intentionally left untouched.
#
# WHY THIS FILE EXISTS ANYWAY: it was built as a structured-output
# rewrite of rsync_from_vm1.sh (line-count verification, split checksum
# strategy, JSON status output — see the full docstring below for the
# design reasoning). Deploying it would mean copying it to VM2 and
# editing the working crontab for a benefit (status visibility, basic
# verification) that doesn't actually require replacing a script that
# already runs reliably. Decision: not worth the risk/effort tradeoff
# for a working production job. Kept in the repo as a reference
# implementation only, in case rsync status visibility or stronger
# verification becomes a real need later.
#
# DO NOT deploy this without re-confirming that decision first. If you
# ARE looking to add rsync status visibility without touching VM2 at
# all, the discussed (not yet built) alternative is a read-only
# pipeline.yml step that SSHes into VM2 and tails the existing
# /home/ubuntu/var/log/thir_rsync.log — see project conversation history.
# ════════════════════════════════════════════════════════════════════
"""
tools/38_rsync_collector.py — THIR VM2 rsync collector (Tool 38)

Replaces /home/ubuntu/rsync_from_vm1.sh with a structured-output equivalent.
Runs on VM2 via cron (same trigger, same timing — see deployment notes at
bottom of this file). NOT a GitHub Actions pipeline step — this is a
VM2-resident tool, same operating pattern as sync_to_r2.sh.

WHAT THIS PRESERVES EXACTLY FROM THE ORIGINAL SCRIPT (do not change
silently — these are confirmed-working production behaviors, not
assumptions):
  - HAProxy failover detection via the admin stats socket
  - Pull from VM1 (active json+log, rotated json+log, downloads/)
  - Pull from VM2 standby Cowrie ONLY when HAProxy reports vm1 DOWN
  - Stale VM2 log cleanup when NOT in failover
  - Section 4/5 merge logic: VM1+VM2 -> sort -u dedup,
    VM1-only -> cp, VM2-only -> cp, neither -> exit 1 / do not overwrite
  - Exact same destination paths and filenames (cowrie.json, cowrie.log,
    cowrie_vm1.json, cowrie_vm2.json, etc.) — pipeline.yml's watermark

    fetch step depends on these exact names not changing.

WHAT THIS ADDS (the actual ask for Tool 38):
  - Line count verification (did the transferred file shrink unexpectedly —
    would indicate a truncated/corrupted transfer)
  - Checksum comparison — SPLIT STRATEGY, see "CHECKSUM STRATEGY" below.
    This was a genuinely open design question, resolved by reasoning about
    the two file classes rather than picked arbitrarily; see comment block.
  - Structured JSON status output: /home/ubuntu/var/thir_rsync_status.json
    (consumable by a future pipeline.yml step / Tool 30 / dashboard — same
    sibling-status-file convention as data/integrity_status.json,
    data/cowrie_watermark.json)
  - rsync exit code is now actually checked (the original script never
    checked $? after any rsync call)

WHAT THIS DOES NOT CHANGE (flagged, not silently resolved):
  - The watermark-vs-resync interaction. cowrie.json is rebuilt wholesale
    each run (cp or sort -u merge), not appended to. GitHub Actions' Tool 26
    fetch step assumes line N stays line N between runs for its
    `tail -n +(LAST_LINE+1)` incremental read. In the common no-failover
    case (VM1_OK only -> straight cp of VM1's append-only file) this likely
    holds, since cowrie.json's line order then matches VM1's natural
    append order. The open, NOT-YET-CHECKED question is specifically:
    does a sort -u run (any pipeline cycle landing during an active HAProxy
    failover, where both VM1 and VM2 have content) reorder enough of the
    file to make the next cycle's tail -n +N read the wrong lines, for
    however many cycles the failover lasts? This script does not attempt
    to fix that — it is explicitly out of scope for Tool 38 as asked, and
    changing merge/dedup behavior to "fix" this without confirming it's
    actually broken risks introducing a different bug. Flagged in the
    status JSON's "known_open_questions" field so it stays visible.

CHECKSUM STRATEGY (the second open design question, now resolved by
reasoning rather than picked arbitrarily — see conversation):
  - Active files (cowrie.json, cowrie.log on VM1): Cowrie writes to these
    continuously. A post-transfer remote-hash comparison would race against
    live attacker traffic — VM1's file can grow between when rsync reads it
    and when a follow-up SSH call hashes "the source." That race makes a
    hash mismatch here a structural false positive, not a real integrity
    signal. So active files get BEHAVIOR-based verification instead:
    rsync exit code == 0, line count did not shrink vs. last known count,
    local file mtime advanced.
  - Rotated files (cowrie.json.YYYY-MM-DD, cowrie.log.YYYY-MM-DD) and
    downloads/: these are closed/static on VM1 — rotation already happened,
    downloads are never appended to after capture. No race condition.
    These get HASH-based verification: sha256 computed remotely on VM1,
    compared against sha256 of the local copy.

Standard library only — no pip install, matching every other tool in this
pipeline.
"""

import hashlib
import json
import os
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Configuration (mirrors the original script's hardcoded values) ────────
VM1 = "10.0.0.53"
DEST = Path("/opt/thir/logs")
RUN_LOG = Path("/home/ubuntu/var/log/thir_rsync.log")
STATUS_FILE = Path("/home/ubuntu/var/thir_rsync_status.json")
SSH_KEY = "/home/ubuntu/.ssh/thir_internal"
SSH_PORT = 22222
HAPROXY_SOCK = "/var/run/haproxy/admin.sock"
COWRIE_REMOTE_DIR = "/home/cowrie/cowrie/var/log/cowrie"
COWRIE_REMOTE_DOWNLOADS = "/home/cowrie/cowrie/var/lib/cowrie/downloads"
VM2_STANDBY_LOG = Path("/home/cowrie/cowrie/var/log/cowrie/cowrie.json")
VM2_STANDBY_TEXT = Path("/home/cowrie/cowrie/var/log/cowrie/cowrie.log")

SSH_BASE = [
    "ssh", "-p", str(SSH_PORT), "-i", SSH_KEY,
    "-o", "StrictHostKeyChecking=no",
    "-o", "ConnectTimeout=15",
    "-o", "BatchMode=yes",
]
RSYNC_SSH_OPT = f"ssh -p {SSH_PORT} -i {SSH_KEY} -o StrictHostKeyChecking=no"


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg):
    line = f"{now_iso()}: {msg}"
    print(line)
    sys.stdout.flush()


def has_content(path):
    p = Path(path)
    return p.is_file() and p.stat().st_size > 0


def line_count(path):
    if not has_content(path):
        return 0
    with open(path, "rb") as f:
        return sum(1 for _ in f)


def run(cmd, timeout=120):
    """Run a subprocess, capturing exit code + stdout/stderr. Never raises."""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)


def remote_sha256(path):
    """sha256sum of a file on VM1, via SSH. Returns hash string or None."""
    rc, out, err = run(SSH_BASE + [f"cowrie@{VM1}", f"sha256sum {shlex.quote(path)}"])
    if rc != 0:
        return None
    parts = out.strip().split()
    return parts[0] if parts else None


def local_sha256(path):
    if not has_content(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ── Status accumulator ─────────────────────────────────────────────────
status = {
    "tool": "38_rsync_collector",
    "run_started_at": now_iso(),
    "run_completed_at": None,
    "overall_status": "UNKNOWN",  # OK / DEGRADED / FAILED
    "vm1_reachable": False,
    "vm2_cowrie_active_failover": False,
    "files": {},       # per-file verification results
    "merge": {},        # cowrie.json / cowrie.log merge outcome
    "errors": [],
    "known_open_questions": [
        "Watermark-vs-resync interaction not yet confirmed safe: cowrie.json "
        "is rebuilt wholesale each run (cp or sort -u merge), not appended. "
        "GitHub Actions' tail -n +(LAST_LINE+1) assumes stable line ordering "
        "between runs. Open question, narrowly scoped: does a sort -u run "
        "(any cycle during an active HAProxy failover) reorder the file "
        "enough to corrupt the NEXT cycle's watermark read, for however "
        "many cycles the failover lasts? Not yet checked. Do not silently "
        "fix without confirming first — see Tool 38 build notes."
    ],
}


def record_file_result(name, **kwargs):
    status["files"][name] = kwargs


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    RUN_LOG.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

    # ════════════════════════════════════════════════════════════════
    # SECTION 1 — Detect HAProxy failover state (unchanged from original)
    # ════════════════════════════════════════════════════════════════
    vm2_cowrie_active = False
    if os.path.exists(HAPROXY_SOCK):
        rc, out, err = run(
            ["bash", "-c",
             f"echo 'show stat' | sudo socat stdio {HAPROXY_SOCK} 2>/dev/null"]
        )
        vm1_backend_status = None
        for line in out.splitlines():
            fields = line.split(",")
            if len(fields) > 17 and fields[0] == "cowrie_backend" and fields[1] == "vm1":
                vm1_backend_status = fields[17]
                break
        if vm1_backend_status == "DOWN":
            vm2_cowrie_active = True
            log("HAProxy reports vm1 DOWN — VM2 standby Cowrie is active")
        else:
            log("HAProxy reports vm1 UP — normal operations")
    else:
        log("WARNING — HAProxy socket not found, cannot check failover state")
        status["errors"].append("haproxy_socket_not_found")

    status["vm2_cowrie_active_failover"] = vm2_cowrie_active

    # ════════════════════════════════════════════════════════════════
    # SECTION 2 — Pull logs from VM1 (normal path, unchanged structure)
    # ════════════════════════════════════════════════════════════════
    vm1_reachable = False
    rc, _, _ = run(["nc", "-zw5", VM1, "22222"])
    if rc == 0:
        vm1_reachable = True
        log("VM1 reachable — starting rsync")

        # ── Active cowrie.json — BEHAVIOR-based verification (active file) ──
        prev_lines = line_count(DEST / "cowrie_vm1.json")
        prev_mtime = (DEST / "cowrie_vm1.json").stat().st_mtime if has_content(DEST / "cowrie_vm1.json") else 0
        rcode, _, err = run([
            "rsync", "-az", "-e", RSYNC_SSH_OPT,
            f"cowrie@{VM1}:{COWRIE_REMOTE_DIR}/cowrie.json",
            str(DEST / "cowrie_vm1.json"),
        ], timeout=180)
        new_lines = line_count(DEST / "cowrie_vm1.json")
        new_mtime = (DEST / "cowrie_vm1.json").stat().st_mtime if has_content(DEST / "cowrie_vm1.json") else 0
        ok = (rcode == 0) and has_content(DEST / "cowrie_vm1.json") and (new_lines >= prev_lines)
        record_file_result(
            "cowrie_vm1.json",
            verification="behavior",  # active/growing file — see CHECKSUM STRATEGY
            rsync_exit_code=rcode,
            line_count_prev=prev_lines,
            line_count_new=new_lines,
            shrank=new_lines < prev_lines,
            mtime_advanced=new_mtime > prev_mtime,
            ok=ok,
        )
        if ok:
            log(f"Active cowrie.json synced — {new_lines} lines")
        else:
            log(f"WARNING — cowrie_vm1.json verification failed "
                f"(rsync_rc={rcode}, lines {prev_lines}->{new_lines}, stderr={err.strip()})")
            status["errors"].append("cowrie_vm1_json_verification_failed")

        # ── Active cowrie.log — same behavior-based approach ──
        prev_lines_log = line_count(DEST / "cowrie_vm1.log")
        rcode, _, err = run([
            "rsync", "-az", "-e", RSYNC_SSH_OPT,
            f"cowrie@{VM1}:{COWRIE_REMOTE_DIR}/cowrie.log",
            str(DEST / "cowrie_vm1.log"),
        ], timeout=180)
        new_lines_log = line_count(DEST / "cowrie_vm1.log")
        ok = (rcode == 0) and has_content(DEST / "cowrie_vm1.log") and (new_lines_log >= prev_lines_log)
        record_file_result(
            "cowrie_vm1.log",
            verification="behavior",
            rsync_exit_code=rcode,
            line_count_prev=prev_lines_log,
            line_count_new=new_lines_log,
            shrank=new_lines_log < prev_lines_log,
            ok=ok,
        )
        if ok:
            log(f"Active cowrie.log synced — {new_lines_log} lines")
        else:
            log(f"WARNING — cowrie_vm1.log verification failed (rsync_rc={rcode}, stderr={err.strip()})")
            status["errors"].append("cowrie_vm1_log_verification_failed")

        # ── Rotated JSON logs — HASH-based verification (static files) ──
        rcode, out, err = run([
            "rsync", "-az", "-e", RSYNC_SSH_OPT,
            "--include=cowrie.json.2026-*", "--exclude=*",
            f"cowrie@{VM1}:{COWRIE_REMOTE_DIR}/", f"{DEST}/",
        ], timeout=300)
        rotated_json = sorted(DEST.glob("cowrie.json.2026-*"))
        rotated_verified, rotated_failed = 0, 0
        for f in rotated_json:
            remote_path = f"{COWRIE_REMOTE_DIR}/{f.name}"
            rh = remote_sha256(remote_path)
            lh = local_sha256(f)
            if rh is not None and rh == lh:
                rotated_verified += 1
            else:
                rotated_failed += 1
        record_file_result(
            "rotated_json",
            verification="hash",  # closed/static file — see CHECKSUM STRATEGY
            rsync_exit_code=rcode,
            files_total=len(rotated_json),
            files_hash_verified=rotated_verified,
            files_hash_failed=rotated_failed,
            ok=(rcode == 0 and rotated_failed == 0),
        )
        log(f"Rotated JSON synced — {len(rotated_json)} files "
            f"({rotated_verified} hash-verified, {rotated_failed} mismatched)")
        if rotated_failed:
            status["errors"].append(f"rotated_json_hash_mismatch:{rotated_failed}")

        # ── Rotated text logs — same hash-based approach ──
        rcode, out, err = run([
            "rsync", "-az", "-e", RSYNC_SSH_OPT,
            "--include=cowrie.log.2026-*", "--exclude=*",
            f"cowrie@{VM1}:{COWRIE_REMOTE_DIR}/", f"{DEST}/",
        ], timeout=300)
        rotated_log = sorted(DEST.glob("cowrie.log.2026-*"))
        rotated_log_verified, rotated_log_failed = 0, 0
        for f in rotated_log:
            remote_path = f"{COWRIE_REMOTE_DIR}/{f.name}"
            rh = remote_sha256(remote_path)
            lh = local_sha256(f)
            if rh is not None and rh == lh:
                rotated_log_verified += 1
            else:
                rotated_log_failed += 1
        record_file_result(
            "rotated_log",
            verification="hash",
            rsync_exit_code=rcode,
            files_total=len(rotated_log),
            files_hash_verified=rotated_log_verified,
            files_hash_failed=rotated_log_failed,
            ok=(rcode == 0 and rotated_log_failed == 0),
        )
        log(f"Rotated text synced — {len(rotated_log)} files "
            f"({rotated_log_verified} hash-verified, {rotated_log_failed} mismatched)")
        if rotated_log_failed:
            status["errors"].append(f"rotated_log_hash_mismatch:{rotated_log_failed}")

        # ── Downloads directory — HASH-based verification (static files) ──
        (DEST / "downloads").mkdir(parents=True, exist_ok=True)
        rcode, out, err = run([
            "rsync", "-az", "-e", RSYNC_SSH_OPT,
            f"cowrie@{VM1}:{COWRIE_REMOTE_DOWNLOADS}/", f"{DEST}/downloads/",
        ], timeout=300)
        downloaded = sorted((DEST / "downloads").glob("*"))
        downloaded = [f for f in downloaded if f.is_file()]
        dl_verified, dl_failed = 0, 0
        for f in downloaded:
            remote_path = f"{COWRIE_REMOTE_DOWNLOADS}/{f.name}"
            rh = remote_sha256(remote_path)
            lh = local_sha256(f)
            if rh is not None and rh == lh:
                dl_verified += 1
            else:
                dl_failed += 1
        record_file_result(
            "downloads",
            verification="hash",
            rsync_exit_code=rcode,
            files_total=len(downloaded),
            files_hash_verified=dl_verified,
            files_hash_failed=dl_failed,
            ok=(rcode == 0 and dl_failed == 0),
        )
        log(f"Downloads synced — {len(downloaded)} files "
            f"({dl_verified} hash-verified, {dl_failed} mismatched)")
        if dl_failed:
            status["errors"].append(f"downloads_hash_mismatch:{dl_failed}")

    else:
        log("VM1 unreachable on port 22222")
        status["errors"].append("vm1_unreachable")

    status["vm1_reachable"] = vm1_reachable

    # ════════════════════════════════════════════════════════════════
    # SECTION 3 — Pull from VM2 standby Cowrie (unchanged from original)
    # ════════════════════════════════════════════════════════════════
    if vm2_cowrie_active:
        if has_content(VM2_STANDBY_LOG):
            data = VM2_STANDBY_LOG.read_bytes()
            (DEST / "cowrie_vm2.json").write_bytes(data)
            n = line_count(DEST / "cowrie_vm2.json")
            log(f"VM2 standby Cowrie active — {n} lines copied")
            record_file_result("cowrie_vm2.json", verification="copy", line_count=n, ok=True)
        else:
            log("WARNING — HAProxy says VM2 active but standby log is empty")
            status["errors"].append("vm2_standby_log_empty")
            record_file_result("cowrie_vm2.json", verification="copy", ok=False)

        if has_content(VM2_STANDBY_TEXT):
            data = VM2_STANDBY_TEXT.read_bytes()
            (DEST / "cowrie_vm2.log").write_bytes(data)
            n = line_count(DEST / "cowrie_vm2.log")
            log(f"VM2 standby cowrie.log copied — {n} lines")
            record_file_result("cowrie_vm2.log", verification="copy", line_count=n, ok=True)
    else:
        # Not in failover — clear any stale VM2 log from a previous failover
        if (DEST / "cowrie_vm2.json").exists():
            (DEST / "cowrie_vm2.json").unlink()
            log("Cleared stale cowrie_vm2.json — not in failover")

    # ════════════════════════════════════════════════════════════════
    # SECTION 4 — Merge into cowrie.json (unchanged merge semantics —
    # SAME sort -u / cp / exit-1 logic as the original script. The
    # watermark interaction with this merge is the flagged open question
    # above, NOT addressed here.)
    # ════════════════════════════════════════════════════════════════
    def merge(active_name, vm1_file, vm2_file, dest_file):
        vm1_ok = has_content(vm1_file)
        vm2_ok = has_content(vm2_file)
        if vm1_ok and vm2_ok:
            with open(vm1_file, "rb") as a, open(vm2_file, "rb") as b:
                lines = set(a.read().splitlines()) | set(b.read().splitlines())
            sorted_lines = sorted(lines)
            with open(dest_file, "wb") as out:
                out.write(b"\n".join(sorted_lines))
                if sorted_lines:
                    out.write(b"\n")
            n = len(sorted_lines)
            log(f"Merged VM1+VM2 — {n} lines (deduped) [{active_name}]")
            return {"source": "vm1+vm2_merged", "lines": n, "ok": True}
        elif vm1_ok:
            data = Path(vm1_file).read_bytes()
            Path(dest_file).write_bytes(data)
            n = line_count(dest_file)
            log(f"VM1 only — {n} lines [{active_name}]")
            return {"source": "vm1_only", "lines": n, "ok": True}
        elif vm2_ok:
            data = Path(vm2_file).read_bytes()
            Path(dest_file).write_bytes(data)
            n = line_count(dest_file)
            log(f"VM2 failover only — {n} lines [{active_name}]")
            return {"source": "vm2_only", "lines": n, "ok": True}
        else:
            log(f"ERROR — no log source has content, {active_name} NOT updated")
            status["errors"].append(f"{active_name}_no_source_content")
            return {"source": "none", "lines": 0, "ok": False}

    status["merge"]["cowrie.json"] = merge(
        "cowrie.json", DEST / "cowrie_vm1.json", DEST / "cowrie_vm2.json", DEST / "cowrie.json"
    )
    status["merge"]["cowrie.log"] = merge(
        "cowrie.log", DEST / "cowrie_vm1.log", DEST / "cowrie_vm2.log", DEST / "cowrie.log"
    )

    # ════════════════════════════════════════════════════════════════
    # Finalize status
    # ════════════════════════════════════════════════════════════════
    log("rsync collector complete")
    status["run_completed_at"] = now_iso()

    merge_failed = (not status["merge"]["cowrie.json"]["ok"]) or (not status["merge"]["cowrie.log"]["ok"])
    if merge_failed:
        status["overall_status"] = "FAILED"
    elif status["errors"]:
        status["overall_status"] = "DEGRADED"
    else:
        status["overall_status"] = "OK"

    STATUS_FILE.write_text(json.dumps(status, indent=2) + "\n")

    return 1 if merge_failed else 0


if __name__ == "__main__":
    with open(RUN_LOG, "a") as logfile:
        # Mirror the original script's `exec >> $LOG 2>&1` behavior —
        # redirect this process's stdout/stderr to the log file for the
        # duration of the run, while status JSON still gets its own
        # dedicated file (the original script had nowhere structured for
        # this — that's the gap Tool 38 closes).
        os.dup2(logfile.fileno(), sys.stdout.fileno())
        os.dup2(logfile.fileno(), sys.stderr.fileno())
        exit_code = main()
    sys.exit(exit_code)


# ════════════════════════════════════════════════════════════════════
# DEPLOYMENT NOTES (not executed by this script — for the operator)
# ════════════════════════════════════════════════════════════════════
#
# 1. Copy this file to VM2 (no git checkout exists there today, confirmed —
#    pipeline.yml treats VM2 purely as an SSH/SCP remote source, not a repo
#    checkout target):
#      scp -P 22222 -i thir-pipeline-key.pem \
#        tools/38_rsync_collector.py ubuntu@VM2_IP:/home/ubuntu/
#      chmod +x /home/ubuntu/38_rsync_collector.py
#
# 2. Replace the cron entry — SAME timing as today, just point at the new
#    script instead of the shell version (per the agreed "keep same
#    55 */2 * * * timing, just swap the script" default):
#      crontab -e
#      # OLD: 55 */2 * * * /home/ubuntu/rsync_from_vm1.sh
#      # NEW: 55 */2 * * * /usr/bin/python3 /home/ubuntu/38_rsync_collector.py
#
# 3. Do NOT delete rsync_from_vm1.sh immediately — keep it as a fallback
#    until at least one full week of Tool 38 runs have been spot-checked
#    against /home/ubuntu/var/thir_rsync_status.json for any overall_status
#    other than "OK", consistent with this project's test-before-handoff
#    discipline.
#
# 4. /home/ubuntu/var/thir_rsync_status.json is VM2-local only as written.
#    It is NOT YET wired into data/rsync_status.json in the GitHub repo —
#    that requires a new pipeline.yml step (an SSH+cat, same two-hop
#    pattern already used for cowrie.json) which was raised as undecided
#    and is intentionally left for a follow-up pass rather than bundled
#    into this build silently.
