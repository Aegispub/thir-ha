#!/usr/bin/env python3
"""
Tool 50 — Infrastructure Corpus Builder
==========================================
Reads: data/asn_clusters.json
       data/enriched_corpus.json (optional cross-reference -- per-IP
       enrichment already accumulated by Tool 43, joined here by ASN)
Writes: data/infrastructure_corpus.json (the vault -- full ASN records, permanent)
        infrastructure-corpus/infrastructure_highlights.json (counts/labels
        only, no raw IPs, per design doc)
        infrastructure-corpus/infrastructure_metadata.json (run metadata)

Natural key: asn (e.g. "AS9498") -- confirmed present exactly as named,
stable network identifier, no derivation needed.

Field mapping notes -- THE ONE GENUINE TRAP IN THIS DATASET (confirmed
against real repo data 2026-08-21, flagged explicitly here because it is
easy to miss):

  - asn_clusters.json ALREADY HAS fields named first_seen and last_seen,
    identical in name to what a cross-run corpus needs. It is tempting to
    assume this means the accumulation problem is already solved for this
    corpus. IT IS NOT. Confirmed directly: for AS9498 in the live data,
    first_seen and last_seen are 8 SECONDS apart (16:38:26 to 16:38:34) --
    these are per-run computation timestamps (when Tool 30b's clustering
    pass started/finished touching this ASN's IPs within THIS run), not
    genuine first-ever-seen / most-recent-ever-seen values. Every other
    corpus in this build (Actor, Campaign, Fingerprint) either had no
    first_seen/last_seen fields at all, or had them and they were
    similarly per-run -- this is the SAME trap as ir_cases.json's
    first_seen/last_seen at the case level (which Tool 43 correctly widens
    cross-run). This tool applies the identical min/max-widening pattern,
    explicitly NOT trusting the source's first_seen/last_seen as already
    being cross-run values.
  - avg_abuse_score / max_abuse_score are per-run averages over the IPs
    seen in THIS run's window -- cross-run, this tool tracks a running
    max_abuse_score_ever (sticky high-water mark, never decreases) and
    recomputes avg_abuse_score_ever as a weighted average across all
    IP-observations ever attributed to this ASN, using ip_count as the
    weight for each run's contribution.
  - risk_tier / tags are recomputed fresh each run from source (not
    accumulated) since they reflect the ASN's CURRENT assessed risk, not
    a historical record -- this is a deliberate choice, documented here so
    it isn't mistaken for an oversight relative to the accumulation
    pattern used elsewhere.
  - unique_ips accumulates the same way as Tool 44/48's unique_ips_ever
    pattern.
  - Cross-reference to enriched_corpus.json (Tool 43's output) is
    OPTIONAL and additive: if present, this tool can pull is_tor/is_vpn
    counts from actual per-IP enrichment data for IPs attributed to this
    ASN, as a richer alternative to relying solely on asn_clusters.json's
    own tor_count/vpn_count fields. Implemented as a best-effort join --
    absence of enriched_corpus.json does not block this tool from running.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from r2_archive_helper import archive_corpus_to_r2, R2UploadError


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=False)


def parse_ts(ts):
    if ts is None:
        return None
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def build_infrastructure_corpus(clusters, enriched_corpus, existing_corpus, now):
    new_count = 0
    updated_count = 0
    unchanged_count = 0

    for cluster in clusters:
        asn = cluster.get("asn")
        if not asn:
            continue

        existing = existing_corpus.get(asn, {})
        is_new = asn not in existing_corpus

        run_ips = set(cluster.get("unique_ips", []))
        prior_ips = set(existing.get("unique_ips_ever", []))
        combined_ips = run_ips | prior_ips
        ip_set_grew = len(combined_ips) > len(prior_ips)

        # --- The trap fix: do NOT trust source first_seen/last_seen as
        # cross-run. Widen against the existing corpus entry's own tracked
        # window instead, exactly like Tool 43's actor first_seen/last_seen. ---
        source_first = parse_ts(cluster.get("first_seen"))
        source_last = parse_ts(cluster.get("last_seen"))
        existing_first = parse_ts(existing.get("first_seen_ever"))
        existing_last = parse_ts(existing.get("last_seen_ever"))

        all_first = [t for t in [source_first, existing_first] if t]
        all_last = [t for t in [source_last, existing_last] if t]
        first_seen_ever = min(all_first).isoformat() if all_first else None
        last_seen_ever = max(all_last).isoformat() if all_last else None

        # Sticky high-water mark for max_abuse_score
        prior_max = existing.get("max_abuse_score_ever", 0)
        current_max = cluster.get("max_abuse_score", 0)
        max_abuse_score_ever = max(prior_max, current_max)

        # Weighted running average for avg_abuse_score, using ip_count as weight
        prior_avg = existing.get("avg_abuse_score_ever", 0.0)
        prior_weight = existing.get("_avg_score_weight", 0)
        run_avg = cluster.get("avg_abuse_score", 0.0)
        run_weight = cluster.get("ip_count", 0)

        total_weight = prior_weight + run_weight
        if total_weight > 0:
            avg_abuse_score_ever = round(
                ((prior_avg * prior_weight) + (run_avg * run_weight)) / total_weight, 2
            )
        else:
            avg_abuse_score_ever = run_avg

        # Optional enrichment cross-reference from Tool 43's output
        tor_from_enriched = 0
        vpn_from_enriched = 0
        proxy_from_enriched = 0
        if enriched_corpus:
            for ip in run_ips:
                ip_entry = enriched_corpus.get(ip)
                if ip_entry:
                    if ip_entry.get("is_tor"):
                        tor_from_enriched += 1
                    if ip_entry.get("is_vpn"):
                        vpn_from_enriched += 1
                    if ip_entry.get("is_proxy"):
                        proxy_from_enriched += 1

        entry = {
            "asn": asn,
            "asn_name": cluster.get("asn_name"),
            "isps": sorted(set(cluster.get("isps", [])) | set(existing.get("isps", []))),
            "top_country": cluster.get("top_country"),
            "countries_seen": sorted(set(cluster.get("countries", [])) | set(existing.get("countries_seen", []))),
            "unique_ips_ever": sorted(combined_ips),
            "unique_ip_count_ever": len(combined_ips),
            "avg_abuse_score_ever": avg_abuse_score_ever,
            "max_abuse_score_ever": max_abuse_score_ever,
            "risk_tier_current": cluster.get("risk_tier"),  # deliberately NOT accumulated, see docstring
            "tags_current": cluster.get("tags", []),          # deliberately NOT accumulated, see docstring
            "tor_count_current": cluster.get("tor_count", 0),
            "vpn_count_current": cluster.get("vpn_count", 0),
            "proxy_count_current": cluster.get("proxy_count", 0),
            "tor_confirmed_via_enriched_corpus": tor_from_enriched,
            "vpn_confirmed_via_enriched_corpus": vpn_from_enriched,
            "proxy_confirmed_via_enriched_corpus": proxy_from_enriched,
            "first_seen_ever": first_seen_ever,
            "last_seen_ever": last_seen_ever,
            "_avg_score_weight": total_weight,
        }
        existing_corpus[asn] = entry

        if is_new:
            new_count += 1
        elif ip_set_grew or max_abuse_score_ever > prior_max:
            updated_count += 1
        else:
            unchanged_count += 1

    stats = {
        "total_asns_in_corpus": len(existing_corpus),
        "new_this_run": new_count,
        "updated_this_run": updated_count,
        "unchanged_this_run": unchanged_count,
    }
    return existing_corpus, stats


def prune_infrastructure_corpus(corpus: dict, max_age_days: int = 180) -> int:
    """Same delete-by-staleness pattern as tools/37_alerts_live.py's
    prune_alert_history(), keyed on this corpus's last_seen_ever field."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    stale_keys = []
    for asn, record in corpus.items():
        try:
            last_seen = parse_ts(record.get("last_seen_ever"))
            if last_seen and last_seen < cutoff:
                stale_keys.append(asn)
        except Exception:
            continue
    for asn in stale_keys:
        del corpus[asn]
    return len(stale_keys)


def build_highlights(corpus, stats, now):
    total = len(corpus)
    high_risk = sum(1 for v in corpus.values() if v.get("risk_tier_current") in ("HIGH", "CRITICAL"))
    anon_infra = sum(
        1 for v in corpus.values()
        if v.get("tor_count_current", 0) > 0 or v.get("vpn_count_current", 0) > 0 or v.get("proxy_count_current", 0) > 0
    )
    # "Persistent" ASNs -- seen across a first/last window wider than one
    # run's typical span (a few seconds, per the trap documented above).
    # Anything with more than 60 seconds of first->last spread has survived
    # at least one accumulation step beyond its origin run.
    persistent = 0
    for v in corpus.values():
        fs = parse_ts(v.get("first_seen_ever"))
        ls = parse_ts(v.get("last_seen_ever"))
        if fs and ls and (ls - fs).total_seconds() > 60:
            persistent += 1

    return {
        "generated_at": now.isoformat(),
        "total_asns": total,
        "new_this_run": stats["new_this_run"],
        "high_risk_asns": high_risk,
        "anonymous_infrastructure_asns": anon_infra,
        "persistent_asns": persistent,
        "note": (
            "Raw IPs are not displayed here -- see design doc Section 7. "
            "first_seen_ever/last_seen_ever are genuinely cross-run values, "
            "NOT copied from asn_clusters.json's own first_seen/last_seen "
            "fields, which are per-run only -- see tool docstring."
        ),
    }


def build_metadata(stats, now, clusters_count, corpus_size_bytes, enriched_corpus_available):
    return {
        "last_updated": now.isoformat(),
        "clusters_processed_this_run": clusters_count,
        "enriched_corpus_cross_reference_available": enriched_corpus_available,
        "corpus_size_bytes": corpus_size_bytes,
        "corpus_size_asn_count": stats["total_asns_in_corpus"],
    }


def strip_internal_fields(corpus):
    public = {}
    for asn, entry in corpus.items():
        e = dict(entry)
        e.pop("_avg_score_weight", None)
        public[asn] = e
    return public


def main():
    data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data")
    infra_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("infrastructure-corpus")

    asn_raw = load_json(data_dir / "asn_clusters.json")
    clusters = asn_raw.get("clusters", asn_raw) if isinstance(asn_raw, dict) else asn_raw

    enriched_path = data_dir / "enriched_corpus.json"
    enriched_corpus = load_json(enriched_path) if enriched_path.exists() else None

    corpus_path = data_dir / "infrastructure_corpus.json"
    existing_corpus = load_json(corpus_path) if corpus_path.exists() else {}

    now = datetime.now(timezone.utc)

    print(f"[50_infrastructure_corpus] Loaded {len(clusters)} ASN clusters, "
          f"enriched_corpus.json {'available' if enriched_corpus else 'NOT available'}, "
          f"{len(existing_corpus)} existing corpus entries")

    corpus, stats = build_infrastructure_corpus(clusters, enriched_corpus, existing_corpus, now)

    if "--prune-days" in sys.argv:
        idx = sys.argv.index("--prune-days")
        prune_days = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 180
        pruned_count = prune_infrastructure_corpus(corpus, prune_days)
        print(f"[50_infrastructure_corpus] Pruned {pruned_count} ASNs older than {prune_days} days")
        stats["pruned_this_run"] = pruned_count
    else:
        stats["pruned_this_run"] = 0
    save_json(corpus_path, corpus)
    corpus_size = corpus_path.stat().st_size

    highlights = build_highlights(corpus, stats, now)
    save_json(infra_dir / "infrastructure_highlights.json", highlights)

    metadata = build_metadata(stats, now, len(clusters), corpus_size, enriched_corpus is not None)
    save_json(infra_dir / "infrastructure_metadata.json", metadata)

    print(f"[50_infrastructure_corpus] Wrote {corpus_path} ({corpus_size:,} bytes, {len(corpus)} ASNs)")
    print(f"[50_infrastructure_corpus] New: {stats['new_this_run']}, Updated: {stats['updated_this_run']}, "
          f"Unchanged: {stats['unchanged_this_run']}")
    print(json.dumps(highlights, indent=2))

    if "--archive-to-r2" in sys.argv:
        try:
            filename = archive_corpus_to_r2(corpus_path, "infrastructure-corpus")
            print(f"[50_infrastructure_corpus] R2 archive verified: {filename}")
        except R2UploadError as e:
            print(f"[50_infrastructure_corpus] R2 ARCHIVE FAILED: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
