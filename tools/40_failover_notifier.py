#!/usr/bin/env python3
"""
THIR Tool 40 — Failover Notifier
Reads data/failover_events.json (produced by Tool 39), deduplicates against
alert_history.json, and emits notifications via ALERT_CHANNEL.

Routing follows the same pattern as Tool 37:
  ALERT_CHANNEL=slack   → Slack webhook only
  ALERT_CHANNEL=email   → SMTP only
  ALERT_CHANNEL=both    → Slack + email
  ALERT_CHANNEL=dry-run → print to stdout, no external calls (default)

Severity:
  vm1_down   → CRITICAL  (primary sensor offline, failover active)
  vm2_down   → HIGH      (pipeline offline, dashboard stalling)
  vm1_up     → INFO      (primary restored, traffic returning)
  unknown    → MEDIUM

Exit codes:
  0 — completed (0 or more notifications sent)
  1 — input file missing or unreadable
  2 — environment / config error
"""

import json
import os
import sys
import hashlib
import smtplib
import urllib.request
import urllib.error
import datetime
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

FAILOVER_EVENTS  = Path("data/failover_events.json")
ALERT_HISTORY    = Path("data/alert_history.json")
OUTPUT_NOTIF     = Path("data/failover_notifications.json")

# ---------------------------------------------------------------------------
# Severity map keyed on HAProxy event type
# ---------------------------------------------------------------------------

SEVERITY_MAP = {
    "vm1_down":           "CRITICAL",
    "vm1_backend_down":   "CRITICAL",
    "vm2_down":           "HIGH",
    "vm2_backend_down":   "HIGH",
    "vm1_up":             "INFO",
    "vm1_backend_up":     "INFO",
    "vm2_up":             "INFO",
    "failover_active":    "CRITICAL",
    "failover_recovered": "INFO",
}

SEVERITY_EMOJI = {
    "CRITICAL": "🔴",
    "HIGH":     "🟠",
    "MEDIUM":   "🟡",
    "INFO":     "🟢",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def utcnow() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json_safe(path: Path, default):
    """Load JSON file; return default if absent or malformed."""
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def event_hash(event: dict) -> str:
    """
    Stable hash for deduplication.
    Keys: event_type + backend + timestamp (truncated to the minute).
    Truncating to the minute prevents duplicate alerts from rapid HAProxy
    state oscillation within a single pipeline window.
    """
    ts = event.get("timestamp", "")[:16]  # "2026-06-22T14:05"
    raw = f"{event.get('event_type','')}|{event.get('backend','')}|{ts}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def build_message(event: dict, severity: str) -> tuple[str, str]:
    """Return (subject, body) for the event."""
    etype    = event.get("event_type", "unknown")
    backend  = event.get("backend",    "unknown")
    ts       = event.get("timestamp",  utcnow())
    detail   = event.get("detail",     "")
    src_ip   = event.get("source_ip",  "")
    sessions = event.get("active_sessions", "")
    emoji    = SEVERITY_EMOJI.get(severity, "⚪")

    subject = f"[THIR] {emoji} {severity} — HAProxy failover: {etype} ({backend})"

    lines = [
        "THIR.HA — Failover Notification",
        "=" * 40,
        f"Severity  : {severity}",
        f"Event     : {etype}",
        f"Backend   : {backend}",
        f"Timestamp : {ts}",
    ]
    if detail:
        lines.append(f"Detail    : {detail}")
    if src_ip:
        lines.append(f"Source IP : {src_ip}")
    if sessions != "":
        lines.append(f"Sessions  : {sessions}")

    lines += [
        "",
        "Recommended action:",
        _action_for(etype, severity),
        "",
        "Dashboard : thirha.aegispub.com",
        "Runbook   : docs/THIR_HA_Runbooks_v2.docx",
    ]

    return subject, "\n".join(lines)


def _action_for(etype: str, severity: str) -> str:
    if "vm1_down" in etype or etype == "failover_active":
        return (
            "  VM1 (sensor) is offline. HAProxy is routing to VM2 standby Cowrie.\n"
            "  1. SSH to VM2 — verify standby Cowrie active: sudo systemctl status cowrie\n"
            "  2. SSH to VM1 — check Oracle console, restart or rebuild per RB-02\n"
            "  3. Once VM1 restored: verify HAProxy marks vm1 backend UP\n"
            "  Ref: RB-02, RB-04"
        )
    if "vm2_down" in etype:
        return (
            "  VM2 (brain/pipeline) is offline. Dashboard will go stale.\n"
            "  1. Check Oracle console for VM2 instance state\n"
            "  2. Rebuild VM2 per RB-03 (Cowrie on VM1 continues independently)\n"
            "  3. Update ORACLE_VPS_IP secret if VM2 public IP changed\n"
            "  Ref: RB-03"
        )
    if "up" in etype or etype == "failover_recovered":
        return (
            "  Node recovered. HAProxy is returning traffic to primary backend.\n"
            "  1. Monitor for 30 minutes — confirm stable UP state\n"
            "  2. Check data/failover_events.json for oscillation patterns\n"
            "  Ref: RB-04"
        )
    return "  Review data/failover_events.json and HAProxy stats. Ref: RB-04"


# ---------------------------------------------------------------------------
# Notification channels
# ---------------------------------------------------------------------------

def send_slack(webhook_url: str, subject: str, body: str, severity: str) -> bool:
    emoji = SEVERITY_EMOJI.get(severity, "⚪")
    payload = {
        "text": f"{emoji} *{subject}*",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*{subject}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"```{body}```"
                }
            }
        ]
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except urllib.error.URLError as e:
        print(f"[Tool 40] Slack send failed: {e}", file=sys.stderr)
        return False


def send_email(
    smtp_host: str,
    smtp_port: int,
    smtp_user: str,
    smtp_pass: str,
    from_addr: str,
    to_addr: str,
    subject: str,
    body: str,
) -> bool:
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"]    = from_addr
    msg["To"]      = to_addr
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=15) as s:
            s.login(smtp_user, smtp_pass)
            s.sendmail(from_addr, [to_addr], msg.as_string())
        return True
    except Exception as e:
        print(f"[Tool 40] Email send failed: {e}", file=sys.stderr)
        return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    # --- env
    channel       = os.environ.get("ALERT_CHANNEL",        "dry-run").lower()
    slack_url     = os.environ.get("SLACK_WEBHOOK_URL",     "")
    smtp_host     = os.environ.get("SMTP_HOST",             "")
    smtp_port     = int(os.environ.get("SMTP_PORT",         "465"))
    smtp_user     = os.environ.get("SMTP_USER",             "")
    smtp_pass     = os.environ.get("SMTP_PASS",             "")
    alert_from    = os.environ.get("ALERT_FROM_EMAIL",      "")
    alert_to      = os.environ.get("ALERT_TO_EMAIL",        "")

    # --- load inputs
    events = load_json_safe(FAILOVER_EVENTS, [])
    if not isinstance(events, list):
        print(f"[Tool 40] ERROR: {FAILOVER_EVENTS} must be a JSON array", file=sys.stderr)
        return 1

    history: dict = load_json_safe(ALERT_HISTORY, {})
    if not isinstance(history, dict):
        history = {}

    notifications_out = load_json_safe(OUTPUT_NOTIF, [])
    if not isinstance(notifications_out, list):
        notifications_out = []

    if not events:
        print(f"[Tool 40] {FAILOVER_EVENTS}: empty — no failover events to process")
        _write_empty_output(notifications_out)
        return 0

    print(f"[Tool 40] Processing {len(events)} failover event(s) | channel={channel}")

    sent_count  = 0
    dedup_count = 0
    error_count = 0

    for event in events:
        ehash    = event_hash(event)
        etype    = event.get("event_type", "unknown")
        severity = SEVERITY_MAP.get(etype, "MEDIUM")

        # skip INFO recoveries in dry-run so the log isn't floisy on stable systems
        # (but do send them on real channels — operators want the all-clear)
        if channel == "dry-run" and severity == "INFO":
            print(f"[Tool 40] DRY-RUN: INFO event suppressed: {etype} ({ehash})")
            continue

        # deduplication — keyed under "failover40_" namespace to avoid collision with Tool 37
        history_key = f"failover40_{ehash}"
        if history_key in history:
            dedup_count += 1
            continue

        subject, body = build_message(event, severity)

        # --- dispatch
        ok = True
        if channel == "dry-run":
            print(f"\n{'='*60}")
            print(f"[DRY-RUN] {subject}")
            print(f"{'='*60}")
            print(body)
            print()

        elif channel in ("slack", "both"):
            if not slack_url:
                print("[Tool 40] WARNING: ALERT_CHANNEL=slack but SLACK_WEBHOOK_URL not set",
                      file=sys.stderr)
                ok = False
            else:
                ok = send_slack(slack_url, subject, body, severity) and ok

        elif channel in ("email", "both"):
            if not all([smtp_host, smtp_user, smtp_pass, alert_from, alert_to]):
                print("[Tool 40] WARNING: ALERT_CHANNEL=email but SMTP_* vars incomplete",
                      file=sys.stderr)
                ok = False
            else:
                ok = send_email(
                    smtp_host, smtp_port, smtp_user, smtp_pass,
                    alert_from, alert_to, subject, body
                ) and ok

        if channel == "both":
            # second leg — email if slack was the first leg
            if slack_url:
                send_slack(slack_url, subject, body, severity)
            if all([smtp_host, smtp_user, smtp_pass, alert_from, alert_to]):
                send_email(
                    smtp_host, smtp_port, smtp_user, smtp_pass,
                    alert_from, alert_to, subject, body
                )

        if ok:
            # record in history so the next run doesn't re-notify
            history[history_key] = {
                "sent_at":    utcnow(),
                "event_type": etype,
                "severity":   severity,
                "backend":    event.get("backend", ""),
                "channel":    channel,
                "hash":       ehash,
            }
            sent_count += 1

            # record in our own output file
            notifications_out.append({
                "notified_at": utcnow(),
                "event_type":  etype,
                "severity":    severity,
                "backend":     event.get("backend", ""),
                "channel":     channel,
                "hash":        ehash,
                "event_ts":    event.get("timestamp", ""),
            })
        else:
            error_count += 1

    # --- persist
    save_json(ALERT_HISTORY, history)
    _write_empty_output(notifications_out)

    print(
        f"[Tool 40] Done — sent={sent_count} dedup={dedup_count} errors={error_count}"
    )
    return 0 if error_count == 0 else 2


def _write_empty_output(notifications_out) -> None:
    """Always write the output file so downstream tools don't fail on missing file."""
    save_json(OUTPUT_NOTIF, notifications_out)


if __name__ == "__main__":
    sys.exit(main())
