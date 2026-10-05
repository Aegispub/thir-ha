#!/usr/bin/env python3
"""
Tool 00: Historical Processor

Batch re-processes a directory of rotated Cowrie cowrie.json.* log files
(plain or .gz) through the same logic as Tools 26, 34, 35, and 36 — but
across an entire corpus instead of a single live log. Produces a
permanent historical_data/<corpus>/ baseline for either the AWS corpus
(thir-raw-archive, one-time) or the Oracle corpus (thirha-raw-archive,
recurring quarterly).

Run mode: one-shot, offline. NOT part of pipeline.yml. Does not touch
data/*.json, does not call Tool 37, does not update cowrie_watermark.json.

Output files (all under --output-dir, committed to git — every field in
both is a count or a label, never a raw IP, credential, command,
fingerprint, or session ID):
    historical_stats.json              — per-day time series + top-N highlights
                                          (kept as-is: daily series, anomaly
                                          days, top 10 IPs, top 20 credential
                                          pairs — a deliberate curated cut)
    corpus_highlights.json             — lightweight no-PII summary proving
                                          the credential/fingerprint/threat-ip/
                                          command-cluster/ir-case analysis
                                          passes ran, and their aggregate shape
                                          (counts, severity breakdown, cluster
                                          counts — never the underlying rows)
    corpus_metadata.json               — run metadata, anomaly days, EOF status

The five raw per-category files this tool used to write
(historical_ir_cases.json, historical_credentials.json,
historical_ssh_fingerprints.json, historical_threat_ips.json,
historical_command_clusters.json) are NOT written to --output-dir anymore.
Row-level data for all five categories — individual IPs, credential pairs,
SSH fingerprints, commands, and session IDs — exists only in the full,
un-truncated R2 archive (see --full-records-out below), never in git. This
keeps the repo from absorbing PII-adjacent attacker IP/credential data and
keeps repo growth roughly flat regardless of corpus size, since the only
git-committed outputs are now aggregate counts.

Full (un-truncated) case records are written to a local temp file for
upload to R2 live-archives/ by the calling workflow — see
--full-records-out.

Standard library only. No pip installs. Python 3.8+.
"""

import argparse
import gzip
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any, Dict, List, Optional, Tuple
import ipaddress

TOOL_VERSION = "00.1.0"

# ──────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────

def log_info(msg: str, verbose: bool = True) -> None:
    if verbose:
        print(f"[Tool00] {msg}", file=sys.stderr)


def log_mem(label: str, verbose: bool = True) -> None:
    if not verbose:
        return
    try:
        vals = {}
        with open("/proc/self/status") as f:
            for l in f:
                if l.startswith(("VmRSS", "VmHWM")):
                    vals[l.split(":")[0]] = int(l.split()[1]) // 1024
        print(f"[Tool00] MEM {label}: {vals.get('VmRSS', 0)} MB RSS "
              f"(peak {vals.get('VmHWM', 0)} MB)", file=sys.stderr)
    except Exception:
        pass


def log_warn(msg: str) -> None:
    print(f"[Tool00] WARNING: {msg}", file=sys.stderr)


def log_error(msg: str) -> None:
    print(f"[Tool00] ERROR: {msg}", file=sys.stderr)


def fatal(msg: str, code: int = 1) -> None:
    log_error(msg)
    sys.exit(code)


# ──────────────────────────────────────────────────────────────────────────
# Phase 1 — File discovery and ordering
# ──────────────────────────────────────────────────────────────────────────

FILENAME_DATE_RE = re.compile(r"cowrie\.json\.(\d{4}-\d{2}-\d{2})(\.gz)?$")


def discover_log_files(log_dir: str, start_date: Optional[str],
                        end_date: Optional[str], verbose: bool) -> List[Path]:
    """Find cowrie.json.YYYY-MM-DD[.gz] files, sorted chronologically,
    filtered to the optional [start_date, end_date] inclusive range."""
    base = Path(log_dir)
    if not base.is_dir():
        fatal(f"--log-dir does not exist or is not a directory: {log_dir}")

    candidates = []
    for p in base.rglob("cowrie.json.*"):
        m = FILENAME_DATE_RE.search(p.name)
        if not m:
            continue
        file_date = m.group(1)
        if start_date and file_date < start_date:
            continue
        if end_date and file_date > end_date:
            continue
        candidates.append((file_date, p))

    candidates.sort(key=lambda t: t[0])
    files = [p for _, p in candidates]

    if not files:
        fatal(f"No cowrie.json.YYYY-MM-DD[.gz] files found in {log_dir} "
              f"within date range [{start_date or 'earliest'}, {end_date or 'latest'}]")

    total_bytes = sum(p.stat().st_size for p in files)
    log_info(f"Discovered {len(files)} log file(s), "
             f"{total_bytes / 1024 / 1024:.1f} MB raw, "
             f"date range {candidates[0][0]} to {candidates[-1][0]}", verbose)
    return files


def open_log_file(path: Path):
    """Transparent .gz / plain text open, matching Cowrie's rotation naming."""
    if path.name.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return open(path, "r", encoding="utf-8", errors="replace")


# ──────────────────────────────────────────────────────────────────────────
# Phase 2 — Session extraction (Tool 26 logic, adapted for many files +
# cross-file dedup)
# ──────────────────────────────────────────────────────────────────────────

MAX_CMD_LEN = 1000  # matches Tool 26's P4 patch

# TTP mapping — same intent as Tool 26's map_ttps(); duplicated here rather
# than imported because Tool 26 is a standalone script (no package __init__),
# and re-implementing this ~15-line mapping is simpler and more robust than
# manipulating sys.path to import a sibling script by filename.
_TTP_PATTERNS = [
    (r"cowrie\.login\.success", "T1078", "Valid Accounts"),
    (r"cowrie\.session\.file_download", "T1105", "Ingress Tool Transfer"),
    (r"cowrie\.command\.input", "T1059", "Command and Scripting Interpreter"),
    (r"chmod\s+\+x", "T1222", "File and Directory Permissions Modification"),
    (r"crontab|systemctl|/etc/init\.d", "T1053", "Scheduled Task/Job"),
    (r"authorized_keys", "T1098.004", "SSH Authorized Keys"),
    (r"wget|curl", "T1105", "Ingress Tool Transfer"),
    (r"history\s+-c|rm\s+-rf\s+/var/log", "T1070", "Indicator Removal"),
]


def map_ttps(events: List[Dict]) -> List[str]:
    seen = {}
    blob_parts = []
    for e in events:
        eid = e.get("eventid", "")
        blob_parts.append(eid)
        if eid == "cowrie.command.input":
            blob_parts.append(e.get("input", ""))
    blob = " ".join(blob_parts).lower()
    for pattern, ttp_id, _name in _TTP_PATTERNS:
        if re.search(pattern, blob, re.IGNORECASE):
            seen[ttp_id] = True
    return list(seen.keys())


def calculate_severity(case: Dict) -> str:
    if case.get("login_success") and case.get("downloads"):
        return "CRITICAL"
    if case.get("login_success"):
        return "HIGH"
    if case.get("downloads") or len(case.get("commands", [])) > 3:
        return "MEDIUM"
    return "LOW"


def sanitise_session_id(raw: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "", raw or "")[:64] or "unknown"


def cross_file_dedup_key(src_ip: str, session_id: str, first_seen: str) -> str:
    """SHA256(src_ip + session_id + first_event_timestamp)[:16] — handles a
    session whose events get split across a rotation boundary (e.g. a
    session open at 23:59:50 and still active at 00:00:05 the next day,
    appearing in both the old and the new rotated file)."""
    raw = f"{src_ip}|{session_id}|{first_seen}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def parse_cowrie_line(line: str) -> Optional[Dict]:
    line = line.strip()
    if not line:
        return None
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        return None
    if "session" not in event or "eventid" not in event:
        return None
    return event


def _build_case(session_id: str, events_sorted: List[Dict], source_file: str) -> Dict:
    """Build one IR case from a session's time-ordered events. Shared by the
    in-memory path (extract_sessions) and the on-disk path (SpillStore) so the
    two cannot drift apart."""
    safe_sid = sanitise_session_id(session_id)

    raw_ip = next((e.get("src_ip", "") for e in events_sorted if e.get("src_ip")), "")
    src_ip = raw_ip if raw_ip else "unknown"

    first_seen = events_sorted[0].get("timestamp", "") if events_sorted else ""
    last_seen = events_sorted[-1].get("timestamp", "") if events_sorted else ""

    duration_seconds = 0
    for e in events_sorted:
        if e.get("eventid") == "cowrie.session.closed":
            try:
                duration_seconds = int(float(e.get("duration", 0)))
            except (TypeError, ValueError):
                pass
            break

    login_attempts = sum(
        1 for e in events_sorted
        if e.get("eventid") in ("cowrie.login.failed", "cowrie.login.success")
    )
    login_success = any(e.get("eventid") == "cowrie.login.success" for e in events_sorted)

    commands = [
        e["input"][:MAX_CMD_LEN]
        for e in events_sorted
        if e.get("eventid") == "cowrie.command.input" and e.get("input")
    ]

    downloads = [
        {"url": e.get("url", ""), "sha256": e.get("shasum", "")}
        for e in events_sorted
        if e.get("eventid") == "cowrie.session.file_download"
    ]

    ttps = map_ttps(events_sorted)

    _strip = {"session", "message", "sensor"}
    timeline = []
    for e in events_sorted:
        entry = {k: v for k, v in e.items() if k not in _strip}
        entry["event"] = e.get("eventid", "")
        timeline.append(entry)

    case = {
        "case_id": f"IR-{safe_sid}",
        "src_ip": src_ip,
        "first_seen": first_seen,
        "last_seen": last_seen,
        "duration_seconds": duration_seconds,
        "login_attempts": login_attempts,
        "login_success": login_success,
        "commands": commands,
        "downloads": downloads,
        "ttps": ttps,
        "severity": "",
        "timeline": timeline,
        "source_file": source_file,
    }
    case["severity"] = calculate_severity(case)
    return case


def extract_sessions(files: List[Path], verbose: bool) -> Tuple[List[Dict], int]:
    """Read all files in chronological order, group events by session,
    apply cross-file dedup, build one IR case per session.

    Returns (cases, lines_skipped).
    """
    # session_id -> list of events (accumulate across files first, since a
    # session can legitimately span a rotation boundary)
    sessions_raw: Dict[str, List[Dict]] = defaultdict(list)
    lines_skipped = 0

    for idx, path in enumerate(files, start=1):
        log_info(f"Reading file {idx}/{len(files)}: {path.name}", verbose)
        try:
            with open_log_file(path) as fh:
                for line in fh:
                    event = parse_cowrie_line(line)
                    if event is None:
                        lines_skipped += 1
                        continue
                    sessions_raw[event["session"]].append(event)
        except (OSError, gzip.BadGzipFile) as exc:
            log_warn(f"Could not read {path}: {exc} — skipping file")
            continue

    log_info(f"Collected {len(sessions_raw)} raw session bucket(s) "
             f"before dedup ({lines_skipped} unparseable lines skipped)", verbose)

    # Build IR cases, then dedup by (src_ip, session_id, first_seen) —
    # this catches the case where the SAME session_id string was reused
    # by a different connection (Cowrie session IDs are short hex strings
    # and can theoretically collide across a 59-day corpus, however rare)
    cases: List[Dict] = []
    seen_dedup_keys = set()
    source_file_by_session: Dict[str, str] = {}

    # Track which file each session's first event came from, for the
    # index's source_file field
    for path in files:
        try:
            with open_log_file(path) as fh:
                for line in fh:
                    event = parse_cowrie_line(line)
                    if event is None:
                        continue
                    sid = event["session"]
                    if sid not in source_file_by_session:
                        source_file_by_session[sid] = path.name
        except (OSError, gzip.BadGzipFile):
            continue

    # --- VCN internal IP exclusion — filters HAProxy health check sessions ---
    VCN_INTERNAL = ipaddress.ip_network("10.0.0.0/24")

    def _ip_in_vcn(raw: str) -> bool:
        try:
            return ipaddress.ip_address(raw.strip()) in VCN_INTERNAL
        except ValueError:
            return False
    # -------------------------------------------------------------------------

    for session_id, events in sessions_raw.items():
        _src = next((e.get("src_ip", "") for e in events if e.get("src_ip")), "")
        if _src and _ip_in_vcn(_src):
            continue
        events_sorted = sorted(events, key=lambda e: e.get("timestamp", ""))
        raw_ip = next((e.get("src_ip", "") for e in events_sorted if e.get("src_ip")), "")
        src_ip = raw_ip if raw_ip else "unknown"
        first_seen = events_sorted[0].get("timestamp", "") if events_sorted else ""

        dedup_key = cross_file_dedup_key(src_ip, session_id, first_seen)
        if dedup_key in seen_dedup_keys:
            continue
        seen_dedup_keys.add(dedup_key)

        cases.append(_build_case(session_id, events_sorted,
                                 source_file_by_session.get(session_id, "")))

    cases.sort(key=lambda c: c.get("first_seen", ""))
    log_info(f"Built {len(cases)} deduplicated IR case(s)", verbose)
    return cases, lines_skipped



# ──────────────────────────────────────────────────────────────────────────
# Phase 2b — On-disk session store (opt-in via --spill-dir)
#
# Produces exactly the same cases, in exactly the same order, as
# extract_sessions(), but never holds the corpus's events (or the finished
# cases) in memory. Events go to a temporary SQLite file as they are parsed;
# cases are rebuilt one at a time, in final sorted order, and handed to the
# caller (which streams them to the archive). Row order inside a session is
# (timestamp, insertion sequence), which reproduces Python's stable
# sorted(..., key=timestamp) over the insertion-ordered event list.
# ──────────────────────────────────────────────────────────────────────────

_VCN_INTERNAL = ipaddress.ip_network("10.0.0.0/24")


def _ip_in_vcn_net(raw) -> bool:
    try:
        return ipaddress.ip_address(str(raw).strip()) in _VCN_INTERNAL
    except ValueError:
        return False


class SpillStore:
    BATCH = 50000

    def __init__(self, files: List[Path], spill_dir: str, verbose: bool) -> None:
        self.files = files
        self.verbose = verbose
        self.dir = Path(spill_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.db_path = self.dir / "tool00_events.sqlite"
        if self.db_path.exists():
            self.db_path.unlink()
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.execute("PRAGMA journal_mode=OFF")
        self.conn.execute("PRAGMA synchronous=OFF")
        self.conn.execute("CREATE TABLE ev (seq INTEGER PRIMARY KEY, sid TEXT, ts TEXT, line TEXT)")
        self.order: List[Tuple[str, str]] = []
        self.total = 0
        self.lines_skipped = 0
        self.skipped_by_file: Dict[str, int] = {}

    def build(self) -> None:
        """Pass 1: parse every file once, spill events, track per-session
        metadata needed to reproduce extract_sessions()' filtering/ordering."""
        # meta[sid] = [min_ts, ip_first_inserted, ip_ts_key, ip_by_ts, first_file]
        meta: Dict[str, list] = {}
        batch: List[tuple] = []
        seq = 0
        for idx, path in enumerate(self.files, start=1):
            log_info(f"Reading file {idx}/{len(self.files)}: {path.name}", self.verbose)
            try:
                with open_log_file(path) as fh:
                    for line in fh:
                        event = parse_cowrie_line(line)
                        if event is None:
                            self.lines_skipped += 1
                            self.skipped_by_file[path.name] = self.skipped_by_file.get(path.name, 0) + 1
                            continue
                        sid = event["session"]
                        ts = event.get("timestamp", "")
                        if not isinstance(ts, str):
                            ts = "" if ts is None else str(ts)
                        src = event.get("src_ip", "")
                        seq += 1
                        batch.append((seq, sid, ts, line.strip()))
                        m = meta.get(sid)
                        if m is None:
                            meta[sid] = [ts, src or "", ts if src else None, src or "", path.name]
                        else:
                            if ts < m[0]:
                                m[0] = ts
                            if src:
                                if not m[1]:
                                    m[1] = src
                                if m[2] is None or ts < m[2]:
                                    m[2] = ts
                                    m[3] = src
                        if len(batch) >= self.BATCH:
                            self.conn.executemany("INSERT INTO ev VALUES (?,?,?,?)", batch)
                            batch.clear()
            except (OSError, gzip.BadGzipFile) as exc:
                log_warn(f"Could not read {path}: {exc} — skipping rest of file")
                continue
        if batch:
            self.conn.executemany("INSERT INTO ev VALUES (?,?,?,?)", batch)
            batch.clear()
        self.conn.commit()
        log_info(f"Collected {len(meta)} raw session bucket(s) "
                 f"before dedup ({self.lines_skipped} unparseable lines skipped)", self.verbose)
        self.conn.execute("CREATE INDEX ev_sid ON ev(sid, ts, seq)")
        self.conn.commit()

        survivors: List[Tuple[str, list]] = []
        seen = set()
        for sid, m in meta.items():              # dict order == first-appearance order
            if m[1] and _ip_in_vcn_net(m[1]):    # first src_ip in INSERTION order (as before)
                continue
            src_ip = m[3] if m[3] else "unknown"  # first src_ip in TIMESTAMP order (as before)
            key = cross_file_dedup_key(src_ip, sid, m[0])
            if key in seen:
                continue
            seen.add(key)
            survivors.append((sid, m))
        survivors.sort(key=lambda t: t[1][0])    # stable, same as cases.sort(first_seen)
        self.order = [(sid, m[4]) for sid, m in survivors]
        self.total = len(self.order)
        log_info(f"Built {self.total} deduplicated IR case(s)", self.verbose)

    def iter_cases(self):
        for _fname, case in self.iter_cases_with_home():
            yield case

    def iter_cases_with_home(self):
        """Yield (home_file_name, case) in final sorted order. home = the first
        file (in the order given to the store) in which the session appears."""
        cur = self.conn.cursor()
        for sid, fname in self.order:
            rows = cur.execute(
                "SELECT line FROM ev WHERE sid=? ORDER BY ts, seq", (sid,)).fetchall()
            yield fname, _build_case(sid, [json.loads(r[0]) for r in rows], fname)

    def close(self) -> None:
        try:
            self.conn.close()
        finally:
            try:
                self.db_path.unlink()
            except OSError:
                pass

# ──────────────────────────────────────────────────────────────────────────
# Phase 3 — Credential extraction (Tool 34 logic, looped per file + merged)
# ──────────────────────────────────────────────────────────────────────────

_LOGIN_EVENTS = {"cowrie.login.failed", "cowrie.login.success"}
_LOGIN_SUCCESS = "cowrie.login.success"
_CRED_TOP_N = 20  # historical corpus warrants a longer top-N than the live Tool 34's 10


def parse_credentials_from_file(path: Path) -> Tuple[List[Dict], List[Dict]]:
    """Same extraction logic as Tool 34's parse_cowrie_credentials(),
    adapted for transparent .gz handling. Returns (all_attempts, success_pairs)
    for this one file — caller merges across files."""
    all_attempts, success_pairs = [], []
    try:
        with open_log_file(path) as fh:
            for line in fh:
                event = parse_cowrie_line(line)
                if event is None:
                    continue
                event_id = event.get("eventid", "")
                if event_id not in _LOGIN_EVENTS:
                    continue
                username = event.get("username", "")
                password = event.get("password", "")
                if not username and not password:
                    continue
                record = {
                    "username": username,
                    "password": password,
                    "src_ip": event.get("src_ip", ""),
                    "timestamp": event.get("timestamp", ""),
                    "success": event_id == _LOGIN_SUCCESS,
                }
                all_attempts.append(record)
                if event_id == _LOGIN_SUCCESS:
                    success_pairs.append({
                        "username": username, "password": password,
                        "src_ip": record["src_ip"], "timestamp": record["timestamp"],
                    })
    except (OSError, gzip.BadGzipFile) as exc:
        log_warn(f"Could not read {path} for credential extraction: {exc}")
    return all_attempts, success_pairs


def aggregate_credentials(all_attempts: List[Dict], success_pairs: List[Dict]) -> Dict:
    """Same aggregation shape as Tool 34's aggregate(), top-N raised for corpus scale."""
    username_counts: Dict[str, int] = defaultdict(int)
    password_counts: Dict[str, int] = defaultdict(int)
    pair_counts: Dict[Tuple[str, str], int] = defaultdict(int)

    for a in all_attempts:
        username_counts[a["username"]] += 1
        password_counts[a["password"]] += 1
        pair_counts[(a["username"], a["password"])] += 1

    top_usernames = sorted(username_counts.items(), key=lambda kv: -kv[1])[:_CRED_TOP_N]
    top_passwords = sorted(password_counts.items(), key=lambda kv: -kv[1])[:_CRED_TOP_N]
    top_pairs = sorted(pair_counts.items(), key=lambda kv: -kv[1])[:_CRED_TOP_N]

    return {
        "total_attempts": len(all_attempts),
        "unique_pairs": len(pair_counts),
        "unique_usernames": len(username_counts),
        "unique_passwords": len(password_counts),
        "top_usernames": [{"username": u, "count": c} for u, c in top_usernames],
        "top_passwords": [{"password": p, "count": c} for p, c in top_passwords],
        "top_pairs": [{"username": u, "password": p, "count": c} for (u, p), c in top_pairs],
        # total_successful_logins is the TRUE count, taken before truncation.
        # success_pairs below is intentionally capped at _CRED_TOP_N for
        # display purposes — do not use len(success_pairs) as a count
        # anywhere; it silently reads as min(true_count, _CRED_TOP_N).
        "total_successful_logins": len(success_pairs),
        "success_pairs": success_pairs[:_CRED_TOP_N],
    }


class CredentialAccumulator:
    """Incremental equivalent of aggregate_credentials(): consumes one file's
    attempts at a time so the full corpus-wide attempt list is never held in
    memory. Counters are filled in the same order the old list was iterated,
    so tie-breaking in the top-N sorts — and therefore the output — is
    identical to aggregate_credentials() on the concatenated list."""

    def __init__(self) -> None:
        self.username_counts: Dict[str, int] = defaultdict(int)
        self.password_counts: Dict[str, int] = defaultdict(int)
        self.pair_counts: Dict[Tuple[str, str], int] = defaultdict(int)
        self.total_attempts = 0
        self.success_total = 0
        self.success_head: List[Dict] = []

    def add_file(self, attempts: List[Dict], successes: List[Dict]) -> None:
        for a in attempts:
            self.username_counts[a["username"]] += 1
            self.password_counts[a["password"]] += 1
            self.pair_counts[(a["username"], a["password"])] += 1
        self.total_attempts += len(attempts)
        self.success_total += len(successes)
        room = _CRED_TOP_N - len(self.success_head)
        if room > 0:
            self.success_head.extend(successes[:room])

    def result(self) -> Dict:
        top_usernames = sorted(self.username_counts.items(), key=lambda kv: -kv[1])[:_CRED_TOP_N]
        top_passwords = sorted(self.password_counts.items(), key=lambda kv: -kv[1])[:_CRED_TOP_N]
        top_pairs = sorted(self.pair_counts.items(), key=lambda kv: -kv[1])[:_CRED_TOP_N]
        return {
            "total_attempts": self.total_attempts,
            "unique_pairs": len(self.pair_counts),
            "unique_usernames": len(self.username_counts),
            "unique_passwords": len(self.password_counts),
            "top_usernames": [{"username": u, "count": c} for u, c in top_usernames],
            "top_passwords": [{"password": p, "count": c} for p, c in top_passwords],
            "top_pairs": [{"username": u, "password": p, "count": c} for (u, p), c in top_pairs],
            "total_successful_logins": self.success_total,
            "success_pairs": self.success_head[:_CRED_TOP_N],
        }


def write_full_records_stream(path: Path, corpus_name: str, total_cases: int, case_iter) -> None:
    """Write the full-record archive one case at a time.

    Output is byte-identical to
        path.write_text(json.dumps({"generated_at": ..., "corpus_name": ...,
                                     "total_cases": N, "cases": cases}, indent=2))
    but never builds the whole corpus as one in-memory string/chunk list.
    Safe re-indent: json.dumps escapes newlines inside strings, so every raw
    newline in a case's dump is structural."""
    header = [
        ("generated_at", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
        ("corpus_name", corpus_name),
        ("total_cases", total_cases),
    ]
    written = 0
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("{\n")
        for key, val in header:
            fh.write(f"  {json.dumps(key)}: {json.dumps(val)},\n")
        if total_cases == 0:
            fh.write('  "cases": []\n}')
            return
        fh.write('  "cases": [\n')
        last = total_cases - 1
        for i, case in enumerate(case_iter):
            fh.write("    " + json.dumps(case, indent=2).replace("\n", "\n    "))
            fh.write(",\n" if i < last else "\n")
            written += 1
        fh.write("  ]\n}")
    if written != total_cases:
        raise RuntimeError(f"archive case count mismatch: header {total_cases}, wrote {written}")


def write_full_records(path: Path, corpus_name: str, cases: List[Dict]) -> None:
    write_full_records_stream(path, corpus_name, len(cases), iter(cases))

# ──────────────────────────────────────────────────────────────────────────
# Phase 4 — HASSH fingerprinting (Tool 35 logic — operates on in-memory cases)
# ──────────────────────────────────────────────────────────────────────────

_CLIENT_FAMILIES = [
    (r"paramiko", "Paramiko (Python)"),
    (r"libssh", "libssh"),
    (r"openssh", "OpenSSH"),
    (r"go-ssh|golang", "Go SSH library"),
    (r"putty", "PuTTY"),
]
_BOTNET_KEX_SIGNATURES = [
    (r"diffie-hellman-group1-sha1", "Legacy/scanner KEX (DH-group1-sha1)"),
]


def classify_client(version_string: str) -> str:
    v = (version_string or "").lower()
    for pattern, family in _CLIENT_FAMILIES:
        if re.search(pattern, v):
            return family
    return "Unknown"


def classify_kex(kex_string: str) -> Optional[str]:
    k = (kex_string or "").lower()
    for pattern, sig in _BOTNET_KEX_SIGNATURES:
        if re.search(pattern, k):
            return sig
    return None


def normalise_alg(val) -> str:
    if isinstance(val, list):
        return ",".join(val)
    return str(val or "")


def compute_hassh(kex_algs: str, enc_algs: str, mac_algs: str, comp_algs: str) -> str:
    raw = ";".join([kex_algs, enc_algs, mac_algs, comp_algs])
    return hashlib.md5(raw.encode()).hexdigest()


def new_fp_sessions():
    return defaultdict(lambda: {
        "session_id": None, "src_ip": None, "timestamp": None,
        "version": None, "kex_algs": None, "enc_algs_client": None,
        "mac_algs": None, "comp_algs": None,
    })


def extract_fingerprints_from_cases(cases: List[Dict], sessions=None) -> Dict[str, Dict]:
    """sessions: optional shared accumulator (used by the streaming path, which
    feeds one case at a time). Same merge semantics either way."""
    shared = sessions is not None
    if not shared:
        sessions = new_fp_sessions()
    for case in cases:
        events = case.get("timeline", [])
        case_id = case.get("case_id", "")
        src_ip = case.get("src_ip", "")
        for evt in events:
            etype = evt.get("event", evt.get("eventid", ""))
            session = evt.get("session", case_id)
            ts = evt.get("timestamp", "")
            if not sessions[session]["session_id"]:
                sessions[session]["session_id"] = session
                sessions[session]["src_ip"] = src_ip
                sessions[session]["timestamp"] = ts
            if etype == "cowrie.client.version":
                sessions[session]["version"] = evt.get("version", evt.get("client", ""))
            elif etype == "cowrie.client.kex":
                sessions[session]["kex_algs"] = normalise_alg(evt.get("kexAlgs", ""))
                sessions[session]["enc_algs_client"] = normalise_alg(evt.get("encCS", ""))
                sessions[session]["mac_algs"] = normalise_alg(evt.get("macCS", ""))
                sessions[session]["comp_algs"] = normalise_alg(evt.get("compCS", ""))
    return sessions if shared else dict(sessions)


def aggregate_fingerprints(sessions: Dict[str, Dict]) -> Tuple[Dict, int]:
    fp_map = defaultdict(lambda: {
        "hassh": None, "client_family": "Unknown", "botnet_signature": None,
        "version_strings": [], "session_count": 0, "unique_ips": set(),
        "sessions": [], "kex_algs": None, "enc_algs": None, "mac_algs": None,
        "comp_algs": None, "first_seen": None, "last_seen": None,
    })
    no_kex = 0
    for sid, sess in sessions.items():
        if not sess["kex_algs"] and not sess["version"]:
            no_kex += 1
            continue
        hassh = compute_hassh(sess["kex_algs"] or "", sess["enc_algs_client"] or "",
                               sess["mac_algs"] or "", sess["comp_algs"] or "")
        rec = fp_map[hassh]
        rec["hassh"] = hassh
        rec["session_count"] += 1
        rec["sessions"].append(sid)
        if sess["src_ip"]:
            rec["unique_ips"].add(sess["src_ip"])
        if sess["version"] and sess["version"] not in rec["version_strings"]:
            rec["version_strings"].append(sess["version"])
        if not rec["kex_algs"] and sess["kex_algs"]:
            rec["kex_algs"] = sess["kex_algs"]
            rec["enc_algs"] = sess["enc_algs_client"]
            rec["mac_algs"] = sess["mac_algs"]
            rec["comp_algs"] = sess["comp_algs"]
        if sess["version"]:
            fam = classify_client(sess["version"])
            if fam != "Unknown":
                rec["client_family"] = fam
        if not rec["botnet_signature"] and sess["kex_algs"]:
            sig = classify_kex(sess["kex_algs"])
            if sig:
                rec["botnet_signature"] = sig
        ts = sess.get("timestamp") or ""
        if ts:
            if not rec["first_seen"] or ts < rec["first_seen"]:
                rec["first_seen"] = ts
            if not rec["last_seen"] or ts > rec["last_seen"]:
                rec["last_seen"] = ts

    result = {}
    for hassh, rec in fp_map.items():
        result[hassh] = {**rec, "unique_ips": sorted(rec["unique_ips"]),
                          "unique_ip_count": len(rec["unique_ips"])}
    return result, no_kex


def build_fingerprint_output(fp_map: Dict, total_sessions: int, no_kex: int) -> Dict:
    fingerprints = sorted(fp_map.values(), key=lambda r: -r["session_count"])
    top_families: Dict[str, int] = defaultdict(int)
    for r in fingerprints:
        top_families[r["client_family"]] += r["session_count"]
    botnet_signals = [
        {"hassh": r["hassh"], "signature": r["botnet_signature"],
         "session_count": r["session_count"], "unique_ips": r["unique_ips"]}
        for r in fingerprints if r["botnet_signature"]
    ]
    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_sessions_parsed": total_sessions,
        "sessions_with_fingerprint": sum(r["session_count"] for r in fingerprints),
        "sessions_without_kex": no_kex,
        "unique_fingerprints": len(fingerprints),
        "top_families": [{"family": k, "sessions": v}
                          for k, v in sorted(top_families.items(), key=lambda kv: -kv[1])],
        "botnet_signals": botnet_signals,
    }


# ──────────────────────────────────────────────────────────────────────────
# Phase 5 — threat_ips, --skip-enrich only (no API calls, ever, in Tool 00)
# ──────────────────────────────────────────────────────────────────────────

def build_threat_ips_no_enrich(cases: List[Dict]) -> Dict:
    """enriched: false always. Tool 00 never calls AbuseIPDB/OTX — see
    session decision: zero shared API quota risk with the live pipeline."""
    ip_first: Dict[str, str] = {}
    ip_last: Dict[str, str] = {}
    ip_sessions: Dict[str, int] = defaultdict(int)

    for c in cases:
        ip = c.get("src_ip", "")
        if not ip or ip == "unknown":
            continue
        fs, ls = c.get("first_seen", ""), c.get("last_seen", "")
        ip_sessions[ip] += 1
        if fs and (ip not in ip_first or fs < ip_first[ip]):
            ip_first[ip] = fs
        if ls and (ip not in ip_last or ls > ip_last[ip]):
            ip_last[ip] = ls

    ips = [
        {
            "indicator": ip, "type": "ip",
            "first_seen": ip_first.get(ip, ""), "last_seen": ip_last.get(ip, ""),
            "session_count": count,
            "abuse_score": None, "country": None, "isp": None,
            "asn": None, "asn_name": None, "org": None,
            "is_tor": None, "is_proxy": None, "is_vpn": None, "otx_pulses": None,
        }
        for ip, count in ip_sessions.items()
    ]
    ips.sort(key=lambda r: -r["session_count"])

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "enriched": False,
        "total_ips": len(ips),
        "ips": ips,
    }


# ──────────────────────────────────────────────────────────────────────────
# Phase 7 — Command clustering (Tool 36 logic — operates on in-memory cases;
# geo fields come back null since threat_ips has no enrichment under
# --skip-enrich, exactly like the live BUG-4 lesson but intentional here)
# ──────────────────────────────────────────────────────────────────────────

_TTP_CLUSTER_PATTERNS = [
    (r"wget|curl", "T1105", "Ingress Tool Transfer"),
    (r"chmod\s+\+x", "T1222", "File and Directory Permissions Modification"),
    (r"authorized_keys", "T1098.004", "SSH Authorized Keys"),
    (r"crontab|systemctl", "T1053", "Scheduled Task/Job"),
    (r"history\s+-c", "T1070", "Indicator Removal"),
]


def normalize_command(cmd: str) -> str:
    cmd = cmd.lower().strip()
    cmd = re.sub(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "<IP>", cmd)
    cmd = re.sub(r"https?://[^\s]+", "<URL>", cmd)
    cmd = re.sub(r"\s+", " ", cmd)
    return cmd


def sequence_hash(commands: List[str]) -> str:
    joined = "|".join(normalize_command(c) for c in commands)
    return hashlib.sha256(joined.encode()).hexdigest()[:16]


def jaccard(seq_a: List[str], seq_b: List[str]) -> float:
    set_a = set(normalize_command(c) for c in seq_a)
    set_b = set(normalize_command(c) for c in seq_b)
    if not set_a and not set_b:
        return 1.0
    union = len(set_a | set_b)
    return (len(set_a & set_b) / union) if union else 0.0


def detect_cluster_ttps(commands: List[str]) -> List[Dict]:
    full_text = " ".join(commands).lower()
    out = []
    for pattern, ttp_id, name in _TTP_CLUSTER_PATTERNS:
        if re.search(pattern, full_text, re.IGNORECASE):
            out.append({"id": ttp_id, "name": name})
    return out


def extract_command_sessions(cases: List[Dict]) -> List[Dict]:
    sessions = []
    for case in cases:
        commands = [c.strip() for c in case.get("commands", []) if c and c.strip()]
        if not commands:
            continue
        sessions.append({
            "session_id": case.get("case_id", ""),
            "src_ip": case.get("src_ip", ""),
            "country": None,   # --skip-enrich: no geo lookup performed
            "isp": None,
            "commands": commands,
            "command_count": len(commands),
            "timestamp": case.get("first_seen", ""),
        })
    return sessions


def cluster_sessions(sessions: List[Dict], threshold: float = 0.7) -> List[Dict]:
    clusters: List[Dict] = []
    seed_sets: List[frozenset] = []          # precomputed once per cluster
    placed_by_hash: Dict[str, int] = {}      # identical sequence -> cluster idx
    for sess in sessions:
        h = sequence_hash(sess["commands"])
        idx = placed_by_hash.get(h)
        if idx is not None:                  # same normalised sequence seen before
            clusters[idx]["members"].append(sess)
            continue
        sset = frozenset(normalize_command(c) for c in sess["commands"])
        la = len(sset)
        idx = None
        for i, bset in enumerate(seed_sets):
            lb = len(bset)
            lo, hi = (la, lb) if la < lb else (lb, la)
            if hi and lo / hi < threshold:   # jaccard can't reach threshold
                continue
            if len(sset & bset) / len(sset | bset) >= threshold:
                idx = i
                break
        if idx is None:
            idx = len(clusters)
            clusters.append({
                "cluster_id": f"CLU-{idx+1:03d}",
                "seed_commands": sess["commands"],
                "members": [],
                "sequence_hash": h,
            })
            seed_sets.append(sset)
        clusters[idx]["members"].append(sess)
        placed_by_hash[h] = idx
    for cl in clusters:
        all_cmds = [c for m in cl["members"] for c in m["commands"]]
        cl["ttps"] = detect_cluster_ttps(all_cmds)
        unique_ips = {m["src_ip"] for m in cl["members"] if m["src_ip"]}
        cl["is_campaign"] = len(cl["members"]) > 5 and len(unique_ips) > 3
        cl["campaign_name"] = None
        cl["campaign_severity"] = None
        cl["campaign_description"] = None
        cl["matched_campaigns"] = []
    return clusters


def build_clusters_output(clusters: List[Dict], total_sessions: int) -> Dict:
    serializable = []
    for cl in clusters:
        members_summary = [
            {"session_id": m["session_id"], "src_ip": m["src_ip"],
             "country": m["country"], "isp": m["isp"],
             "command_count": m["command_count"], "timestamp": m["timestamp"]}
            for m in cl["members"]
        ]
        unique_ips = list({m["src_ip"] for m in cl["members"] if m["src_ip"]})
        serializable.append({
            "cluster_id": cl["cluster_id"], "is_campaign": cl["is_campaign"],
            "campaign_name": cl["campaign_name"], "campaign_severity": cl["campaign_severity"],
            "campaign_description": cl["campaign_description"],
            "matched_campaigns": cl["matched_campaigns"],
            "session_count": len(cl["members"]), "unique_ips": unique_ips,
            "unique_ip_count": len(unique_ips), "sequence_hash": cl["sequence_hash"],
            "ttps": cl["ttps"], "representative_commands": cl["seed_commands"][:10],
            "members": members_summary,
        })
    campaigns = [c for c in serializable if c["is_campaign"]]
    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_sessions_with_commands": total_sessions,
        "total_clusters": len(serializable),
        "campaign_clusters": len(campaigns),
        "singleton_clusters": len([c for c in serializable if c["session_count"] == 1]),
        "active_campaigns": [c["cluster_id"] for c in campaigns],
        "clusters": serializable,
    }


# ──────────────────────────────────────────────────────────────────────────
# Phase 6b — Corpus highlights (lightweight, no-PII summary of the five
# categories that are no longer written to the repo in full: ir_cases,
# credentials, ssh_fingerprints, threat_ips, command_clusters. Every field
# here must be a COUNT or a LABEL — never a raw IP, credential, command,
# fingerprint, or session ID. The full row-level data for all five
# categories lives exclusively in the R2 full-record archive; this file
# exists only to prove those five analysis passes ran and show their shape.
# ──────────────────────────────────────────────────────────────────────────

def build_corpus_highlights(cases: List[Dict], credentials: Dict,
                             ssh_fingerprints: Dict, threat_ips: Dict,
                             command_clusters: Dict) -> Dict:
    severity_breakdown: Dict[str, int] = defaultdict(int)
    for c in cases:
        severity_breakdown[c.get("severity", "LOW")] += 1
    return build_corpus_highlights_from_counts(len(cases), severity_breakdown, credentials,
                                                ssh_fingerprints, threat_ips, command_clusters)


def build_corpus_highlights_from_counts(total_cases: int, severity_breakdown: Dict[str, int],
                                         credentials: Dict, ssh_fingerprints: Dict,
                                         threat_ips: Dict, command_clusters: Dict) -> Dict:
    total_pairs = credentials.get("unique_pairs", 0)
    diversity_index = (
        "high" if total_pairs > 5000 else
        "medium" if total_pairs > 500 else
        "low"
    )

    return {
        "ir_cases": {
            "total_sessions": total_cases,
            "severity_breakdown": {
                "critical": severity_breakdown.get("CRITICAL", 0),
                "high": severity_breakdown.get("HIGH", 0),
                "medium": severity_breakdown.get("MEDIUM", 0),
                "low": severity_breakdown.get("LOW", 0),
            },
        },
        "credentials": {
            "total_attempts": credentials.get("total_attempts", 0),
            "unique_username_password_pairs": credentials.get("unique_pairs", 0),
            "unique_usernames": credentials.get("unique_usernames", 0),
            "unique_passwords": credentials.get("unique_passwords", 0),
            "successful_auth_count": credentials.get("total_successful_logins", 0),
            "credential_diversity_index": diversity_index,
        },
        "ssh_fingerprints": {
            "unique_hassh_values": ssh_fingerprints.get("unique_fingerprints", 0),
            "known_client_families_identified": len(ssh_fingerprints.get("top_families", [])),
            "sessions_without_kex": ssh_fingerprints.get("sessions_without_kex", 0),
            "botnet_signature_matches": len(ssh_fingerprints.get("botnet_signals", [])),
        },
        "threat_ips": {
            "unique_source_ips": threat_ips.get("total_ips", 0),
            "enriched": threat_ips.get("enriched", False),
            "note": "geo/ASN/abuse-score enrichment not performed by the "
                    "historical processor — --skip-enrich is permanent",
        },
        "command_clusters": {
            "total_clusters": command_clusters.get("total_clusters", 0),
            "campaign_clusters": command_clusters.get("campaign_clusters", 0),
            "singleton_clusters": command_clusters.get("singleton_clusters", 0),
            "largest_cluster_session_count": max(
                (cl["session_count"] for cl in command_clusters.get("clusters", [])),
                default=0,
            ),
        },
    }


# ──────────────────────────────────────────────────────────────────────────
# Phase 6 — Stats aggregation (genuinely new — no existing tool equivalent)
# ──────────────────────────────────────────────────────────────────────────

def build_stats(cases: List[Dict], credentials: Dict, ttp_counter: Dict[str, int]) -> Dict:
    sessions_per_day: Dict[str, int] = defaultdict(int)
    ip_sessions: Dict[str, int] = defaultdict(int)

    for c in cases:
        day = (c.get("first_seen") or "")[:10]
        if day:
            sessions_per_day[day] += 1
        ip = c.get("src_ip", "")
        if ip and ip != "unknown":
            ip_sessions[ip] += 1
    return build_stats_from_counts(len(cases), sessions_per_day, ip_sessions,
                                    credentials, ttp_counter)


def build_stats_from_counts(total_sessions: int, sessions_per_day: Dict[str, int],
                             ip_sessions: Dict[str, int], credentials: Dict,
                             ttp_counter: Dict[str, int]) -> Dict:
    countries = set()  # always empty under --skip-enrich; kept for schema stability

    daily_series = [{"date": d, "sessions": n} for d, n in sorted(sessions_per_day.items())]
    counts = [d["sessions"] for d in daily_series]
    day_median = median(counts) if counts else 0

    anomaly_days = []
    for d in daily_series:
        if day_median > 0 and d["sessions"] > 3 * day_median:
            anomaly_days.append({
                "date": d["date"], "sessions": d["sessions"],
                "vs_median": f"{d['sessions'] / day_median:.0f}x",
                "note": "anomalous volume — investigate",
            })

    top_ips = sorted(ip_sessions.items(), key=lambda kv: -kv[1])[:10]

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "date_range": {
            "start": daily_series[0]["date"] if daily_series else None,
            "end": daily_series[-1]["date"] if daily_series else None,
        },
        "total_sessions": total_sessions,
        "total_unique_ips": len(ip_sessions),
        "total_unique_countries": len(countries),
        "sessions_per_day": daily_series,
        "daily_median": day_median,
        "anomaly_days": anomaly_days,
        "top_source_ips": [{"ip": ip, "session_count": n} for ip, n in top_ips],
        "top_credential_pairs": credentials.get("top_pairs", [])[:20],
        "ttp_frequency": [{"ttp": k, "count": v}
                           for k, v in sorted(ttp_counter.items(), key=lambda kv: -kv[1])],
    }


# ──────────────────────────────────────────────────────────────────────────
# Phase 8 — EOF detection
# ──────────────────────────────────────────────────────────────────────────

def check_eof(output_dir: Path, current_listing_path: Optional[str],
              verbose: bool) -> Tuple[bool, List[str]]:
    """Compare --current-listing (R2 `rclone lsf --recursive` output) against
    the previous run's corpus_metadata.json files_processed_list.
    Returns (is_eof, current_listing).
    """
    if not current_listing_path:
        return False, []

    listing_file = Path(current_listing_path)
    if not listing_file.exists():
        log_warn(f"--current-listing file not found: {current_listing_path} — skipping EOF check")
        return False, []

    current_listing = sorted(
        line.strip() for line in listing_file.read_text().splitlines() if line.strip()
    )

    meta_path = output_dir / "corpus_metadata.json"
    if not meta_path.exists():
        log_info("No previous corpus_metadata.json — first run, not EOF", verbose)
        return False, current_listing

    try:
        prev_meta = json.loads(meta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        log_warn(f"Could not read previous corpus_metadata.json: {exc} — not EOF")
        return False, current_listing

    prev_listing = sorted(prev_meta.get("files_processed_list", []))

    if prev_listing and prev_listing == current_listing:
        log_info("Current R2 listing identical to previous run — EOF condition met", verbose)
        return True, current_listing

    return False, current_listing


def write_eof_marker(output_dir: Path, final_file_count: int) -> None:
    eof_path = output_dir / ".EOF"
    eof_payload = {
        "marked_complete_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "final_file_count": final_file_count,
        "reason": "no new files since last run",
    }
    eof_path.write_text(json.dumps(eof_payload, indent=2))
    log_info(f"Wrote EOF marker: {eof_path}")



# ──────────────────────────────────────────────────────────────────────────
# Phase 10 — Incremental mode (--incremental --state-dir)
#
# Unit of state is one rotated log file F, stored as two parts:
#   file_level  — facts about the lines physically in F (login events,
#                 unparseable-line count). Never changes once F is read.
#   home_level  — everything about the CASES whose first event is in F
#                 (counters, ordered dicts, distinct command sequences,
#                 fingerprint classification, archive fragment). A case can
#                 include events from F+1, so home_level of the newest file is
#                 PROVISIONAL and is recomputed on the next run.
# Each run reads: one file of context before the provisional file (to tell
# which sessions started earlier), the provisional file, and the new files.
# Outputs are then rebuilt by folding all shards in file order, which
# reproduces what a full run computes (same dict insertion orders, same
# first-fit clustering over distinct command sequences).
# Limitation: a session spanning more than two rotation boundaries (>~24 h)
# is not reassembled; the periodic full run is the cross-check.
# ──────────────────────────────────────────────────────────────────────────

INC_VERSION = 1


def _atomic_write_gz_json(path: Path, obj) -> None:
    tmp = path.with_name(path.name + ".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8") as fh:
        json.dump(obj, fh, separators=(",", ":"))
    os.replace(tmp, path)


def _read_gz_json(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return json.load(fh)


class HomeAcc:
    """Counters for the cases homed in one file. Dicts keep first-occurrence
    order, which later tie-breaking sorts depend on."""

    def __init__(self) -> None:
        self.cases = 0
        self.severity: Dict[str, int] = {}
        self.daily: Dict[str, int] = {}
        self.ttp: Dict[str, int] = {}
        self.ips: Dict[str, int] = {}
        self.fp = new_fp_sessions()
        self.seqs: Dict[str, list] = {}   # hash -> [commands, count, {ip: None}]
        self.first_min: Optional[str] = None
        self.first_max: Optional[str] = None

    def add(self, case: Dict) -> None:
        self.cases += 1
        sev = case.get("severity", "LOW")
        self.severity[sev] = self.severity.get(sev, 0) + 1
        fs = case.get("first_seen") or ""
        day = fs[:10]
        if day:
            self.daily[day] = self.daily.get(day, 0) + 1
        for t in case.get("ttps", []):
            self.ttp[t] = self.ttp.get(t, 0) + 1
        ip = case.get("src_ip", "")
        if ip and ip != "unknown":
            self.ips[ip] = self.ips.get(ip, 0) + 1
        extract_fingerprints_from_cases([case], self.fp)
        cmds = [c.strip() for c in case.get("commands", []) if c and c.strip()]
        if cmds:
            h = sequence_hash(cmds)
            ent = self.seqs.get(h)
            if ent is None:
                ent = self.seqs[h] = [cmds, 0, {}]
            ent[1] += 1
            if ip:
                ent[2][ip] = None
        if self.first_min is None or fs < self.first_min:
            self.first_min = fs
        if self.first_max is None or fs > self.first_max:
            self.first_max = fs

    def to_json(self, final: bool) -> Dict:
        fp_map, no_kex = aggregate_fingerprints(self.fp)
        return {
            "final": final, "cases": self.cases,
            "severity": self.severity, "daily": self.daily, "ttp": self.ttp,
            "ips": self.ips,
            "fp": {h: [r["client_family"], r["botnet_signature"]] for h, r in fp_map.items()},
            "no_kex": no_kex,
            "seqs": [[h, e[0], e[1], list(e[2])] for h, e in self.seqs.items()],
            "first_min": self.first_min, "first_max": self.first_max,
        }


def _file_level(path: Path, skipped: int) -> Dict:
    attempts, successes = parse_credentials_from_file(path)
    pairs: Dict[Tuple[str, str], int] = {}
    users: Dict[str, int] = {}
    pwds: Dict[str, int] = {}
    for a in attempts:
        pairs[(a["username"], a["password"])] = pairs.get((a["username"], a["password"]), 0) + 1
        users[a["username"]] = users.get(a["username"], 0) + 1
        pwds[a["password"]] = pwds.get(a["password"], 0) + 1
    return {
        "lines_skipped": skipped, "attempts": len(attempts), "successes": len(successes),
        "pairs": [[u, p, c] for (u, p), c in pairs.items()],
        "users": list(users.items()), "pwds": list(pwds.items()),
    }


class ClusterReplay:
    """Same first-fit clustering as cluster_sessions(), fed distinct command
    sequences (with counts and IPs) in global first-appearance order."""

    def __init__(self, threshold: float = 0.7) -> None:
        self.t = threshold
        self.seed_sets: List[frozenset] = []
        self.members: List[int] = []
        self.ips: List[set] = []
        self.by_hash: Dict[str, int] = {}

    def add(self, h: str, commands: List[str], count: int, ips: List[str]) -> None:
        idx = self.by_hash.get(h)
        if idx is None:
            sset = frozenset(normalize_command(c) for c in commands)
            la = len(sset)
            for i, bset in enumerate(self.seed_sets):
                lb = len(bset)
                lo, hi = (la, lb) if la < lb else (lb, la)
                if hi and lo / hi < self.t:
                    continue
                if len(sset & bset) / len(sset | bset) >= self.t:
                    idx = i
                    break
            if idx is None:
                idx = len(self.seed_sets)
                self.seed_sets.append(sset)
                self.members.append(0)
                self.ips.append(set())
            self.by_hash[h] = idx
        self.members[idx] += count
        self.ips[idx].update(ips)

    def summary(self, total_sessions: int) -> Dict:
        campaigns = sum(1 for m, ips in zip(self.members, self.ips) if m > 5 and len(ips) > 3)
        return {
            "total_sessions_with_commands": total_sessions,
            "total_clusters": len(self.members),
            "campaign_clusters": campaigns,
            "singleton_clusters": sum(1 for m in self.members if m == 1),
            "clusters": [{"session_count": m} for m in self.members],
        }


def run_incremental(args, output_dir: Path, current_listing: List[str], verbose: bool) -> None:
    if not args.state_dir:
        fatal("--incremental requires --state-dir")
    state = Path(args.state_dir)
    (state / "shards").mkdir(parents=True, exist_ok=True)
    (state / "cases").mkdir(parents=True, exist_ok=True)
    manifest_path = state / "manifest.json"
    manifest: Dict[str, Dict] = {}
    if manifest_path.exists():
        m = json.loads(manifest_path.read_text())
        if m.get("version") != INC_VERSION:
            fatal(f"state manifest version {m.get('version')} != {INC_VERSION}; run a full pass")
        manifest = m["files"]

    files_all = discover_log_files(args.log_dir, args.start_date, args.end_date, verbose)
    names = [p.name for p in files_all]
    by_name = {p.name: p for p in files_all}

    new = [n for n in names if n not in manifest]
    if manifest and new and min(new) < max(manifest):
        fatal("a new log file is older than files already in state — incremental mode "
              "cannot reorder history; run a full pass to rebuild state")
    missing = [n for n in manifest if n not in by_name]
    if missing:
        log_info(f"{len(missing)} file(s) known from state are not on disk "
                 f"(expected — only needed logs are downloaded; their shards are reused)", verbose)
    if not new:
        log_info(f"[{args.corpus_name}] No new log files — nothing to process.", verbose)
        return

    provisional = [n for n in names if n in manifest and not manifest[n]["final"]]
    P = sorted(provisional + new)
    prev = None
    first_idx = names.index(P[0])
    if first_idx > 0:
        prev = names[first_idx - 1]
        if prev not in manifest:
            fatal(f"internal: context file {prev} has no shard")
    R = ([by_name[prev]] if prev else []) + [by_name[n] for n in P]
    log_info(f"Incremental: {len(new)} new, {len(provisional)} provisional, "
             f"context={prev}, reading {len(R)} file(s)", verbose)

    spill = args.spill_dir or str(state / "spill")
    store = SpillStore(R, spill, verbose)
    accs = {n: HomeAcc() for n in P}
    handles: Dict[str, Any] = {}
    wrote_first: Dict[str, bool] = {}
    try:
        store.build()
        for home, case in store.iter_cases_with_home():
            if home == prev or home not in accs:
                continue                       # started earlier: owned by an older shard
            accs[home].add(case)
            fh = handles.get(home)
            if fh is None:
                fh = handles[home] = gzip.open(state / "cases" / f"{home}.cases.gz.tmp",
                                                "wt", encoding="utf-8", newline="")
                wrote_first[home] = False
            if wrote_first[home]:
                fh.write(",\n")
            fh.write("    " + json.dumps(case, indent=2).replace("\n", "\n    "))
            wrote_first[home] = True
        skipped = dict(store.skipped_by_file)
    finally:
        for fh in handles.values():
            fh.close()
        store.close()
    log_mem("after incremental read", verbose)

    for n in P:
        tmp = state / "cases" / f"{n}.cases.gz.tmp"
        final_path = state / "cases" / f"{n}.cases.gz"
        if tmp.exists():
            os.replace(tmp, final_path)
        else:                                   # no cases homed in this file
            with gzip.open(final_path, "wt", encoding="utf-8") as fh:
                fh.write("")
        shard_path = state / "shards" / f"{n}.json.gz"
        if n in manifest:                      # provisional: file_level is already final
            file_level = _read_gz_json(shard_path)["file_level"]
        else:
            file_level = _file_level(by_name[n], skipped.get(n, 0))
        final = n != P[-1]
        _atomic_write_gz_json(shard_path, {"version": INC_VERSION, "file": n,
                                            "file_level": file_level,
                                            "home": accs[n].to_json(final)})
        manifest[n] = {"final": final}
    tmp_m = manifest_path.with_name("manifest.json.tmp")
    tmp_m.write_text(json.dumps({"version": INC_VERSION, "files": manifest}, indent=1))
    os.replace(tmp_m, manifest_path)

    # ---- fold every shard, in file order, into the corpus-wide figures ----
    order = sorted(manifest)
    cred = CredentialAccumulator()
    severity: Dict[str, int] = {}
    daily: Dict[str, int] = {}
    ttp: Dict[str, int] = {}
    ips: Dict[str, int] = {}
    fp_slots: Dict[str, list] = {}           # hassh -> [family, botnet_sig]
    no_kex = lines_skipped = total_cases = cmd_sessions = 0
    replay = ClusterReplay()
    last_max: Optional[str] = None
    frag_files: List[Path] = []
    for n in order:
        sh = _read_gz_json(state / "shards" / f"{n}.json.gz")
        fl, hm = sh["file_level"], sh["home"]
        lines_skipped += fl["lines_skipped"]
        for u, p, c in fl["pairs"]:
            cred.pair_counts[(u, p)] += c
        for u, c in fl["users"]:
            cred.username_counts[u] += c
        for pw, c in fl["pwds"]:
            cred.password_counts[pw] += c
        cred.total_attempts += fl["attempts"]
        cred.success_total += fl["successes"]
        total_cases += hm["cases"]
        for src, dst in ((hm["severity"], severity), (hm["daily"], daily),
                         (hm["ttp"], ttp), (hm["ips"], ips)):
            for k, v in src.items():
                dst[k] = dst.get(k, 0) + v
        for h, (fam, sig) in hm["fp"].items():
            slot = fp_slots.setdefault(h, ["Unknown", None])
            if fam != "Unknown":
                slot[0] = fam
            if slot[1] is None:
                slot[1] = sig
        no_kex += hm["no_kex"]
        for h, cmds, cnt, sips in hm["seqs"]:
            replay.add(h, cmds, cnt, sips)
            cmd_sessions += cnt
        if hm["cases"]:
            if last_max is not None and hm["first_min"] < last_max:
                fatal(f"case order across shards violated at {n} "
                      f"({hm['first_min']} < {last_max}); run a full pass")
            last_max = hm["first_max"]
            frag_files.append(state / "cases" / f"{n}.cases.gz")
    if total_cases == 0:
        fatal("No sessions in state — aborting before writing output")

    credentials = cred.result()
    ssh_fp = {
        "unique_fingerprints": len(fp_slots),
        "top_families": [{"family": f} for f in sorted({v[0] for v in fp_slots.values()})],
        "sessions_without_kex": no_kex,
        "botnet_signals": [h for h, v in fp_slots.items() if v[1]],
    }
    threat_ips = {"enriched": False, "total_ips": len(ips)}
    command_clusters = replay.summary(cmd_sessions)
    stats = build_stats_from_counts(total_cases, daily, ips, credentials, ttp)
    highlights = build_corpus_highlights_from_counts(
        total_cases, severity, credentials, ssh_fp, threat_ips, command_clusters)

    # ---- cumulative archive: stream fragments, no parsing ----
    full_records_path = Path(args.full_records_out) if args.full_records_out \
        else output_dir / ".full_records_tmp.json"
    with open(full_records_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("{\n")
        for key, val in (("generated_at", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")),
                         ("corpus_name", args.corpus_name), ("total_cases", total_cases)):
            fh.write(f"  {json.dumps(key)}: {json.dumps(val)},\n")
        fh.write('  "cases": [\n')
        for i, fp_ in enumerate(frag_files):
            if i:
                fh.write(",\n")
            with gzip.open(fp_, "rt", encoding="utf-8", newline="") as src:
                shutil.copyfileobj(src, fh)
        fh.write("\n  ]\n}")
    log_info(f"Wrote full (un-truncated) case records to {full_records_path} "
             f"— upload this to R2 live-archives/, then it can be deleted locally")

    (output_dir / "corpus_highlights.json").write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "corpus_name": args.corpus_name, **highlights}, indent=2))
    (output_dir / "historical_stats.json").write_text(
        json.dumps({"corpus_name": args.corpus_name, **stats}, indent=2))
    anomaly_dates = [a["date"] for a in stats["anomaly_days"]]
    (output_dir / "corpus_metadata.json").write_text(json.dumps({
        "corpus_name": args.corpus_name,
        "processed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "log_dir": args.log_dir, "date_range": stats["date_range"],
        "files_processed": len(manifest),
        "files_processed_list": current_listing if current_listing else sorted(manifest),
        "lines_skipped": lines_skipped, "sessions_extracted": total_cases,
        "unique_ips": len(ips), "enriched": False, "tool_version": TOOL_VERSION,
        "anomaly_days": anomaly_dates, "full_record_archive": str(full_records_path),
        "eof_status": "active",
    }, indent=2))
    log_info(f"[{args.corpus_name}] Done (incremental). {total_cases} sessions, "
             f"{len(ips)} unique IPs, {len(anomaly_dates)} anomaly day(s): {anomaly_dates}")


# ──────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Tool 00 — Historical Processor")
    p.add_argument("--log-dir", required=True,
                   help="Directory containing cowrie.json.YYYY-MM-DD[.gz] files")
    p.add_argument("--output-dir", required=True,
                   help="Directory to write historical_data output files")
    p.add_argument("--start-date", default=None, help="YYYY-MM-DD, inclusive")
    p.add_argument("--end-date", default=None, help="YYYY-MM-DD, inclusive")
    p.add_argument("--corpus-name", default="unnamed-corpus")
    p.add_argument("--skip-enrich", action="store_true", default=True,
                   help="Always true in Tool 00 — kept as a flag for spec "
                        "compatibility, but Tool 00 never performs live "
                        "enrichment regardless of this flag's value.")
    p.add_argument("--current-listing", default=None,
                   help="Path to rclone lsf --recursive output, for EOF detection")
    p.add_argument("--check-eof", action="store_true",
                   help="If set, run EOF detection and exit early if EOF condition met")
    p.add_argument("--full-records-out", default=None,
                   help="Path to write the FULL (un-truncated) case list, for "
                        "upload to R2 live-archives/ by the calling workflow. "
                        "If omitted, defaults to <output-dir>/.full_records_tmp.json")
    p.add_argument("--spill-dir", default=None,
                   help="If set, keep session events and finished cases on disk "
                        "(SQLite under this directory) instead of in memory, and stream "
                        "the full-record archive while building cases. Output is "
                        "byte-identical to the in-memory path; peak memory is far lower. "
                        "Needs free disk for the spill file (removed on exit).")
    p.add_argument("--incremental", action="store_true",
                   help="Process only log files not yet in --state-dir (plus the one "
                        "provisional file and one file of context), then rebuild every "
                        "output from the persisted per-file shards. Output is identical "
                        "to a full run. Requires --state-dir.")
    p.add_argument("--state-dir", default=None,
                   help="Directory holding per-file shards and archive fragments for "
                        "--incremental. Sync it to/from R2 around the run.")
    p.add_argument("--verbose", "-v", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    verbose = args.verbose
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ---- EOF short-circuit (before any file reading) ----
    if args.incremental:
        # the per-file manifest replaces the all-or-nothing .EOF lock
        current_listing = []
        if args.current_listing and Path(args.current_listing).exists():
            current_listing = sorted(
                l.strip() for l in Path(args.current_listing).read_text().splitlines() if l.strip())
        run_incremental(args, output_dir, current_listing, verbose)
        return
    if args.check_eof and args.current_listing:
        is_eof, current_listing = check_eof(output_dir, args.current_listing, verbose)
        if is_eof:
            write_eof_marker(output_dir, len(current_listing))
            log_info(f"[{args.corpus_name}] EOF — nothing new to process. Exiting cleanly.")
            return
    else:
        current_listing = []
        if args.current_listing:
            listing_file = Path(args.current_listing)
            if listing_file.exists():
                current_listing = sorted(
                    l.strip() for l in listing_file.read_text().splitlines() if l.strip()
                )

    eof_marker_path = output_dir / ".EOF"
    if eof_marker_path.exists():
        log_info(f"[{args.corpus_name}] .EOF marker present at {eof_marker_path} — "
                  f"skipping processing. Remove this file manually to force a re-run.")
        return

    # ---- Phase 1 ----
    files = discover_log_files(args.log_dir, args.start_date, args.end_date, verbose)

    full_records_path = Path(args.full_records_out) if args.full_records_out \
        else output_dir / ".full_records_tmp.json"

    # ---- Phase 2 ----
    spill_mode = bool(args.spill_dir)
    fp_sessions = None
    if spill_mode:
        # Events live in a temp SQLite file; each case is rebuilt, streamed to
        # the archive, reduced to the slim fields later phases use, and dropped.
        store = SpillStore(files, args.spill_dir, verbose)
        try:
            store.build()
            log_mem("after spill build", verbose)
            if store.total == 0:
                fatal("No sessions extracted from any input file — aborting before writing output")
            lines_skipped = store.lines_skipped
            fp_sessions = new_fp_sessions()
            cases = []   # slim records: everything Phases 3-7 read, minus timeline/downloads

            def _stream():
                for full in store.iter_cases():
                    extract_fingerprints_from_cases([full], fp_sessions)
                    cases.append({
                        "case_id": full["case_id"], "src_ip": full["src_ip"],
                        "first_seen": full["first_seen"], "last_seen": full["last_seen"],
                        "severity": full["severity"], "commands": full["commands"],
                        "ttps": full["ttps"],
                    })
                    yield full

            write_full_records_stream(full_records_path, args.corpus_name,
                                       store.total, _stream())
        finally:
            store.close()
        log_mem("after extraction + archive write", verbose)
        log_info(f"Wrote full (un-truncated) case records to {full_records_path} "
                 f"— upload this to R2 live-archives/, then it can be deleted locally")
    else:
        cases, lines_skipped = extract_sessions(files, verbose)
        if not cases:
            fatal("No sessions extracted from any input file — aborting before writing output")
        log_mem("after extraction", verbose)

    # ---- Phase 3 ----
    log_info("Extracting credentials...", verbose)
    cred_acc = CredentialAccumulator()
    for path in files:
        a, s = parse_credentials_from_file(path)
        cred_acc.add_file(a, s)
    credentials = cred_acc.result()
    log_mem("after credentials", verbose)

    # ---- Phase 5 (threat_ips — no enrichment, ever) ----
    log_info("Building threat_ips index (--skip-enrich, no API calls)...", verbose)
    threat_ips = build_threat_ips_no_enrich(cases)

    # ---- Phase 4 ----
    log_info("Computing SSH fingerprints...", verbose)
    if fp_sessions is None:
        fp_sessions = extract_fingerprints_from_cases(cases)
    fp_map, no_kex_count = aggregate_fingerprints(fp_sessions)
    ssh_fingerprints = build_fingerprint_output(fp_map, len(cases), no_kex_count)

    # ---- Phase 7 ----
    log_info("Clustering commands...", verbose)
    cmd_sessions = extract_command_sessions(cases)
    clusters = cluster_sessions(cmd_sessions, threshold=0.7)
    log_mem("after clustering", verbose)
    command_clusters = build_clusters_output(clusters, len(cmd_sessions))
    log_mem("after cluster output", verbose)

    # ---- Phase 6 (depends on everything above) ----
    log_info("Aggregating corpus-wide stats...", verbose)
    ttp_counter: Dict[str, int] = defaultdict(int)
    for c in cases:
        for t in c.get("ttps", []):
            ttp_counter[t] += 1
    stats = build_stats(cases, credentials, ttp_counter)
    log_mem("after stats", verbose)

    # ---- Output: full records (for R2 upload by the calling workflow) ----
    if not spill_mode:   # spill mode already streamed the archive during Phase 2
        write_full_records(full_records_path, args.corpus_name, cases)
        log_mem("after full-record write", verbose)
        log_info(f"Wrote full (un-truncated) case records to {full_records_path} "
                 f"— upload this to R2 live-archives/, then it can be deleted locally")

    # ---- Output: corpus_highlights.json (committed to repo) ----
    # Replaces the five raw per-category files (historical_ir_cases.json,
    # historical_credentials.json, historical_ssh_fingerprints.json,
    # historical_threat_ips.json, historical_command_clusters.json), none
    # of which are written to the repo anymore. Row-level data for all
    # five categories (IPs, credential pairs, fingerprints, commands,
    # session IDs) lives ONLY in the full R2 archive (full_records_path,
    # uploaded by the calling workflow) — never in git. This file is
    # counts and labels only; see build_corpus_highlights() docstring.
    highlights = build_corpus_highlights(
        cases, credentials, ssh_fingerprints, threat_ips, command_clusters)
    (output_dir / "corpus_highlights.json").write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "corpus_name": args.corpus_name,
        **highlights,
    }, indent=2))

    (output_dir / "historical_stats.json").write_text(
        json.dumps({"corpus_name": args.corpus_name, **stats}, indent=2))

    # ---- corpus_metadata.json — last, since it records what just happened ----
    anomaly_dates = [a["date"] for a in stats["anomaly_days"]]
    metadata = {
        "corpus_name": args.corpus_name,
        "processed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "log_dir": args.log_dir,
        "date_range": stats["date_range"],
        "files_processed": len(files),
        "files_processed_list": current_listing if current_listing else [f.name for f in files],
        "lines_skipped": lines_skipped,
        "sessions_extracted": len(cases),
        "unique_ips": threat_ips["total_ips"],
        "enriched": False,
        "tool_version": TOOL_VERSION,
        "anomaly_days": anomaly_dates,
        "full_record_archive": str(full_records_path),
        "eof_status": "active",
    }
    (output_dir / "corpus_metadata.json").write_text(json.dumps(metadata, indent=2))

    log_info(f"[{args.corpus_name}] Done. {len(cases)} sessions, "
              f"{threat_ips['total_ips']} unique IPs, "
              f"{len(anomaly_dates)} anomaly day(s): {anomaly_dates}")


if __name__ == "__main__":
    main()
