#!/usr/bin/env python3
"""
Tool 44 — Campaign Corpus Builder
===================================
Reads: data/command_clusters.json
Writes: data/campaign_corpus.json (the vault — full cluster records, permanent)
        campaign-corpus/campaign_highlights.json (counts/labels only)
        campaign-corpus/campaign_metadata.json (run metadata)

Natural key: sequence_hash (SHA-derived, stable across runs per Tool 36's
own hashing — confirmed against real command_clusters.json, field exists
exactly as named, no derivation needed).

Field mapping notes (confirmed against real repo data 2026-08-21):

  - cluster_id (e.g. "CLU-001") is run-scoped, NOT stable across runs —
    Tool 36 can reassign CLU-00N numbers between runs as new clusters
    appear/disappear. sequence_hash is the only safe cross-run key.
  - session_count in command_clusters.json is a per-run count (how many
    sessions matched this pattern in the current pipeline window), not
    cross-run. This tool accumulates it properly using the same
    seen-case-id-set pattern as Tool 43, to avoid double-counting on
    reruns against unchanged input.
  - Sessions are NOT individually enumerated in command_clusters.json
    (unlike ssh_fingerprints.json's sessions[] list) — only session_count
    and unique_ips[] are given per cluster. This means true dedup against
    "have I seen this exact session before" isn't possible from this
    source alone. The dedup fallback used here: track unique_ips seen
    per cluster cross-run (a proxy signal — a cluster still active with
    the same IP set on a rerun of the same window is likely the same
    activity, not new activity). This is a known limitation, documented
    inline and in the highlights output as `note`.
  - is_campaign / campaign_name / campaign_severity / campaign_description
    / matched_campaigns[] all map directly, richer than the original
    design doc assumed (includes pattern_hits/pattern_total fidelity
    scoring per matched campaign signature).
  - first_seen / last_seen for a campaign (when did this sequence_hash
    first appear, is it still active) do NOT exist in command_clusters.json
    at all — net new accumulation, same category as Tool 43's actor
    first_seen/last_seen.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from r2_archive_helper import archive_corpus_to_r2, R2UploadError

STALE_AFTER_DAYS = 14  # a campaign not seen in any run for this long is considered "ended"


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


def build_campaign_corpus(clusters, existing_corpus, now):
    new_count = 0
    updated_count = 0
    reactivated_count = 0
    unchanged_count = 0

    seen_hashes_this_run = set()

    for cluster in clusters:
        seq_hash = cluster.get("sequence_hash")
        if not seq_hash:
            continue  # skip malformed entries defensively

        seen_hashes_this_run.add(seq_hash)
        existing = existing_corpus.get(seq_hash, {})
        is_new = seq_hash not in existing_corpus

        run_ips = set(cluster.get("unique_ips", []))
        prior_ips = set(existing.get("unique_ips_ever", []))
        combined_ips = run_ips | prior_ips
        ip_set_grew = len(combined_ips) > len(prior_ips)

        # session_count accumulation via the IP-set-growth proxy documented above.
        # If the IP set didn't grow, treat this run's session_count as already
        # reflected (avoids double counting on an unchanged rerun). If it did
        # grow, add this run's session_count as incremental new activity.
        prior_session_count = existing.get("session_count", 0)
        if is_new:
            session_count = cluster.get("session_count", 0)
        elif ip_set_grew:
            session_count = prior_session_count + cluster.get("session_count", 0)
        else:
            session_count = prior_session_count  # unchanged — likely same rerun window

        first_seen = existing.get("first_seen") or now.isoformat()
        last_seen = now.isoformat()  # this cluster appeared in this run, so it's active now

        status = "active"
        if not is_new and not ip_set_grew and existing.get("status") == "ended":
            status = "reactivated"
            reactivated_count += 1

        entry = {
            "sequence_hash": seq_hash,
            "cluster_id_last_seen_as": cluster.get("cluster_id"),
            "is_campaign": cluster.get("is_campaign", False),
            "campaign_name": cluster.get("campaign_name"),
            "campaign_severity": cluster.get("campaign_severity"),
            "campaign_description": cluster.get("campaign_description"),
            "matched_campaigns": cluster.get("matched_campaigns", []),
            "ttps": cluster.get("ttps", []),
            "session_count": session_count,
            "unique_ips_ever": sorted(combined_ips),
            "unique_ip_count_ever": len(combined_ips),
            "first_seen": first_seen,
            "last_seen": last_seen,
            "status": status,
        }

        existing_corpus[seq_hash] = entry

        if is_new:
            new_count += 1
        elif ip_set_grew:
            updated_count += 1
        else:
            unchanged_count += 1

    # Mark campaigns not seen in this run as potentially ended, if stale enough
    ended_count = 0
    for seq_hash, entry in existing_corpus.items():
        if seq_hash in seen_hashes_this_run:
            continue
        if entry.get("status") == "ended":
            continue
        last_seen_dt = parse_ts(entry.get("last_seen"))
        if last_seen_dt and (now - last_seen_dt).days >= STALE_AFTER_DAYS:
            entry["status"] = "ended"
            ended_count += 1

    stats = {
        "total_campaigns_in_corpus": len(existing_corpus),
        "new_this_run": new_count,
        "updated_this_run": updated_count,
        "unchanged_this_run": unchanged_count,
        "reactivated_this_run": reactivated_count,
        "ended_this_run": ended_count,
    }
    return existing_corpus, stats


def prune_campaign_corpus(corpus: dict, max_age_days: int = 180) -> int:
    """
    Deletes campaign entries entirely once they are BOTH marked "ended"
    (14-day staleness, existing logic above) AND have been ended for
    longer than max_age_days beyond that. This two-stage design keeps
    the existing status-flip behaviour intact (a campaign silent for 14
    days is flagged "ended" but stays fully queryable) while adding true
    deletion only for campaigns that have been dormant for a genuinely
    long time -- mirrors tools/37_alerts_live.py's prune_alert_history()
    delete pattern, applied on top of this corpus's own existing
    ended-status concept rather than replacing it.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    stale_keys = []
    for seq_hash, record in corpus.items():
        if record.get("status") != "ended":
            continue
        try:
            last_seen = parse_ts(record.get("last_seen"))
            if last_seen and last_seen < cutoff:
                stale_keys.append(seq_hash)
        except Exception:
            continue
    for seq_hash in stale_keys:
        del corpus[seq_hash]
    return len(stale_keys)


def build_highlights(corpus, stats, now):
    active = [v for v in corpus.values() if v.get("status") in ("active", "reactivated")]
    ended = [v for v in corpus.values() if v.get("status") == "ended"]

    largest = max(corpus.values(), key=lambda v: v.get("unique_ip_count_ever", 0), default=None)

    ttp_combo_counts = {}
    for v in corpus.values():
        for ttp in v.get("ttps", []):
            tid = ttp.get("id") if isinstance(ttp, dict) else ttp
            if tid:
                ttp_combo_counts[tid] = ttp_combo_counts.get(tid, 0) + 1
    top_ttps = sorted(ttp_combo_counts.items(), key=lambda x: -x[1])[:10]

    return {
        "generated_at": now.isoformat(),
        "total_campaigns": len(corpus),
        "active_campaigns": len(active),
        "ended_campaigns": len(ended),
        "new_this_run": stats["new_this_run"],
        "reactivated_this_run": stats["reactivated_this_run"],
        "largest_campaign_ip_count": largest.get("unique_ip_count_ever") if largest else 0,
        "largest_campaign_name": largest.get("campaign_name") if largest else None,
        "top_ttp_ids": [{"ttp": t, "count": n} for t, n in top_ttps],
        "note": (
            "session_count accumulation uses an IP-set-growth proxy, not "
            "individual session_id tracking, because command_clusters.json "
            "does not enumerate session IDs per cluster (unlike "
            "ssh_fingerprints.json). See tool docstring."
        ),
    }


def build_metadata(stats, now, clusters_count, corpus_size_bytes):
    return {
        "last_updated": now.isoformat(),
        "total_clusters_processed_this_run": clusters_count,
        "corpus_size_bytes": corpus_size_bytes,
        "corpus_size_campaign_count": stats["total_campaigns_in_corpus"],
    }


def main():
    data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data")
    campaign_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("campaign-corpus")

    cc_raw = load_json(data_dir / "command_clusters.json")
    clusters = cc_raw.get("clusters", cc_raw) if isinstance(cc_raw, dict) else cc_raw

    corpus_path = data_dir / "campaign_corpus.json"
    existing_corpus = load_json(corpus_path) if corpus_path.exists() else {}

    now = datetime.now(timezone.utc)

    print(f"[44_campaign_corpus] Loaded {len(clusters)} clusters, "
          f"{len(existing_corpus)} existing corpus entries")

    corpus, stats = build_campaign_corpus(clusters, existing_corpus, now)

    if "--prune-days" in sys.argv:
        idx = sys.argv.index("--prune-days")
        prune_days = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 180
        pruned_count = prune_campaign_corpus(corpus, prune_days)
        print(f"[44_campaign_corpus] Pruned {pruned_count} ended campaigns older than {prune_days} days")
        stats["pruned_this_run"] = pruned_count
    else:
        stats["pruned_this_run"] = 0
    save_json(corpus_path, corpus)
    corpus_size = corpus_path.stat().st_size

    highlights = build_highlights(corpus, stats, now)
    save_json(campaign_dir / "campaign_highlights.json", highlights)

    metadata = build_metadata(stats, now, len(clusters), corpus_size)
    save_json(campaign_dir / "campaign_metadata.json", metadata)

    print(f"[44_campaign_corpus] Wrote {corpus_path} ({corpus_size:,} bytes, {len(corpus)} campaigns)")
    print(f"[44_campaign_corpus] New: {stats['new_this_run']}, Updated: {stats['updated_this_run']}, "
          f"Unchanged: {stats['unchanged_this_run']}, Reactivated: {stats['reactivated_this_run']}, "
          f"Ended: {stats['ended_this_run']}")
    print(json.dumps(highlights, indent=2))

    if "--archive-to-r2" in sys.argv:
        try:
            filename = archive_corpus_to_r2(corpus_path, "campaign-corpus")
            print(f"[44_campaign_corpus] R2 archive verified: {filename}")
        except R2UploadError as e:
            print(f"[44_campaign_corpus] R2 ARCHIVE FAILED: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
