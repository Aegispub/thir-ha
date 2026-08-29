#!/usr/bin/env python3
"""
Tool 43 — Enriched Corpus Builder (Actor Corpus)
==================================================
Reads: data/ir_cases.json, data/threat_ips.json
Writes: data/enriched_corpus.json (the vault — full IP records, permanent)
        enriched-data/enriched_highlights.json (counts/labels only, no raw IPs)
        enriched-data/enriched_metadata.json (run metadata)

Design contract: see enriched_corpus_schema_reconciliation.md.
Field mapping notes (deviations from the original design doc, confirmed
against real repo data 2026-08-21):

  - login_success_count : derived by summing login_success booleans across
    all ir_cases for the IP. NOT a field that exists in ir_cases.json.
  - commands_observed    : derived as len(case['commands']) > 0.
  - malware_downloaded   : derived as len(case['downloads']) > 0.
  - ttps_observed        : union of case['ttps'] (flat list of TTP ID
    strings) across all cases for the IP, accumulated cross-run.
  - first_seen/last_seen : min/max of case-level first_seen/last_seen,
    accumulated cross-run (existing corpus value is never widened
    backwards, only extended).
  - session_count        : count of DISTINCT case_id ever seen for this IP,
    accumulated cross-run via a persisted set of seen case_ids per IP.
  - enriched_at/enrichment_ttl_days : new fields, drive the cache-skip
    logic that avoids re-hitting AbuseIPDB/OTX for IPs already enriched
    within the TTL window. This is also the Tool 27 rate-limit fix.

This tool does NOT call AbuseIPDB/OTX directly — it reads threat_ips.json,
which Tool 27 already produces. The TTL/cache-skip logic here operates on
the corpus's own enriched_at bookkeeping and is the reference
implementation to later merge into 27_threat_intel_feeder_live.go itself,
so Tool 27 stops re-enriching IPs unnecessarily at the source.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Shared R2 archival helper -- same rclone remote/bucket as
# historical_processor.yml's Oracle corpus upload, parameterised per-corpus.
# Only invoked when --archive-to-r2 is passed (monthly step), not on the
# normal every-2h run.
sys.path.insert(0, str(Path(__file__).parent))
from r2_archive_helper import archive_corpus_to_r2, R2UploadError

TTL_DAYS_DEFAULT = 30
TTL_DAYS_CRITICAL = 7
CRITICAL_ABUSE_SCORE = 80

# _seen_case_ids only needs to survive same-day reruns (pipeline runs every
# 2h, so worst case ~12 reruns/day touching overlapping data). The
# historical corpus (Tool 00, aws-corpus/oracle-corpus, quarterly) already
# owns permanent memory of every case ever seen -- the enriched corpus does
# not need to duplicate that job. Case IDs older than this window are
# dropped from the bookkeeping set; the derived aggregate fields
# (session_count, login_success_count, ttps_observed, etc.) they already
# contributed to remain unaffected, since those are running totals, not
# re-derived from the bookkeeping set itself.
DEDUP_WINDOW_DAYS = 2


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=False)


def parse_ts(ts):
    """Parse ISO8601 timestamps consistently, tolerating trailing Z."""
    if ts is None:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def is_critical(ioc):
    return ioc.get("abuse_score", 0) >= CRITICAL_ABUSE_SCORE or ioc.get("is_tor", False)


def ttl_for(ioc):
    return TTL_DAYS_CRITICAL if is_critical(ioc) else TTL_DAYS_DEFAULT


def needs_reenrichment(existing_entry, now):
    """True if this IP's cached enrichment is missing or stale."""
    enriched_at = existing_entry.get("enriched_at")
    if not enriched_at:
        return True
    ttl_days = existing_entry.get("enrichment_ttl_days", TTL_DAYS_DEFAULT)
    age_days = (now - parse_ts(enriched_at)).total_seconds() / 86400.0
    return age_days >= ttl_days


def build_actor_corpus(ir_cases, threat_ips, existing_corpus, now):
    """
    Core accumulation logic. existing_corpus is the previously-written
    enriched_corpus.json (empty dict on first run). Returns the updated
    corpus dict and a stats dict for the highlights/metadata files.
    """
    threat_ip_map = {ioc["indicator"]: ioc for ioc in threat_ips}

    # Group ir_cases by src_ip so we can compute session-level aggregates
    cases_by_ip = {}
    for case in ir_cases:
        ip = case.get("src_ip")
        if not ip:
            continue
        cases_by_ip.setdefault(ip, []).append(case)

    all_ips = set(cases_by_ip.keys()) | set(threat_ip_map.keys())

    new_ip_count = 0
    updated_ip_count = 0
    reenriched_count = 0
    cache_hit_count = 0

    for ip in sorted(all_ips):
        cases = cases_by_ip.get(ip, [])
        existing = existing_corpus.get(ip, {})
        is_new = ip not in existing_corpus

        # --- Behavioral accumulation (from ir_cases.json) ---
        # _seen_case_ids is stored as {case_id: last_seen_timestamp} so it can
        # be pruned by age (DEDUP_WINDOW_DAYS) each run. session_count itself
        # is a separate running total that survives pruning -- pruning only
        # trims the dedup-lookup set, never the counters already derived from it.
        seen_case_ids_raw = existing.get("_seen_case_ids", {})
        if isinstance(seen_case_ids_raw, list):
            # backward-compat: older corpus entries stored a bare list before
            # this patch. Treat every entry as seen "now" so it ages out
            # naturally on the next DEDUP_WINDOW_DAYS boundary rather than
            # being lost immediately.
            seen_case_ids = {cid: now.isoformat() for cid in seen_case_ids_raw}
        else:
            seen_case_ids = dict(seen_case_ids_raw)

        prior_running_session_count = existing.get("session_count", 0)
        genuinely_new_case_ids = [c["case_id"] for c in cases if c["case_id"] not in seen_case_ids]

        for case in cases:
            seen_case_ids[case["case_id"]] = case.get("last_seen", now.isoformat())

        # prune entries outside the dedup window -- doesn't affect counters,
        # only shrinks the lookup set used to detect "have I already counted
        # this case_id" on future reruns
        cutoff = now.timestamp() - (DEDUP_WINDOW_DAYS * 86400)
        seen_case_ids = {
            cid: ts for cid, ts in seen_case_ids.items()
            if parse_ts(ts).timestamp() >= cutoff
        }

        session_count = prior_running_session_count + len(genuinely_new_case_ids)

        # first_seen / last_seen — widen the existing window, never shrink it
        candidate_first = [parse_ts(c["first_seen"]) for c in cases if c.get("first_seen")]
        candidate_last = [parse_ts(c["last_seen"]) for c in cases if c.get("last_seen")]

        existing_first = parse_ts(existing.get("first_seen"))
        existing_last = parse_ts(existing.get("last_seen"))

        all_first = candidate_first + ([existing_first] if existing_first else [])
        all_last = candidate_last + ([existing_last] if existing_last else [])

        first_seen = min(all_first).isoformat() if all_first else None
        last_seen = max(all_last).isoformat() if all_last else None

        # login_success_count — sum booleans, but only for cases not already
        # reflected in the running total (uses the same genuinely-new-case-id
        # set computed above, so a same-day rerun of unchanged ir_cases.json
        # never double-counts, regardless of dedup-window pruning state).
        genuinely_new_case_id_set = set(genuinely_new_case_ids)
        new_login_successes = sum(
            1 for c in cases
            if c["case_id"] in genuinely_new_case_id_set and c.get("login_success")
        )
        login_success_count = existing.get("login_success_count", 0) + new_login_successes

        # last_session_severity — most recent case by timestamp, else keep existing
        severity = existing.get("last_session_severity")
        if cases:
            most_recent = max(cases, key=lambda c: parse_ts(c["last_seen"]))
            severity = most_recent.get("severity", severity)

        # ttps_observed — union across all cases ever seen, cross-run
        ttps_observed = set(existing.get("ttps_observed", []))
        for c in cases:
            ttps_observed.update(c.get("ttps", []))

        # commands_observed / malware_downloaded — derived booleans, sticky true
        commands_observed = existing.get("commands_observed", False) or any(
            len(c.get("commands", [])) > 0 for c in cases
        )
        malware_downloaded = existing.get("malware_downloaded", False) or any(
            len(c.get("downloads", [])) > 0 for c in cases
        )

        # --- Reputation half (from threat_ips.json) ---
        ioc = threat_ip_map.get(ip)
        reputation_fields = {
            "abuse_score": existing.get("abuse_score"),
            "country": existing.get("country"),
            "asn": existing.get("asn"),
            "isp": existing.get("isp"),
            "org": existing.get("org"),
            "is_tor": existing.get("is_tor", False),
            "is_proxy": existing.get("is_proxy", False),
            "is_vpn": existing.get("is_vpn", False),
            "otx_pulses": existing.get("otx_pulses", 0),
        }
        enriched_at = existing.get("enriched_at")
        ttl_days = existing.get("enrichment_ttl_days", TTL_DAYS_DEFAULT)

        needs_refresh = needs_reenrichment(existing, now) if existing else True

        if ioc is not None and needs_refresh:
            # In the real Tool 27 integration, this is the point where a live
            # API call would happen if `ioc` were absent/stale in threat_ips.json.
            # Here, threat_ips.json is already the enriched source, so "refresh"
            # just means: accept this run's values as the new cache entry.
            reputation_fields.update({
                "abuse_score": ioc.get("abuse_score"),
                "country": ioc.get("country"),
                "asn": ioc.get("asn"),
                "isp": ioc.get("isp"),
                "org": ioc.get("org"),
                "is_tor": ioc.get("is_tor", False),
                "is_proxy": ioc.get("is_proxy", False),
                "is_vpn": ioc.get("is_vpn", False),
                "otx_pulses": ioc.get("otx_pulses", 0),
            })
            enriched_at = now.isoformat()
            ttl_days = TTL_DAYS_CRITICAL if is_critical(reputation_fields) else TTL_DAYS_DEFAULT
            reenriched_count += 1
        elif ioc is not None:
            cache_hit_count += 1

        entry = {
            "first_seen": first_seen,
            "last_seen": last_seen,
            "session_count": session_count,
            "login_success_count": login_success_count,
            "last_session_severity": severity,
            "ttps_observed": sorted(ttps_observed),
            "commands_observed": commands_observed,
            "malware_downloaded": malware_downloaded,
            **reputation_fields,
            "enriched_at": enriched_at,
            "enrichment_ttl_days": ttl_days,
            "_seen_case_ids": seen_case_ids,  # {case_id: timestamp}, pruned to DEDUP_WINDOW_DAYS -- internal bookkeeping, not for highlights
        }

        existing_corpus[ip] = entry

        if is_new:
            new_ip_count += 1
        elif session_count > prior_running_session_count:
            updated_ip_count += 1

    stats = {
        "total_ips_in_corpus": len(existing_corpus),
        "new_ips_this_run": new_ip_count,
        "updated_ips_this_run": updated_ip_count,
        "reenriched_this_run": reenriched_count,
        "cache_hits_this_run": cache_hit_count,
    }

    return existing_corpus, stats


def build_highlights(corpus, stats, now):
    """Counts/labels only — no raw IP addresses, per Section 7 of the design doc."""
    total = len(corpus)
    high_risk = sum(1 for v in corpus.values() if (v.get("abuse_score") or 0) >= CRITICAL_ABUSE_SCORE)
    tor = sum(1 for v in corpus.values() if v.get("is_tor"))
    vpn = sum(1 for v in corpus.values() if v.get("is_vpn"))
    proxy = sum(1 for v in corpus.values() if v.get("is_proxy"))
    auth_success = sum(1 for v in corpus.values() if v.get("login_success_count", 0) > 0)
    malware = sum(1 for v in corpus.values() if v.get("malware_downloaded"))

    country_counts = {}
    asn_counts = {}
    for v in corpus.values():
        c = v.get("country")
        a = v.get("asn")
        if c:
            country_counts[c] = country_counts.get(c, 0) + 1
        if a:
            asn_counts[a] = asn_counts.get(a, 0) + 1

    top_countries = sorted(country_counts.items(), key=lambda x: -x[1])[:10]
    top_asns = sorted(asn_counts.items(), key=lambda x: -x[1])[:10]

    return {
        "generated_at": now.isoformat(),
        "total_actors": total,
        "new_actors_this_run": stats["new_ips_this_run"],
        "updated_actors_this_run": stats["updated_ips_this_run"],
        "high_risk_count": high_risk,
        "tor_count": tor,
        "vpn_count": vpn,
        "proxy_count": proxy,
        "auth_success_count": auth_success,
        "malware_delivery_count": malware,
        "top_countries": [{"country": c, "count": n} for c, n in top_countries],
        "top_asns": [{"asn": a, "count": n} for a, n in top_asns],
    }


def prune_actor_corpus(corpus: dict, max_age_days: int = 180) -> int:
    """
    Remove IP entries whose last_seen is older than max_age_days. Mirrors
    tools/37_alerts_live.py's prune_alert_history() exactly -- same cutoff
    computation, same "delete stale keys" pattern, same return-count
    contract, only the record shape and staleness field differ (last_seen
    here vs last_fired in alert_history).

    A 180-day default matches Tool 37's own default so an actor and its
    associated alert history age out on comparable timelines, rather than
    one persisting long after the other has been forgotten.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    stale_keys = []
    for ip, record in corpus.items():
        try:
            last_seen = parse_ts(record.get("last_seen"))
            if last_seen and last_seen < cutoff:
                stale_keys.append(ip)
        except Exception:
            continue
    for ip in stale_keys:
        del corpus[ip]
    return len(stale_keys)


def build_metadata(stats, now, ir_cases_count, threat_ips_count, corpus_size_bytes):
    return {
        "last_updated": now.isoformat(),
        "total_ir_cases_processed": ir_cases_count,
        "total_threat_ips_available": threat_ips_count,
        "api_calls_this_run": stats["reenriched_this_run"],
        "cache_hits_this_run": stats["cache_hits_this_run"],
        "corpus_size_bytes": corpus_size_bytes,
        "corpus_size_ip_count": stats["total_ips_in_corpus"],
    }


def strip_internal_fields(corpus):
    """Produce the public-facing corpus dict without bookkeeping fields
    that shouldn't be considered part of the documented schema."""
    public = {}
    for ip, entry in corpus.items():
        e = dict(entry)
        e.pop("_seen_case_ids", None)
        public[ip] = e
    return public


def main():
    data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data")
    enriched_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("enriched-data")

    ir_cases_raw = load_json(data_dir / "ir_cases.json")
    ir_cases = ir_cases_raw.get("cases", ir_cases_raw) if isinstance(ir_cases_raw, dict) else ir_cases_raw

    threat_ips_raw = load_json(data_dir / "threat_ips.json")
    threat_ips = threat_ips_raw.get("ips", threat_ips_raw) if isinstance(threat_ips_raw, dict) else threat_ips_raw

    corpus_path = data_dir / "enriched_corpus.json"
    existing_corpus = load_json(corpus_path) if corpus_path.exists() else {}

    now = datetime.now(timezone.utc)

    print(f"[43_enriched_corpus] Loaded {len(ir_cases)} ir_cases, {len(threat_ips)} threat_ips, "
          f"{len(existing_corpus)} existing corpus entries")

    corpus, stats = build_actor_corpus(ir_cases, threat_ips, existing_corpus, now)

    # Prune -- sentinel-gated, matches tools/37_alerts_live.py's pattern
    # exactly (see .github/workflows/enriched_corpus.yml's sentinel logic,
    # which mirrors pipeline.yml's Tool 32/37 sentinel pattern rather than
    # an exact-date/hour check -- the latter was tried and rejected for
    # Tool 32's rollups per that workflow's own comment history).
    if "--prune-days" in sys.argv:
        idx = sys.argv.index("--prune-days")
        prune_days = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 180
        pruned_count = prune_actor_corpus(corpus, prune_days)
        print(f"[43_enriched_corpus] Pruned {pruned_count} entries with last_seen older than {prune_days} days")
        stats["pruned_this_run"] = pruned_count
    else:
        stats["pruned_this_run"] = 0

    public_corpus = strip_internal_fields(corpus)
    save_json(corpus_path, corpus)  # internal version, with _seen_case_ids, is the real persisted state

    corpus_size = corpus_path.stat().st_size

    highlights = build_highlights(corpus, stats, now)
    save_json(enriched_dir / "enriched_highlights.json", highlights)

    metadata = build_metadata(stats, now, len(ir_cases), len(threat_ips), corpus_size)
    save_json(enriched_dir / "enriched_metadata.json", metadata)

    print(f"[43_enriched_corpus] Wrote {corpus_path} ({corpus_size:,} bytes, {len(corpus)} IPs)")
    print(f"[43_enriched_corpus] New IPs: {stats['new_ips_this_run']}, "
          f"Updated: {stats['updated_ips_this_run']}, "
          f"Re-enriched (API-equivalent): {stats['reenriched_this_run']}, "
          f"Cache hits: {stats['cache_hits_this_run']}")
    print(json.dumps(highlights, indent=2))

    # Monthly R2 archival step -- only runs when explicitly requested
    # (pipeline.yml's monthly trigger, per design doc Section 8.1), not on
    # every 2h run. Archives the FULL vault (with all IP records) before
    # any future git-side pruning of this corpus is considered -- currently
    # this corpus is never pruned from git (Section 5 table: "Permanent"),
    # so this call is a durability snapshot, not a prerequisite for deletion.
    if "--archive-to-r2" in sys.argv:
        try:
            filename = archive_corpus_to_r2(corpus_path, "actor-corpus")
            print(f"[43_enriched_corpus] R2 archive verified: {filename}")
        except R2UploadError as e:
            print(f"[43_enriched_corpus] R2 ARCHIVE FAILED: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
