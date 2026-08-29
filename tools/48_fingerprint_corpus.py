#!/usr/bin/env python3
"""
Tool 48 — Fingerprint Corpus Builder
=======================================
Reads: data/ssh_fingerprints.json
Writes: data/fingerprint_corpus.json (the vault -- full HASSH records, permanent)
        fingerprint-corpus/fingerprint_highlights.json (counts/labels only,
        no raw HASSH hashes in the highlights display, per design doc)
        fingerprint-corpus/fingerprint_metadata.json (run metadata)

Natural key: hassh (MD5 of SSH KEX negotiation string) -- confirmed present
exactly as named in the real source, no derivation needed.

Field mapping notes (confirmed against real repo data 2026-08-21):

  - This is the BEST-aligned source of the six corpora. Unlike
    command_clusters.json (Tool 44), ssh_fingerprints.json already
    enumerates individual session references in `sessions[]` -- a real
    list of case_id strings (e.g. "IR-17921542c4b9"), not just a count or
    an IP-set proxy. This means dedup here has the SAME rigor as Tool 43's
    case_id-based approach, not Tool 44's weaker IP-set-growth fallback.
  - `first_seen`/`last_seen` already exist per-fingerprint in the source
    -- but same trap as asn_clusters.json (per the original schema
    reconciliation): these are PER-RUN values, recomputed each run, not
    accumulated across runs. This tool widens them properly (min/max
    against the existing corpus entry), same pattern as Tool 43's actor
    first_seen/last_seen.
  - session_count in the source is also per-run. True cross-run count is
    derived here as len(accumulated distinct session IDs), which is exact
    (not a proxy), because sessions[] gives real case_id values to dedupe
    against -- same DEDUP_WINDOW_DAYS discipline as Tool 43: the
    bookkeeping set only needs to survive same-day reruns, not accumulate
    forever, since the historical corpus (Tool 00) already owns permanent
    per-case memory.
  - client_family / botnet_signature / kex_algs / enc_algs / mac_algs /
    comp_algs / version_strings all map directly, no derivation needed.
  - unique_ips accumulates the same way as Tool 44's unique_ips_ever set.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from r2_archive_helper import archive_corpus_to_r2, R2UploadError

# Same rationale as Tool 43: bookkeeping only needs to survive same-day
# pipeline reruns (every 2h, ~12x/day). Tool 00's historical corpus already
# owns permanent case-level memory.
DEDUP_WINDOW_DAYS = 2


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


def build_fingerprint_corpus(fingerprints, existing_corpus, now):
    new_count = 0
    updated_count = 0
    unchanged_count = 0

    for fp in fingerprints:
        hassh = fp.get("hassh")
        if not hassh:
            continue

        existing = existing_corpus.get(hassh, {})
        is_new = hassh not in existing_corpus

        # session dedup -- exact, via real case_id list, same rigor as Tool 43
        seen_sessions_raw = existing.get("_seen_sessions", {})
        if isinstance(seen_sessions_raw, list):
            seen_sessions = {sid: now.isoformat() for sid in seen_sessions_raw}
        else:
            seen_sessions = dict(seen_sessions_raw)

        run_sessions = fp.get("sessions", [])
        genuinely_new_sessions = [s for s in run_sessions if s not in seen_sessions]

        for s in run_sessions:
            seen_sessions[s] = fp.get("last_seen", now.isoformat())

        cutoff = now.timestamp() - (DEDUP_WINDOW_DAYS * 86400)
        seen_sessions = {
            sid: ts for sid, ts in seen_sessions.items()
            if parse_ts(ts).timestamp() >= cutoff
        }

        prior_session_count = existing.get("session_count", 0)
        session_count = prior_session_count + len(genuinely_new_sessions)

        # first_seen/last_seen -- widen existing window, never shrink
        candidate_first = parse_ts(fp.get("first_seen"))
        candidate_last = parse_ts(fp.get("last_seen"))
        existing_first = parse_ts(existing.get("first_seen"))
        existing_last = parse_ts(existing.get("last_seen"))

        all_first = [t for t in [candidate_first, existing_first] if t]
        all_last = [t for t in [candidate_last, existing_last] if t]
        first_seen = min(all_first).isoformat() if all_first else None
        last_seen = max(all_last).isoformat() if all_last else None

        # unique_ips accumulate, same pattern as Tool 44
        run_ips = set(fp.get("unique_ips", []))
        prior_ips = set(existing.get("unique_ips_ever", []))
        combined_ips = run_ips | prior_ips

        entry = {
            "hassh": hassh,
            "client_family": fp.get("client_family", existing.get("client_family")),
            "botnet_signature": fp.get("botnet_signature", existing.get("botnet_signature")),
            "version_strings": sorted(set(fp.get("version_strings", [])) | set(existing.get("version_strings", []))),
            "kex_algs": fp.get("kex_algs", existing.get("kex_algs")),
            "enc_algs": fp.get("enc_algs", existing.get("enc_algs")),
            "mac_algs": fp.get("mac_algs", existing.get("mac_algs")),
            "comp_algs": fp.get("comp_algs", existing.get("comp_algs")),
            "session_count": session_count,
            "unique_ips_ever": sorted(combined_ips),
            "unique_ip_count_ever": len(combined_ips),
            "first_seen": first_seen,
            "last_seen": last_seen,
            "_seen_sessions": seen_sessions,
        }
        existing_corpus[hassh] = entry

        if is_new:
            new_count += 1
        elif genuinely_new_sessions:
            updated_count += 1
        else:
            unchanged_count += 1

    stats = {
        "total_fingerprints_in_corpus": len(existing_corpus),
        "new_this_run": new_count,
        "updated_this_run": updated_count,
        "unchanged_this_run": unchanged_count,
    }
    return existing_corpus, stats


def prune_fingerprint_corpus(corpus: dict, max_age_days: int = 180) -> int:
    """Same delete-by-staleness pattern as tools/37_alerts_live.py's
    prune_alert_history(), keyed on this corpus's own last_seen field."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    stale_keys = []
    for h, record in corpus.items():
        try:
            last_seen = parse_ts(record.get("last_seen"))
            if last_seen and last_seen < cutoff:
                stale_keys.append(h)
        except Exception:
            continue
    for h in stale_keys:
        del corpus[h]
    return len(stale_keys)


def build_highlights(corpus, stats, now):
    total = len(corpus)
    family_counts = {}
    botnet_sigs = set()
    for v in corpus.values():
        fam = v.get("client_family")
        if fam:
            family_counts[fam] = family_counts.get(fam, 0) + 1
        sig = v.get("botnet_signature")
        if sig and sig.lower() not in ("generic scanner", "none", ""):
            botnet_sigs.add(sig)

    top_families = sorted(family_counts.items(), key=lambda x: -x[1])[:10]

    return {
        "generated_at": now.isoformat(),
        "total_unique_hassh": total,
        "new_this_run": stats["new_this_run"],
        "updated_this_run": stats["updated_this_run"],
        "client_families": [{"family": f, "count": n} for f, n in top_families],
        "known_botnet_signatures": sorted(botnet_sigs),
        "note": "HASSH hash values are not displayed here -- see design doc Section 7. Full records in data/fingerprint_corpus.json.",
    }


def build_metadata(stats, now, fingerprints_count, corpus_size_bytes):
    return {
        "last_updated": now.isoformat(),
        "fingerprints_processed_this_run": fingerprints_count,
        "corpus_size_bytes": corpus_size_bytes,
        "corpus_size_hassh_count": stats["total_fingerprints_in_corpus"],
    }


def strip_internal_fields(corpus):
    public = {}
    for h, entry in corpus.items():
        e = dict(entry)
        e.pop("_seen_sessions", None)
        public[h] = e
    return public


def main():
    data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data")
    fp_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("fingerprint-corpus")

    fp_raw = load_json(data_dir / "ssh_fingerprints.json")
    fingerprints = fp_raw.get("fingerprints", fp_raw) if isinstance(fp_raw, dict) else fp_raw

    corpus_path = data_dir / "fingerprint_corpus.json"
    existing_corpus = load_json(corpus_path) if corpus_path.exists() else {}

    now = datetime.now(timezone.utc)

    print(f"[48_fingerprint_corpus] Loaded {len(fingerprints)} fingerprints, "
          f"{len(existing_corpus)} existing corpus entries")

    corpus, stats = build_fingerprint_corpus(fingerprints, existing_corpus, now)

    if "--prune-days" in sys.argv:
        idx = sys.argv.index("--prune-days")
        prune_days = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 180
        pruned_count = prune_fingerprint_corpus(corpus, prune_days)
        print(f"[48_fingerprint_corpus] Pruned {pruned_count} HASSH entries older than {prune_days} days")
        stats["pruned_this_run"] = pruned_count
    else:
        stats["pruned_this_run"] = 0
    save_json(corpus_path, corpus)
    corpus_size = corpus_path.stat().st_size

    highlights = build_highlights(corpus, stats, now)
    save_json(fp_dir / "fingerprint_highlights.json", highlights)

    metadata = build_metadata(stats, now, len(fingerprints), corpus_size)
    save_json(fp_dir / "fingerprint_metadata.json", metadata)

    print(f"[48_fingerprint_corpus] Wrote {corpus_path} ({corpus_size:,} bytes, {len(corpus)} HASSH entries)")
    print(f"[48_fingerprint_corpus] New: {stats['new_this_run']}, Updated: {stats['updated_this_run']}, "
          f"Unchanged: {stats['unchanged_this_run']}")
    print(json.dumps(highlights, indent=2))

    if "--archive-to-r2" in sys.argv:
        try:
            filename = archive_corpus_to_r2(corpus_path, "fingerprint-corpus")
            print(f"[48_fingerprint_corpus] R2 archive verified: {filename}")
        except R2UploadError as e:
            print(f"[48_fingerprint_corpus] R2 ARCHIVE FAILED: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
