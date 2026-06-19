#!/usr/bin/env python3
"""
Tool 00  Historical Processor

Batch re-processes a directory of rotated Cowrie cowrie.json.* log files
(plain or .gz) through the same logic as Tools 26, 34, 35, and 36 — but
across an entire corpus instead of a single live log. Produces a
permanent historical_data/<corpus>/ baseline for either the AWS corpus
(thir-raw-archive, one-time) or the Oracle corpus (thirha-raw-archive,
recurring quarterly).

Run mode: one-shot, offline. NOT part of pipeline.yml. Does not touch
data/*.json, does not call Tool 37, does not update cowrie_watermark.json.

Output files (all under --output-dir):
    historical_ir_cases.json           — ID-only index (5 fields/case)
    historical_credentials.json        — same schema as data/credentials.json
    historical_ssh_fingerprints.json   — same schema as data/ssh_fingerprints.json
    historical_threat_ips.json         — IPs only, enriched=false (--skip-enrich)
    historical_command_clusters.json   — same schema as data/command_clusters.json
    historical_stats.json              — per-day time series + aggregates
    corpus_metadata.json               — run metadata, anomaly days, EOF status

Full (un-truncated) case records are written to a local temp file for
upload to R2 live-archives/ by the calling workflow — see
--full-records-out.

Standard library only. No pip installs. Python 3.8+.
"""

import argparse
import gzip
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median
from typing import Any, Dict, List, Optional, Tuple

TOOL_VERSION = "00.1.0"

# ──────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────

def log_info(msg: str, verbose: bool = True) -> None:
    if verbose:
        print(f"[Tool00] {msg}", file=sys.stderr)


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

    for session_id, events in sessions_raw.items():
        events_sorted = sorted(events, key=lambda e: e.get("timestamp", ""))
        safe_sid = sanitise_session_id(session_id)

        raw_ip = next((e.get("src_ip", "") for e in events_sorted if e.get("src_ip")), "")
        src_ip = raw_ip if raw_ip else "unknown"

        first_seen = events_sorted[0].get("timestamp", "") if events_sorted else ""
        last_seen = events_sorted[-1].get("timestamp", "") if events_sorted else ""

        dedup_key = cross_file_dedup_key(src_ip, session_id, first_seen)
        if dedup_key in seen_dedup_keys:
            continue
        seen_dedup_keys.add(dedup_key)

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
            "source_file": source_file_by_session.get(session_id, ""),
        }
        case["severity"] = calculate_severity(case)
        cases.append(case)

    cases.sort(key=lambda c: c.get("first_seen", ""))
    log_info(f"Built {len(cases)} deduplicated IR case(s)", verbose)
    return cases, lines_skipped


def build_index_records(cases: List[Dict]) -> List[Dict]:
    """The 5-field committed-to-repo index. Full case detail stays only
    in the in-memory `cases` list and the full-records archive file."""
    return [
        {
            "case_id": c["case_id"],
            "src_ip": c["src_ip"],
            "first_seen": c["first_seen"],
            "severity": c["severity"],
            "source_file": c["source_file"],
        }
        for c in cases
    ]


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
        "success_pairs": success_pairs[:_CRED_TOP_N],
    }


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


def extract_fingerprints_from_cases(cases: List[Dict]) -> Dict[str, Dict]:
    sessions = defaultdict(lambda: {
        "session_id": None, "src_ip": None, "timestamp": None,
        "version": None, "kex_algs": None, "enc_algs_client": None,
        "mac_algs": None, "comp_algs": None,
    })
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
    return dict(sessions)


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
    for sess in sessions:
        placed = False
        for cl in clusters:
            if jaccard(sess["commands"], cl["seed_commands"]) >= threshold:
                cl["members"].append(sess)
                placed = True
                break
        if not placed:
            clusters.append({
                "cluster_id": f"CLU-{len(clusters)+1:03d}",
                "seed_commands": sess["commands"],
                "members": [sess],
                "sequence_hash": sequence_hash(sess["commands"]),
            })
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
# Phase 6 — Stats aggregation (genuinely new — no existing tool equivalent)
# ──────────────────────────────────────────────────────────────────────────

def build_stats(cases: List[Dict], credentials: Dict, ttp_counter: Dict[str, int]) -> Dict:
    sessions_per_day: Dict[str, int] = defaultdict(int)
    ip_sessions: Dict[str, int] = defaultdict(int)
    countries = set()  # always empty under --skip-enrich; kept for schema stability

    for c in cases:
        day = (c.get("first_seen") or "")[:10]
        if day:
            sessions_per_day[day] += 1
        ip = c.get("src_ip", "")
        if ip and ip != "unknown":
            ip_sessions[ip] += 1

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
        "total_sessions": len(cases),
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
    p.add_argument("--verbose", "-v", action="store_true")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    verbose = args.verbose
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ---- EOF short-circuit (before any file reading) ----
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

    # ---- Phase 2 ----
    cases, lines_skipped = extract_sessions(files, verbose)
    if not cases:
        fatal("No sessions extracted from any input file — aborting before writing output")

    # ---- Phase 3 ----
    log_info("Extracting credentials...", verbose)
    all_attempts: List[Dict] = []
    success_pairs: List[Dict] = []
    for path in files:
        a, s = parse_credentials_from_file(path)
        all_attempts.extend(a)
        success_pairs.extend(s)
    credentials = aggregate_credentials(all_attempts, success_pairs)

    # ---- Phase 5 (threat_ips — no enrichment, ever) ----
    log_info("Building threat_ips index (--skip-enrich, no API calls)...", verbose)
    threat_ips = build_threat_ips_no_enrich(cases)

    # ---- Phase 4 ----
    log_info("Computing SSH fingerprints...", verbose)
    fp_sessions = extract_fingerprints_from_cases(cases)
    fp_map, no_kex_count = aggregate_fingerprints(fp_sessions)
    ssh_fingerprints = build_fingerprint_output(fp_map, len(cases), no_kex_count)

    # ---- Phase 7 ----
    log_info("Clustering commands...", verbose)
    cmd_sessions = extract_command_sessions(cases)
    clusters = cluster_sessions(cmd_sessions, threshold=0.7)
    command_clusters = build_clusters_output(clusters, len(cmd_sessions))

    # ---- Phase 6 (depends on everything above) ----
    log_info("Aggregating corpus-wide stats...", verbose)
    ttp_counter: Dict[str, int] = defaultdict(int)
    for c in cases:
        for t in c.get("ttps", []):
            ttp_counter[t] += 1
    stats = build_stats(cases, credentials, ttp_counter)

    # ---- Output: full records (for R2 upload by the calling workflow) ----
    full_records_path = Path(args.full_records_out) if args.full_records_out \
        else output_dir / ".full_records_tmp.json"
    full_payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "corpus_name": args.corpus_name,
        "total_cases": len(cases),
        "cases": cases,
    }
    full_records_path.write_text(json.dumps(full_payload, indent=2))
    log_info(f"Wrote full (un-truncated) case records to {full_records_path} "
             f"— upload this to R2 live-archives/, then it can be deleted locally")

    # ---- Output: index-only historical_ir_cases.json (committed to repo) ----
    index_records = build_index_records(cases)
    (output_dir / "historical_ir_cases.json").write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "corpus_name": args.corpus_name,
        "total_cases": len(index_records),
        "cases": index_records,
    }, indent=2))

    (output_dir / "historical_credentials.json").write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "corpus_name": args.corpus_name,
        **credentials,
    }, indent=2))

    (output_dir / "historical_ssh_fingerprints.json").write_text(
        json.dumps({"corpus_name": args.corpus_name, **ssh_fingerprints}, indent=2))

    (output_dir / "historical_threat_ips.json").write_text(
        json.dumps({"corpus_name": args.corpus_name, **threat_ips}, indent=2))

    (output_dir / "historical_command_clusters.json").write_text(
        json.dumps({"corpus_name": args.corpus_name, **command_clusters}, indent=2))

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
