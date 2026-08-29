#!/usr/bin/env python3
"""
Tool 32 — THIR Report Lifecycle Manager

Handles the full tiered retention lifecycle for SOC reports:

  DAILY   → Written every pipeline run to reports/daily/
              Format: reports/daily/soc_YYYY-MM-DD.md
              Retention: 5–7 files (one per day, overwritten same-day)

  WEEKLY  → Triggered on Monday via pipeline.yml's sentinel (--rollup weekly)
              Reads all reports/daily/*.md from the past week
              Writes reports/weekly/soc_week_YYYY-WNN.md
              Deletes the daily files that were rolled up
              Retention: 3–4 files (one per week)

  MONTHLY → Triggered on 1st of month via pipeline.yml's sentinel
              (--rollup monthly) -- BUT only actually executes once the
              previous month's final ISO week has itself been rolled up
              by WEEKLY above (see _last_iso_week_rollup_ready()). If not
              yet eligible, exits with status 3 and the sentinel persists
              for automatic retry on the next run -- this is expected,
              not an error. Two real scheduling bugs this gate fixes:
              (1) when the 1st of a month lands on a Monday (~15% of
              months), both sentinels fire the same run -- pipeline.yml
              now runs weekly first, monthly second, so neither starves
              the other; (2) any month whose final days fall in an ISO
              week extending into the next month (true for December
              every year) would previously roll up before that week's
              data existed at all, silently producing a short month and
              orphaning that week's file.
              Reads all reports/weekly/soc_week_*.md whose Monday falls
              in the previous month
              Writes reports/monthly/soc_YYYY-MM.md
              Deletes the weekly files that were rolled up
              Retention: consumption-pruned by YEARLY below, not
              age-pruned (the original 6-month cap was an AWS
              credit-expiry workaround, removed post-Oracle-migration --
              no time limit applies now)

  YEARLY  → Triggered from the end of MONTHLY above, every run -- but
              only actually executes on April 1 UTC (fixed fiscal-year
              boundary, no jurisdiction-specific significance, just a
              consistent annual default). Rolls up whatever monthly
              reports fall in the fiscal year that just ended (previous
              April 1 → March 31), even if fewer than 12 exist --
              labeled honestly as an incomplete year rather than
              withheld or padded. Deletes the rolled-up monthly files.
              Retention: permanent (no tier above yearly; 12-month text
              aggregates are small enough that unbounded growth is not a
              realistic concern at any normal operating timescale)

OPTION 3 — Peak Stats:
  Every run (--save-daily) also reads stats.json and updates it with
  high-water marks: peak_sessions, peak_date, peak_unique_ips, peak_ip_date.
  These are NEVER overwritten by a quieter day — only updated if today beats
  the current peak.

Usage:
    # Every hourly pipeline run:
    python tools/32_report_lifecycle.py --save-daily \\
        --report data/soc_handover.md \\
        --stats  data/stats.json \\
        --date   2026-03-07

    # Monday — weekly rollup (fires via pipeline.yml's sentinel check,
    # no fixed hour -- see WEEKLY above):
    python tools/32_report_lifecycle.py --rollup weekly \\
        --stats data/stats.json

    # 1st of month — monthly rollup (fires via pipeline.yml's sentinel
    # check; self-defers with exit code 3 if not yet eligible, see
    # MONTHLY above):
    python tools/32_report_lifecycle.py --rollup monthly \\
        --stats data/stats.json

No external dependencies — stdlib only.
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, date, timezone, timedelta


# ─────────────────────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────────────────────

def log(msg, level="INFO", verbose=False):
    if level == "INFO" and not verbose:
        return
    prefix = {"INFO": "[INFO]", "WARN": "[WARN]", "ERROR": "[ERROR]"}.get(level, "[INFO]")
    sys.stderr.write(f"{prefix} {msg}\n")
    sys.stderr.flush()


# ─────────────────────────────────────────────────────────────────────────────
# Directory helpers
# ─────────────────────────────────────────────────────────────────────────────

REPORTS_DAILY   = "reports/daily"
REPORTS_WEEKLY  = "reports/weekly"
REPORTS_MONTHLY = "reports/monthly"
REPORTS_YEARLY  = "reports/yearly"

def ensure_dirs():
    for d in [REPORTS_DAILY, REPORTS_WEEKLY, REPORTS_MONTHLY]:
        os.makedirs(d, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# Option 3 — Peak stats update
# ─────────────────────────────────────────────────────────────────────────────

def update_peak_stats(stats_path, verbose=False):
    """
    Reads stats.json, compares today's session/IP counts against stored
    peak high-water marks. Updates only if today beats the current peak.
    Writes back to stats.json.
    """
    if not os.path.exists(stats_path):
        log(f"stats.json not found at {stats_path} — skipping peak update", "WARN", True)
        return

    try:
        with open(stats_path, encoding="utf-8") as f:
            stats = json.load(f)
    except Exception as e:
        log(f"Failed to read stats.json: {e}", "ERROR", True)
        return

    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    changed   = False

    # Peak sessions
    today_sessions = int(stats.get("total_attacks", 0))
    peak_sessions  = int(stats.get("peak_sessions", 0))
    if today_sessions > peak_sessions:
        log(f"New peak sessions: {today_sessions} (was {peak_sessions} on {stats.get('peak_date','never')})", "INFO", True)
        stats["peak_sessions"] = today_sessions
        stats["peak_date"]     = today
        changed = True

    # Peak unique IPs
    today_ips  = int(stats.get("unique_ips", 0))
    peak_ips   = int(stats.get("peak_unique_ips", 0))
    if today_ips > peak_ips:
        log(f"New peak unique IPs: {today_ips} (was {peak_ips} on {stats.get('peak_ip_date','never')})", "INFO", True)
        stats["peak_unique_ips"] = today_ips
        stats["peak_ip_date"]    = today
        changed = True

    # Peak confirmed threats
    today_threats = int(stats.get("confirmed_threats", 0))
    peak_threats  = int(stats.get("peak_confirmed_threats", 0))
    if today_threats > peak_threats:
        log(f"New peak confirmed threats: {today_threats}", "INFO", True)
        stats["peak_confirmed_threats"] = today_threats
        stats["peak_threats_date"]      = today
        changed = True

    if changed:
        try:
            with open(stats_path, "w", encoding="utf-8") as f:
                json.dump(stats, f, indent=2)
            log(f"Peak stats updated in {stats_path}", "INFO", verbose)
        except Exception as e:
            log(f"Failed to write stats.json: {e}", "ERROR", True)
    else:
        log("No new peaks today — stats.json unchanged", "INFO", verbose)


# ─────────────────────────────────────────────────────────────────────────────
# Daily save
# ─────────────────────────────────────────────────────────────────────────────

def save_daily(report_path, date_str, verbose=False):
    """
    Copies today's soc_handover.md into reports/daily/soc_YYYY-MM-DD.md.
    If same-day file already exists it is overwritten (latest run wins).
    """
    if not os.path.exists(report_path):
        log(f"Report not found at {report_path} — skipping daily save", "WARN", True)
        return

    dest = os.path.join(REPORTS_DAILY, f"soc_{date_str}.md")
    shutil.copy2(report_path, dest)
    log(f"Daily report saved → {dest}", "INFO", verbose)


# ─────────────────────────────────────────────────────────────────────────────
# Extract key metrics from a daily Markdown report
# ─────────────────────────────────────────────────────────────────────────────

def _extract_metric(text, label):
    """Pull a bold number from a Markdown table row like '| Total Sessions | **40** |'"""
    pattern = rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|\s*\*\*(\d+)\*\*"
    m = re.search(pattern, text)
    if m:
        return int(m.group(1))
    # fallback: label not bold
    pattern2 = rf"\|\s*{re.escape(label)}\s*\|\s*\*\*(\d+)\*\*"
    m2 = re.search(pattern2, text)
    return int(m2.group(1)) if m2 else 0


def parse_daily_report(path):
    """Return a dict of key metrics extracted from a daily .md report."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return {}

    date_m = re.search(r"soc_(\d{4}-\d{2}-\d{2})\.md", path)
    date_s = date_m.group(1) if date_m else "unknown"

    return {
        "date":               date_s,
        "total_sessions":     _extract_metric(text, "Total Sessions Captured"),
        "confirmed_threats":  _extract_metric(text, "Confirmed Threats"),
        "false_positives":    _extract_metric(text, "False Positives Filtered"),
        "unique_ips":         _extract_metric(text, "Unique Attacker IPs (cumulative)") or
                              _extract_metric(text, "Unique Attacker IPs"),
        "countries":          _extract_metric(text, "Countries of Origin"),
        "high_sev":           _extract_metric(text, "High Severity Cases"),
        "medium_sev":         _extract_metric(text, "Medium Severity Cases"),
        "low_sev":            _extract_metric(text, "Low Severity Cases"),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Weekly rollup
# ─────────────────────────────────────────────────────────────────────────────

def rollup_weekly(verbose=False, week_label_override=None):
    """
    Runs on Monday. Reads all daily reports from the past 7 days,
    produces a weekly summary Markdown, deletes the rolled-up daily files.

    week_label_override: optional string like '2026-W11'. When set, the date
    window and output filename are derived from that ISO week rather than
    calculated from today. Use this for manual backfill when the automatic
    Monday trigger was missed.

    Bug fixed (2026-03-19): Previously returned silently with no output file
    when zero daily reports were found in the window. This caused the weekly
    slot to remain permanently empty — no retry is possible once the window
    passes, and the already-exists guard prevents re-runs even for stubs.
    Now writes a stub report in all cases so the slot is always filled and
    downstream monthly rollup has a consistent file to consume.
    """
    if week_label_override:
        # Parse YYYY-WNN into explicit date window (Mon–Sun of that ISO week)
        try:
            m = re.match(r"^(\d{4})-W(\d{2})$", week_label_override)
            if not m:
                raise ValueError(f"Invalid week label format: {week_label_override!r}. Expected YYYY-WNN e.g. 2026-W11")
            yr, wk = int(m.group(1)), int(m.group(2))
            prev_monday = datetime.fromisocalendar(yr, wk, 1).date()   # Monday of target week
            today       = prev_monday + timedelta(days=7)               # following Monday (exclusive end)
            week_ago    = prev_monday                                    # inclusive start
            week_label  = week_label_override
        except Exception as e:
            log(f"--week-label error: {e}", "ERROR", True)
            return
    else:
        today = datetime.now(timezone.utc).date()

        # Fix: derive previous week using proper ISO week boundaries (Mon–Sun).
        # Previously used today-7 which shifted the window 1 day forward:
        # e.g. on Mon Mar-24, old code gave Mar17–Mar23 instead of Mar16–Mar22.
        year, week, _ = today.isocalendar()           # current ISO week
        prev_week = week - 1
        prev_year = year
        if prev_week == 0:                            # handle Jan year-boundary
            prev_year -= 1
            prev_week = datetime(prev_year, 12, 28).isocalendar()[1]

        prev_monday = datetime.fromisocalendar(prev_year, prev_week, 1).date()
        prev_sunday = prev_monday + timedelta(days=6)
        week_ago    = prev_monday                     # inclusive start (Monday)
        today       = prev_sunday + timedelta(days=1) # exclusive end (following Monday)
        week_label  = f"{prev_year}-W{prev_week:02d}"

        log(f"Weekly rollup — label: {week_label}", "INFO", True)
        log(f"Weekly rollup — window: {week_ago} → {prev_sunday} (inclusive)", "INFO", True)

    dest = os.path.join(REPORTS_WEEKLY, f"soc_week_{week_label}.md")

    if os.path.exists(dest):
        log(f"Weekly report {dest} already exists — skipping", "WARN", True)
        return

    # Collect daily files from the past 7 days
    daily_files = []
    for fname in sorted(os.listdir(REPORTS_DAILY)):
        m = re.match(r"soc_(\d{4}-\d{2}-\d{2})\.md$", fname)
        if not m:
            continue
        try:
            fdate = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if week_ago <= fdate < today:
            daily_files.append(os.path.join(REPORTS_DAILY, fname))

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not daily_files:
        # Write a stub so the slot is filled — silent skip would leave a permanent gap
        log(f"No daily reports found for week {week_label} — writing empty stub to {dest}", "WARN", True)
        lines = []
        def ln(s=""): lines.append(s)
        ln(f"# 🛡 THIR · SOC Weekly Summary — {week_label}")
        ln()
        ln("| Field | Value |")
        ln("|---|---|")
        ln(f"| **Week** | {week_label} ({prev_monday} → {today - timedelta(days=1)}) |")
        ln(f"| **Generated At** | {now_str} |")
        ln(f"| **Days Covered** | 0 |")
        ln(f"| **Source** | No daily reports found in window {week_ago} → {today - timedelta(days=1)} |")
        ln()
        ln("> ⚠️ **No daily SOC reports were available for this week.**")
        ln("> This stub was written automatically to preserve the weekly archive slot.")
        ln("> Possible causes: pipeline failures during the week, or daily save step errors.")
        ln()
        ln("---")
        ln()
        ln(f"_Generated by THIR · Tool 32 · Report Lifecycle Manager_  ")
        ln(f"_Stub — zero daily reports found · Week {week_label}_  ")
        ln(f"_Generated: {now_str}_")
        ln()
        try:
            with open(dest, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            log(f"Empty stub written → {dest}", "WARN", True)
        except Exception as e:
            log(f"Failed to write stub weekly report: {e}", "ERROR", True)
        return

    # Check for missing days and warn (does not block rollup)
    expected_dates = {week_ago + timedelta(days=i) for i in range(7)}
    found_dates = set()
    for fpath in daily_files:
        m = re.search(r"soc_(\d{4}-\d{2}-\d{2})\.md$", fpath)
        if m:
            try:
                found_dates.add(datetime.strptime(m.group(1), "%Y-%m-%d").date())
            except ValueError:
                pass
    missing_dates = sorted(expected_dates - found_dates)
    if missing_dates:
        log(f"Weekly rollup {week_label}: {len(missing_dates)} day(s) missing from window "
            f"({', '.join(str(d) for d in missing_dates)}) — rollup proceeds with {len(daily_files)} day(s)",
            "WARN", True)

    log(f"Rolling up {len(daily_files)} daily reports → {dest}", "INFO", verbose)

    # Parse each daily report
    days = [parse_daily_report(f) for f in daily_files]
    days = [d for d in days if d]

    # Aggregate
    total_sessions    = sum(d["total_sessions"]    for d in days)
    total_threats     = sum(d["confirmed_threats"] for d in days)
    total_fps         = sum(d["false_positives"]   for d in days)
    total_ips         = sum(d["unique_ips"]        for d in days)
    peak_day          = max(days, key=lambda d: d["total_sessions"]) if days else {}
    peak_sessions     = peak_day.get("total_sessions", 0)
    peak_date         = peak_day.get("date", "—")
    high_total        = sum(d["high_sev"]   for d in days)
    med_total         = sum(d["medium_sev"] for d in days)
    low_total         = sum(d["low_sev"]    for d in days)

    lines = []
    def ln(s=""): lines.append(s)

    ln(f"# 🛡 THIR · SOC Weekly Summary — {week_label}")
    ln()
    ln("| Field | Value |")
    ln("|---|---|")
    ln(f"| **Week** | {week_label} ({prev_monday} → {today - timedelta(days=1)}) |")
    ln(f"| **Generated At** | {now_str} |")
    ln(f"| **Days Covered** | {len(days)} of 7 |")
    ln(f"| **Source** | Rolled up from {len(daily_files)} daily SOC reports |")
    if missing_dates:
        ln(f"| **Missing Days** | {', '.join(str(d) for d in missing_dates)} — no daily report saved |")
    ln()
    ln("---")
    ln()
    ln("## 📊 Weekly Aggregate Metrics")
    ln()
    ln("| Metric | Total |")
    ln("|---|---|")
    ln(f"| Total Sessions Captured | **{total_sessions}** |")
    ln(f"| Confirmed Threats | **{total_threats}** |")
    ln(f"| False Positives Filtered | **{total_fps}** |")
    ln(f"| Unique Attacker IPs (cumulative) | **{total_ips}** |")
    ln(f"| High Severity Cases | **{high_total}** |")
    ln(f"| Medium Severity Cases | **{med_total}** |")
    ln(f"| Low Severity Cases | **{low_total}** |")
    ln(f"| Peak Activity Day | **{peak_date}** ({peak_sessions} sessions) |")
    ln()
    ln("---")
    ln()
    ln("## 📅 Daily Breakdown")
    ln()
    ln("| Date | Sessions | Threats | FPs | High | Med | Low |")
    ln("|---|---|---|---|---|---|---|")
    for d in sorted(days, key=lambda x: x["date"]):
        ln(f"| {d['date']} | {d['total_sessions']} | {d['confirmed_threats']} | "
           f"{d['false_positives']} | {d['high_sev']} | {d['medium_sev']} | {d['low_sev']} |")
    ln()
    ln("---")
    ln()
    ln("## 📋 Analyst Notes")
    ln()
    ln("> _Add shift notes, escalations, or notable incidents here before archiving._")
    ln()
    ln("---")
    ln()
    ln(f"_Generated by THIR · Tool 32 · Report Lifecycle Manager_  ")
    ln(f"_Rolled up from {len(daily_files)} daily reports · Week {week_label}_  ")
    ln(f"_Generated: {now_str}_")
    ln()

    try:
        with open(dest, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        log(f"Weekly report written → {dest}", "INFO", verbose)
    except Exception as e:
        log(f"Failed to write weekly report: {e}", "ERROR", True)
        return

    # Delete rolled-up daily files
    for fpath in daily_files:
        try:
            os.remove(fpath)
            log(f"Deleted daily report: {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not delete {fpath}: {e}", "WARN", True)

    log(f"Weekly rollup complete — {len(daily_files)} daily reports → {dest}", "INFO", True)


# ─────────────────────────────────────────────────────────────────────────────
# Monthly rollup
# ─────────────────────────────────────────────────────────────────────────────

def _last_iso_week_rollup_ready(year, month, today):
    """
    Returns True if the ISO week containing the LAST DAY of (year, month)
    has already had its own weekly rollup run -- i.e. today is on or
    after the Monday FOLLOWING that week's Monday.

    Fixes a real, structural bug found 2026-08: rollup_monthly() used to
    fire unconditionally on the 1st of the month, with no check for
    whether the previous month's final ISO week had actually been rolled
    up yet by rollup_weekly() (which only processes a week the Monday
    AFTER it ends). For any month whose last few days fall in an ISO
    week that extends into the following month (true for December every
    year, and periodically for other months depending on where month
    boundaries land relative to Monday), the monthly rollup would fire
    before that final week's data existed on disk at all -- silently
    producing a short month and leaving that week's file to become an
    orphan once rollup_weekly() finally wrote it days later. This is the
    most likely root cause of the orphaned weekly files (W18, W22, W27,
    W31) found in an earlier review of this repo's report inventory.

    A second, independent consequence of the same missing gate: when the
    1st of a month lands ON a Monday (happens ~15% of months, e.g.
    2026-06-01), pipeline.yml's sentinel logic gives monthly rollup
    priority over weekly in the SAME run -- meaning that week's OWN
    rollup gets deferred by a cycle, and if that week also happens to be
    the previous month's final week, monthly would again run before its
    own prerequisite data exists. This gate makes rollup_monthly() safe
    against both cases: it simply declines to run (and lets the sentinel
    persist for automatic retry, exactly like a failure would) until its
    actual prerequisite -- the final week's weekly rollup -- has
    genuinely completed.
    """
    if month == 12:
        last_day = date(year, 12, 31)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)

    iso_year, iso_week, _ = last_day.isocalendar()
    week_monday = date.fromisocalendar(iso_year, iso_week, 1)
    eligible_from = week_monday + timedelta(days=7)  # that week's own rollup Monday

    return today >= eligible_from


def rollup_monthly(verbose=False):
    """
    Runs on 1st of month -- but only actually executes once the previous
    month's final ISO week has itself been rolled up by rollup_weekly().
    See _last_iso_week_rollup_ready() for why this gate exists. If not
    yet eligible, this function logs why and returns without writing
    anything or deleting anything -- pipeline.yml's sentinel persists
    (data/.rollup_monthly_pending is only cleared on success), so the
    next scheduled run retries automatically, same retry-on-failure
    behaviour the sentinel already provides for genuine errors.

    Reads all weekly reports from the previous month, produces a monthly
    summary Markdown, deletes the rolled-up weekly files.

    Retention: monthly reports are consumption-pruned by rollup_yearly(),
    NOT age-pruned. The original 6-month age-based prune (_prune_old_monthlies,
    kept below but no longer called) was an AWS free-tier credit-expiry
    workaround with no equivalent constraint on Oracle Cloud's Always Free
    tier. In its place: on April 1 each year (fixed fiscal-year boundary,
    no special significance beyond consistency), all monthly reports
    falling in the fiscal year that just ended are rolled into one yearly
    report and deleted -- same consumption-based pattern already used at
    every other tier (daily→weekly→monthly), extended one level up rather
    than replaced with either "delete after N months" or "keep forever".
    """
    today       = datetime.now(timezone.utc).date()
    # Previous month
    first_this  = today.replace(day=1)
    last_month  = first_this - timedelta(days=1)
    month_label = last_month.strftime("%Y-%m")
    month_start = last_month.replace(day=1)

    if not _last_iso_week_rollup_ready(last_month.year, last_month.month, today):
        log(f"Monthly rollup for {month_label}: previous month's final ISO week "
            f"has not been rolled up yet — deferring (sentinel persists for retry)",
            "INFO", True)
        return "deferred"

    dest = os.path.join(REPORTS_MONTHLY, f"soc_{month_label}.md")

    if os.path.exists(dest):
        log(f"Monthly report {dest} already exists — skipping", "WARN", True)
        return "already_exists"

    # Collect weekly files that fall within the previous month
    weekly_files = []
    for fname in sorted(os.listdir(REPORTS_WEEKLY)):
        m = re.match(r"soc_week_(\d{4})-W(\d{2})\.md$", fname)
        if not m:
            continue
        year_w, week_n = int(m.group(1)), int(m.group(2))
        try:
            # Get the Monday of that ISO week
            week_monday = datetime.fromisocalendar(year_w, week_n, 1).date()
        except Exception:
            continue
        # Include if the week's Monday falls inside the previous month
        if month_start <= week_monday < first_this:
            weekly_files.append(os.path.join(REPORTS_WEEKLY, fname))

    if not weekly_files:
        log("No weekly reports found for monthly rollup — nothing to do", "WARN", True)
        return "no_data"

    log(f"Rolling up {len(weekly_files)} weekly reports → {dest}", "INFO", verbose)

    # Parse each weekly report — reuse parse_daily_report (same table format)
    weeks = [parse_daily_report(f) for f in weekly_files]
    weeks_data = []
    for fpath, parsed in zip(weekly_files, weeks):
        # Weekly files have week label in filename, not date — patch it
        wm = re.search(r"soc_week_(\d{4}-W\d{2})\.md$", fpath)
        parsed["date"] = wm.group(1) if wm else parsed.get("date", "?")
        if parsed:
            weeks_data.append(parsed)

    total_sessions   = sum(d["total_sessions"]    for d in weeks_data)
    total_threats    = sum(d["confirmed_threats"] for d in weeks_data)
    total_fps        = sum(d["false_positives"]   for d in weeks_data)
    total_ips        = sum(d["unique_ips"]        for d in weeks_data)
    high_total       = sum(d["high_sev"]          for d in weeks_data)
    med_total        = sum(d["medium_sev"]        for d in weeks_data)
    low_total        = sum(d["low_sev"]           for d in weeks_data)
    peak_week        = max(weeks_data, key=lambda d: d["total_sessions"]) if weeks_data else {}
    peak_sessions    = peak_week.get("total_sessions", 0)
    peak_week_label  = peak_week.get("date", "—")

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    def ln(s=""): lines.append(s)

    ln(f"# 🛡 THIR · SOC Monthly Summary — {month_label}")
    ln()
    ln("| Field | Value |")
    ln("|---|---|")
    ln(f"| **Month** | {month_label} ({month_start} → {last_month}) |")
    ln(f"| **Generated At** | {now_str} |")
    ln(f"| **Weeks Covered** | {len(weeks_data)} |")
    ln(f"| **Source** | Rolled up from {len(weekly_files)} weekly SOC reports |")
    ln()
    ln("---")
    ln()
    ln("## 📊 Monthly Aggregate Metrics")
    ln()
    ln("| Metric | Total |")
    ln("|---|---|")
    ln(f"| Total Sessions Captured | **{total_sessions}** |")
    ln(f"| Confirmed Threats | **{total_threats}** |")
    ln(f"| False Positives Filtered | **{total_fps}** |")
    ln(f"| Unique Attacker IPs (cumulative) | **{total_ips}** |")
    ln(f"| High Severity Cases | **{high_total}** |")
    ln(f"| Medium Severity Cases | **{med_total}** |")
    ln(f"| Low Severity Cases | **{low_total}** |")
    ln(f"| Peak Activity Week | **{peak_week_label}** ({peak_sessions} sessions) |")
    ln()
    ln("---")
    ln()
    ln("## 📅 Weekly Breakdown")
    ln()
    ln("| Week | Sessions | Threats | FPs | High | Med | Low |")
    ln("|---|---|---|---|---|---|---|")
    for d in weeks_data:
        ln(f"| {d['date']} | {d['total_sessions']} | {d['confirmed_threats']} | "
           f"{d['false_positives']} | {d['high_sev']} | {d['medium_sev']} | {d['low_sev']} |")
    ln()
    ln("---")
    ln()
    ln("## 📋 Monthly Analyst Notes")
    ln()
    ln("> _Trends, escalations, notable threat actor patterns, or infrastructure changes this month._")
    ln()
    ln("---")
    ln()
    ln(f"_Generated by THIR · Tool 32 · Report Lifecycle Manager_  ")
    ln(f"_Rolled up from {len(weekly_files)} weekly reports · Month {month_label}_  ")
    ln(f"_Generated: {now_str}_")
    ln()

    try:
        with open(dest, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        log(f"Monthly report written → {dest}", "INFO", verbose)
    except Exception as e:
        log(f"Failed to write monthly report: {e}", "ERROR", True)
        return "write_failed"

    # Delete rolled-up weekly files
    for fpath in weekly_files:
        try:
            os.remove(fpath)
            log(f"Deleted weekly report: {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not delete {fpath}: {e}", "WARN", True)

    # Fiscal-year (April-March) yearly rollup -- checked every monthly run;
    # only actually fires when today is April 1 UTC. This replaces the old
    # age-based 6-month prune (see docstring above and
    # _prune_old_monthlies()'s own docstring for why that was removed).
    # April-March is a fixed default with no special significance beyond
    # being a predictable, consistent annual boundary -- not tied to any
    # particular jurisdiction's actual fiscal calendar. See
    # rollup_yearly()'s own docstring for gap-tolerance behaviour: THIR's
    # first fiscal year (2025-04 to 2026-03) will only have ONE real month
    # of data (2026-03, THIR's actual go-live) when it closes on 2026-04-01,
    # and that is rolled up and labeled as incomplete rather than withheld.
    rollup_yearly(verbose=verbose)

    log(f"Monthly rollup complete — {len(weekly_files)} weekly reports → {dest}", "INFO", True)
    return "success"


# ─────────────────────────────────────────────────────────────────────────────
# Yearly rollup — consumption-based, triggered by FIXED FISCAL CALENDAR
# (April 1), not monthly report count. Runs automatically at the end of
# rollup_monthly() above; only actually produces a report on April 1 UTC.
# No separate cron/sentinel needed -- monthly already runs every 1st of
# month, so checking today's date there is sufficient.
# ─────────────────────────────────────────────────────────────────────────────

def rollup_yearly(verbose=False):
    """
    Fiscal-year (April-March) consumption-based yearly rollup. Triggered
    from rollup_monthly() every run; only actually produces a report when
    today is April 1 UTC AND at least one monthly report exists for the
    fiscal year that just ended (previous April 1 -> March 31).

    Fixed April-March was chosen as the default with no special
    significance attached beyond "a fixed, predictable annual boundary" --
    not tied to any particular jurisdiction's actual fiscal calendar.

    Gap tolerance: does NOT require all 12 months to be present before
    rolling up. THIR's first fiscal year (2025-04 to 2026-03) only has
    ONE real month of data (2026-03 -- THIR's actual go-live), and the
    weekly rollup gap investigation (docs/enriched_corpus_build_plan.md
    era session) already found genuine missing months elsewhere in this
    system's history. Requiring a full 12 before rolling up would mean
    that FY's data either never gets archived or sits in reports/monthly/
    indefinitely waiting for months that will never exist. Instead, this
    rolls up whatever months from that FY window ARE present the same
    way rollup_monthly() already tolerates 2-5 weekly reports instead of
    requiring exactly 4-5 -- and the resulting report's "Months Covered"
    field states the true count (which may be less than 12) rather than
    implying a complete year.
    """
    today = datetime.now(timezone.utc).date()

    if today.month != 4 or today.day != 1:
        log(f"Yearly rollup: today ({today}) is not April 1 UTC — not due", "INFO", verbose)
        return

    # Fiscal year that just ended: previous April 1 -> March 31 (today)
    fy_end_year   = today.year - 1
    fy_start      = date(fy_end_year, 4, 1)
    fy_end        = date(fy_end_year + 1, 3, 31)
    fy_label      = f"FY{fy_start.year}-{str(fy_end.year)[2:]}"   # e.g. "FY2026-27"

    dest = os.path.join(REPORTS_YEARLY, f"soc_{fy_label}.md")

    if os.path.exists(dest):
        log(f"Yearly report {dest} already exists — skipping", "WARN", True)
        return

    # Select monthly reports whose month falls inside the fiscal window,
    # same "parse filename, check date range" pattern rollup_monthly()
    # already uses for its own weekly-file selection.
    all_monthly = sorted([
        f for f in os.listdir(REPORTS_MONTHLY)
        if re.match(r"soc_\d{4}-\d{2}\.md$", f)
    ])
    to_consume = []
    for fname in all_monthly:
        m = re.match(r"soc_(\d{4})-(\d{2})\.md$", fname)
        month_date = date(int(m.group(1)), int(m.group(2)), 1)
        if fy_start <= month_date <= fy_end:
            to_consume.append(fname)

    if not to_consume:
        log(f"Yearly rollup: no monthly reports found for {fy_label} "
            f"({fy_start} to {fy_end}) — nothing to do", "WARN", True)
        return

    months_present = len(to_consume)
    if months_present < 12:
        log(f"Yearly rollup: {fy_label} has only {months_present}/12 possible "
            f"monthly reports — rolling up what exists rather than waiting "
            f"(see docstring: gap tolerance is intentional)", "INFO", True)

    os.makedirs(REPORTS_YEARLY, exist_ok=True)

    log(f"Rolling up {len(to_consume)} monthly reports → {dest}", "INFO", verbose)

    months_data = []
    for fname in to_consume:
        fpath = os.path.join(REPORTS_MONTHLY, fname)
        parsed = _parse_monthly_report(fpath)
        month_label = re.match(r"soc_(\d{4}-\d{2})\.md$", fname).group(1)
        parsed["date"] = month_label
        months_data.append(parsed)

    total_sessions = sum(d["total_sessions"]    for d in months_data)
    total_threats  = sum(d["confirmed_threats"] for d in months_data)
    total_fps      = sum(d["false_positives"]   for d in months_data)
    total_ips      = sum(d["unique_ips"]        for d in months_data)
    high_total     = sum(d["high_sev"]          for d in months_data)
    med_total      = sum(d["medium_sev"]        for d in months_data)
    low_total      = sum(d["low_sev"]           for d in months_data)
    peak_month     = max(months_data, key=lambda d: d["total_sessions"]) if months_data else {}
    peak_sessions  = peak_month.get("total_sessions", 0)
    peak_month_label = peak_month.get("date", "—")

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    def ln(s=""): lines.append(s)

    ln(f"# 🛡 THIR · SOC Yearly Summary — {fy_label}")
    ln()
    ln("| Field | Value |")
    ln("|---|---|")
    ln(f"| **Fiscal Year** | {fy_label} ({fy_start} → {fy_end}) |")
    ln(f"| **Generated At** | {now_str} |")
    ln(f"| **Months Covered** | {len(months_data)} of 12 possible"
       f"{' — incomplete year, see note below' if months_present < 12 else ''} |")
    ln(f"| **Source** | Rolled up from {len(to_consume)} monthly SOC reports |")
    ln()
    ln("---")
    ln()
    ln("## 📊 Yearly Aggregate Metrics")
    ln()
    ln("| Metric | Total |")
    ln("|---|---|")
    ln(f"| Total Sessions Captured | **{total_sessions}** |")
    ln(f"| Confirmed Threats | **{total_threats}** |")
    ln(f"| False Positives Filtered | **{total_fps}** |")
    ln(f"| Unique Attacker IPs (cumulative) | **{total_ips}** |")
    ln(f"| High Severity Cases | **{high_total}** |")
    ln(f"| Medium Severity Cases | **{med_total}** |")
    ln(f"| Low Severity Cases | **{low_total}** |")
    ln(f"| Peak Activity Month | **{peak_month_label}** ({peak_sessions} sessions) |")
    ln()
    ln("---")
    ln()
    ln("## 📅 Monthly Breakdown")
    ln()
    ln("| Month | Sessions | Threats | FPs | High | Med | Low |")
    ln("|---|---|---|---|---|---|---|")
    for d in months_data:
        ln(f"| {d['date']} | {d['total_sessions']} | {d['confirmed_threats']} | "
           f"{d['false_positives']} | {d['high_sev']} | {d['medium_sev']} | {d['low_sev']} |")
    ln()
    ln("---")
    ln()
    ln("## 📋 Yearly Analyst Notes")
    ln()
    if months_present < 12:
        missing = 12 - months_present
        present_months = {d['date'] for d in months_data}
        expected_months = set()
        cursor = fy_start
        while cursor <= fy_end:
            expected_months.add(cursor.strftime("%Y-%m"))
            cursor = date(cursor.year + (1 if cursor.month == 12 else 0),
                           1 if cursor.month == 12 else cursor.month + 1, 1)
        missing_months = sorted(expected_months - present_months)
        ln(f"> ⚠️ **Incomplete fiscal year** — {months_present} of 12 possible months "
           f"present. Missing: {', '.join(missing_months)}. Aggregate totals above "
           f"reflect only the months actually rolled up, not a full {fy_label}.")
        ln(">")
    ln("> _Major campaigns, infrastructure changes, or year-over-year trend notes._")
    ln()
    ln("---")
    ln()
    ln(f"_Generated by THIR · Tool 32 · Report Lifecycle Manager_  ")
    ln(f"_Rolled up from {len(to_consume)} monthly reports · {fy_label} ({fy_start} to {fy_end})_  ")
    ln(f"_Generated: {now_str}_")
    ln()

    try:
        with open(dest, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        log(f"Yearly report written → {dest}", "INFO", verbose)
    except Exception as e:
        log(f"Failed to write yearly report: {e}", "ERROR", True)
        return

    # Delete rolled-up monthly files -- consumption-based, same as every
    # other tier. Nothing is retained past this point except the yearly
    # summary itself; yearly reports are never pruned (no further tier
    # above them, and 12-month aggregates are small text files -- the
    # unbounded-growth concern that applies to the corpus vaults doesn't
    # apply here at any realistic multi-decade timescale).
    for fname in to_consume:
        fpath = os.path.join(REPORTS_MONTHLY, fname)
        try:
            os.remove(fpath)
            log(f"Deleted monthly report: {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not delete {fpath}: {e}", "WARN", True)

    log(f"Yearly rollup complete — {len(to_consume)} monthly reports → {dest}", "INFO", True)


def _parse_monthly_report(path):
    """
    Extract aggregate metrics from a monthly report for yearly rollup.
    Monthly reports use a different table structure than daily/weekly
    (parse_daily_report expects the daily/weekly shape) -- this reads
    the "Monthly Aggregate Metrics" table instead.
    """
    defaults = {
        "total_sessions": 0, "confirmed_threats": 0, "false_positives": 0,
        "unique_ips": 0, "high_sev": 0, "medium_sev": 0, "low_sev": 0,
    }
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        log(f"Could not read {path} for yearly rollup: {e}", "WARN", True)
        return defaults

    patterns = {
        "total_sessions":    r"Total Sessions Captured \| \*\*(\d+)\*\*",
        "confirmed_threats": r"Confirmed Threats \| \*\*(\d+)\*\*",
        "false_positives":   r"False Positives Filtered \| \*\*(\d+)\*\*",
        "unique_ips":        r"Unique Attacker IPs \(cumulative\) \| \*\*(\d+)\*\*",
        "high_sev":          r"High Severity Cases \| \*\*(\d+)\*\*",
        "medium_sev":        r"Medium Severity Cases \| \*\*(\d+)\*\*",
        "low_sev":           r"Low Severity Cases \| \*\*(\d+)\*\*",
    }
    result = dict(defaults)
    for key, pattern in patterns.items():
        m = re.search(pattern, content)
        if m:
            result[key] = int(m.group(1))
    return result


def _prune_old_monthlies(keep=6, verbose=False):
    """
    Delete monthly reports beyond `keep` months, oldest first, with no
    yearly summary produced -- data is simply discarded.

    NOT CALLED as of 2026-08. Superseded by rollup_yearly(), which
    consumption-prunes monthly reports the same way weekly reports
    consumption-prune daily reports -- rolling the oldest 12 into a
    permanent yearly summary rather than deleting them outright. This
    function's original role (an AWS free-tier credit-expiry workaround,
    since removed -- Oracle's Always Free tier has no equivalent time
    limit) is now fully replaced, not just disabled: rollup_yearly()
    achieves genuine bounded reports/monthly/ growth (the same operational
    goal this function served) WITHOUT the destructive data loss this
    function's outright deletion caused. Kept in the file only as a
    reference implementation of pure age-based deletion, in case a future
    maintainer specifically wants that (not recommended -- prefer
    extending rollup_yearly()'s consumption pattern instead).
    """
    monthly_files = sorted([
        f for f in os.listdir(REPORTS_MONTHLY)
        if re.match(r"soc_\d{4}-\d{2}\.md$", f)
    ])
    if len(monthly_files) <= keep:
        return
    to_delete = monthly_files[:len(monthly_files) - keep]
    for fname in to_delete:
        fpath = os.path.join(REPORTS_MONTHLY, fname)
        try:
            os.remove(fpath)
            log(f"Pruned old monthly report (>{keep} months): {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not prune {fpath}: {e}", "WARN", True)


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tool 32 — THIR Report Lifecycle Manager"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--save-daily",
        action="store_true",
        help="Copy today's report to reports/daily/ and update peak stats"
    )
    group.add_argument(
        "--rollup",
        choices=["weekly", "monthly"],
        help="Trigger weekly or monthly rollup and cleanup"
    )

    parser.add_argument("--report",  default="data/soc_handover.md",
                        help="Path to today's SOC handover report (used with --save-daily)")
    parser.add_argument("--stats",   default="data/stats.json",
                        help="Path to stats.json for peak stats update")
    parser.add_argument("--date",    default=None,
                        help="Override date for daily save (YYYY-MM-DD). Defaults to today UTC.")
    parser.add_argument("--week-label", default=None, dest="week_label",
                        help="Override ISO week for weekly rollup, e.g. 2026-W11. "
                             "Use to manually backfill a missed Monday rollup. "
                             "Derives the date window from that week's Mon–Sun range.")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    ensure_dirs()

    if args.save_daily:
        date_str = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log(f"Mode: save-daily for {date_str}", "INFO", True)
        update_peak_stats(args.stats, verbose=args.verbose)
        save_daily(args.report, date_str, verbose=args.verbose)

    elif args.rollup == "weekly":
        log("Mode: weekly rollup", "INFO", True)
        rollup_weekly(verbose=args.verbose, week_label_override=args.week_label)

    elif args.rollup == "monthly":
        log("Mode: monthly rollup", "INFO", True)
        status = rollup_monthly(verbose=args.verbose)
        # "deferred" is a real, expected outcome (the previous month's
        # final ISO week hasn't been rolled up yet -- see
        # _last_iso_week_rollup_ready()'s docstring), NOT a failure. It
        # must still exit non-zero so pipeline.yml's sentinel logic
        # correctly treats it as "not done yet, retry next run" rather
        # than clearing the sentinel and silently never trying again
        # this month. "already_exists" and "no_data" are also non-error
        # terminal states -- exit 0 is correct for those, since retrying
        # them would not change the outcome.
        if status == "deferred":
            log("Monthly rollup deferred -- exiting non-zero so the sentinel "
                "persists for automatic retry next run", "INFO", True)
            sys.exit(3)
        elif status == "write_failed":
            sys.exit(1)
        # status in ("success", "already_exists", "no_data") -> exit 0

    log("Tool 32 completed", "INFO", True)


if __name__ == "__main__":
    main()
