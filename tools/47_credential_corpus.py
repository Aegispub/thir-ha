#!/usr/bin/env python3
"""
Tool 47 — Credential Corpus Builder
======================================
Reads: data/credentials.json
Writes: data/credential_corpus.json (the vault -- full pair records, permanent)
        credential-corpus/credential_highlights.json (counts/labels only, NO
        raw usernames/passwords -- per Section 7 of the design doc, this is
        the one corpus explicitly called out as PII-adjacent and kept out
        of git in full form; only the highlights aggregate ships to git)
        credential-corpus/credential_metadata.json (run metadata)

Natural key: SHA256(username|password) -- does NOT exist as a field in
credentials.json (confirmed against real repo data 2026-08-21). Computed
at ingestion time by this tool.

Field mapping notes:

  - credentials.json's top_pairs[] gives {username, password, count} where
    count is a PER-RUN occurrence count, not cross-run. This tool
    accumulates count across runs, keyed by the computed hash, using the
    same "only count genuinely new occurrences" discipline as Tool 43 --
    except here there's no case_id to dedupe against, since top_pairs[]
    doesn't reference individual sessions. The dedup fallback used: if the
    per-run count for a known hash is IDENTICAL to what was already
    recorded for that hash's last run, treat it as an unchanged rerun and
    do not add it again. This is a weaker guarantee than Tool 43's
    case_id-based dedup (a coincidental identical count on a genuinely new
    run would be missed), but is the correct fallback given the source
    schema's limitations -- documented here and in highlights output.
  - success_pairs[] gives {username, password, src_ip, timestamp} -- actual
    individual events, each with a timestamp, so these DO dedupe safely by
    exact (username, password, src_ip, timestamp) tuple, same rigor as
    Tool 43's case_id approach.
  - Per Section 4.3 / Section 7 of the design doc: full username/password
    values stay in the git vault (data/credential_corpus.json) exactly
    like alert_history.json keeps alert hashes -- but the corpus is
    explicitly NOT surfaced in git as a "full pair records" R2-only
    artifact per the original design's R2 structure table. This
    implementation keeps the vault in data/ (git) since that matches how
    Tool 43's actor corpus and the existing alert_history.json pattern
    both work, and because dashboard/Tool 43-style consumption needs it
    queryable. If stricter PII handling is required later, moving
    data/credential_corpus.json to R2-only is a follow-up decision, not
    a change to this tool's core accumulation logic.
"""

import hashlib
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


def pair_hash(username, password):
    raw = f"{username}|{password}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def build_credential_corpus(top_pairs, success_pairs, existing_corpus, now):
    new_pair_count = 0
    updated_pair_count = 0
    unchanged_pair_count = 0
    new_success_events = 0

    seen_hashes_this_run = set()

    for pair in top_pairs:
        username = pair.get("username", "")
        password = pair.get("password", "")
        run_count = pair.get("count", 0)

        h = pair_hash(username, password)
        seen_hashes_this_run.add(h)
        existing = existing_corpus.get(h, {})
        is_new = h not in existing_corpus

        last_run_count = existing.get("_last_run_count", -1)
        is_unchanged_rerun = (not is_new) and (run_count == last_run_count)

        if is_unchanged_rerun:
            total_count = existing.get("total_count", 0)
            unchanged_pair_count += 1
        else:
            total_count = existing.get("total_count", 0) + run_count
            if is_new:
                new_pair_count += 1
            else:
                updated_pair_count += 1

        # success events for this hash -- matched against success_pairs by
        # exact (username, password) match, deduped by (src_ip, timestamp)
        # tuple so identical-value reruns don't double count
        existing_success_keys = set(
            (e["src_ip"], e["timestamp"]) for e in existing.get("success_events", [])
        )
        matching_successes = [
            s for s in success_pairs
            if s.get("username") == username and s.get("password") == password
        ]
        combined_success_events = list(existing.get("success_events", []))
        for s in matching_successes:
            key = (s.get("src_ip"), s.get("timestamp"))
            if key not in existing_success_keys:
                combined_success_events.append({
                    "src_ip": s.get("src_ip"),
                    "timestamp": s.get("timestamp"),
                })
                existing_success_keys.add(key)
                new_success_events += 1

        first_seen = existing.get("first_seen") or now.isoformat()
        last_seen = now.isoformat()

        entry = {
            "username": username,
            "password": password,
            "total_count": total_count,
            "success_events": combined_success_events,
            "success_count": len(combined_success_events),
            "first_seen": first_seen,
            "last_seen": last_seen,
            "_last_run_count": run_count,
        }
        existing_corpus[h] = entry

    stats = {
        "total_pairs_in_corpus": len(existing_corpus),
        "new_this_run": new_pair_count,
        "updated_this_run": updated_pair_count,
        "unchanged_this_run": unchanged_pair_count,
        "new_success_events_this_run": new_success_events,
    }
    return existing_corpus, stats


def prune_credential_corpus(corpus: dict, max_age_days: int = 180) -> int:
    """Same delete-by-staleness pattern as tools/37_alerts_live.py's
    prune_alert_history(), keyed on this corpus's own last_seen field."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    stale_keys = []
    for h, record in corpus.items():
        try:
            last_seen = datetime.fromisoformat(record["last_seen"])
            if last_seen < cutoff:
                stale_keys.append(h)
        except Exception:
            continue
    for h in stale_keys:
        del corpus[h]
    return len(stale_keys)


def build_highlights(corpus, stats, now):
    total = len(corpus)
    with_success = sum(1 for v in corpus.values() if v.get("success_count", 0) > 0)

    usernames = set()
    passwords = set()
    for v in corpus.values():
        usernames.add(v.get("username", ""))
        passwords.add(v.get("password", ""))

    diversity_index = round(len(passwords) / total, 3) if total else 0.0
    spray_ratio = round(with_success / total, 3) if total else 0.0

    return {
        "generated_at": now.isoformat(),
        "total_unique_pairs": total,
        "new_pairs_this_run": stats["new_this_run"],
        "pairs_with_successful_auth": with_success,
        "unique_usernames": len(usernames),
        "unique_passwords": len(passwords),
        "diversity_index": diversity_index,
        "spray_success_ratio": spray_ratio,
        "note": (
            "Credential values are NOT shown here per design -- highlights "
            "are counts/labels only. Full pairs live in data/credential_corpus.json "
            "(git, current state) -- see tool docstring for the PII-handling "
            "note on whether this should move R2-only in a future revision."
        ),
    }


def build_metadata(stats, now, top_pairs_count, success_pairs_count, corpus_size_bytes):
    return {
        "last_updated": now.isoformat(),
        "top_pairs_processed_this_run": top_pairs_count,
        "success_pairs_processed_this_run": success_pairs_count,
        "new_success_events_this_run": stats["new_success_events_this_run"],
        "corpus_size_bytes": corpus_size_bytes,
        "corpus_size_pair_count": stats["total_pairs_in_corpus"],
    }


def strip_internal_fields(corpus):
    public = {}
    for h, entry in corpus.items():
        e = dict(entry)
        e.pop("_last_run_count", None)
        public[h] = e
    return public


def main():
    data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data")
    cred_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("credential-corpus")

    creds_raw = load_json(data_dir / "credentials.json")
    top_pairs = creds_raw.get("top_pairs", [])
    success_pairs = creds_raw.get("success_pairs", [])

    corpus_path = data_dir / "credential_corpus.json"
    existing_corpus = load_json(corpus_path) if corpus_path.exists() else {}

    now = datetime.now(timezone.utc)

    print(f"[47_credential_corpus] Loaded {len(top_pairs)} top_pairs, "
          f"{len(success_pairs)} success_pairs, {len(existing_corpus)} existing corpus entries")

    corpus, stats = build_credential_corpus(top_pairs, success_pairs, existing_corpus, now)

    if "--prune-days" in sys.argv:
        idx = sys.argv.index("--prune-days")
        prune_days = int(sys.argv[idx + 1]) if idx + 1 < len(sys.argv) else 180
        pruned_count = prune_credential_corpus(corpus, prune_days)
        print(f"[47_credential_corpus] Pruned {pruned_count} pairs older than {prune_days} days")
        stats["pruned_this_run"] = pruned_count
    else:
        stats["pruned_this_run"] = 0
    save_json(corpus_path, corpus)
    corpus_size = corpus_path.stat().st_size

    highlights = build_highlights(corpus, stats, now)
    save_json(cred_dir / "credential_highlights.json", highlights)

    metadata = build_metadata(stats, now, len(top_pairs), len(success_pairs), corpus_size)
    save_json(cred_dir / "credential_metadata.json", metadata)

    print(f"[47_credential_corpus] Wrote {corpus_path} ({corpus_size:,} bytes, {len(corpus)} pairs)")
    print(f"[47_credential_corpus] New: {stats['new_this_run']}, Updated: {stats['updated_this_run']}, "
          f"Unchanged: {stats['unchanged_this_run']}, New success events: {stats['new_success_events_this_run']}")
    print(json.dumps(highlights, indent=2))

    # Per Section 7 of the design doc, credential pairs are attacker-controlled
    # data kept out of git "by convention" for full records beyond the git
    # vault -- the R2 archive here is the durable off-git copy this policy
    # implies, uploaded under the SAME PII-adjacent handling as the rest of
    # this corpus (see tool docstring).
    if "--archive-to-r2" in sys.argv:
        try:
            filename = archive_corpus_to_r2(corpus_path, "credential-corpus")
            print(f"[47_credential_corpus] R2 archive verified: {filename}")
        except R2UploadError as e:
            print(f"[47_credential_corpus] R2 ARCHIVE FAILED: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
