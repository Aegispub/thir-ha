#!/usr/bin/env python3
"""
Regression test for Bundle B (F3) -- tools/43_enriched_corpus.py

Covers the exact failure mode: an IP whose key is ABSENT from the
current run's input delta (ir_cases.json / threat_ips.json), but which
has a stale _seen_case_ids sub-dict left over from a previous run, must
still be pruned by build_actor_corpus(). Pre-fix, the in-loop prune only
ever visited IPs present in `all_ips = cases_by_ip.keys() | threat_ip_map.keys()`
-- an IP silent for the current run was never revisited, so its
bookkeeping dict was copied forward unpruned forever.

No test framework dependency -- plain assert, __main__-invocable, matching
the repo's existing convention (no tests/ directory existed before this
patch). Run directly: python3 tests/test_tool43_whole_corpus_prune.py
"""

import sys
import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOL43_PATH = Path(__file__).resolve().parent.parent / "tools" / "43_enriched_corpus.py"


def _load_tool43():
    spec = importlib.util.spec_from_file_location("tool43", TOOL43_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def iso(dt: datetime) -> str:
    return dt.isoformat()


def test_f3_stale_ip_absent_from_delta_is_still_pruned(t43):
    """The core regression: an IP with old _seen_case_ids entries that
    does NOT appear in this run's ir_cases.json or threat_ips.json must
    still have those stale entries removed."""
    now = datetime.now(timezone.utc)

    absent_ip = "198.51.100.7"   # will NOT appear in ir_cases/threat_ips this run
    active_ip = "198.51.100.8"   # WILL appear this run

    existing_corpus = {
        absent_ip: {
            "first_seen": iso(now - timedelta(days=30)),
            "last_seen": iso(now - timedelta(days=15)),
            "session_count": 5,
            "login_success_count": 0,
            "last_session_severity": "LOW",
            "ttps_observed": [],
            "commands_observed": False,
            "malware_downloaded": False,
            "abuse_score": None, "country": None, "asn": None,
            "isp": None, "org": None, "is_tor": False,
            "is_proxy": False, "is_vpn": False, "otx_pulses": 0,
            "enriched_at": iso(now - timedelta(days=15)),
            "enrichment_ttl_days": 30,
            "_seen_case_ids": {
                "IR-old0001": iso(now - timedelta(days=12)),  # stale, >2d
                "IR-old0002": iso(now - timedelta(days=20)),  # stale, >2d
            },
        },
        active_ip: {
            "first_seen": iso(now - timedelta(days=1)),
            "last_seen": iso(now),
            "session_count": 1,
            "login_success_count": 0,
            "last_session_severity": "LOW",
            "ttps_observed": [],
            "commands_observed": False,
            "malware_downloaded": False,
            "abuse_score": None, "country": None, "asn": None,
            "isp": None, "org": None, "is_tor": False,
            "is_proxy": False, "is_vpn": False, "otx_pulses": 0,
            "enriched_at": iso(now),
            "enrichment_ttl_days": 30,
            "_seen_case_ids": {
                "IR-new0001": iso(now),  # fresh, must survive
            },
        },
    }

    # This run's delta only contains active_ip -- absent_ip is genuinely
    # absent from both inputs, exactly reproducing the real-world scenario
    # (97.9% of corpus IPs were found to be in this state).
    ir_cases = [
        {
            "case_id": "IR-new0002",
            "src_ip": active_ip,
            "first_seen": iso(now),
            "last_seen": iso(now),
            "login_success": False,
            "ttps": [],
            "commands": [],
            "downloads": [],
            "severity": "LOW",
        }
    ]
    threat_ips = []

    updated_corpus, stats = t43.build_actor_corpus(
        ir_cases, threat_ips, existing_corpus, now
    )

    absent_seen = updated_corpus[absent_ip]["_seen_case_ids"]
    assert absent_seen == {}, (
        f"F3 REGRESSION: absent_ip's stale _seen_case_ids entries were not "
        f"pruned even though the IP never appeared in this run's delta. "
        f"Found: {absent_seen}"
    )
    print("  PASS: IP absent from current delta still had its stale _seen_case_ids pruned")

    # session_count (the derived running total) must be UNAFFECTED by the
    # prune -- pruning only trims the dedup-lookup set, per the tool's own
    # documented contract, never the counters already derived from it.
    assert updated_corpus[absent_ip]["session_count"] == 5, (
        "F3 REGRESSION: pruning _seen_case_ids incorrectly altered "
        "session_count, which must remain a running total independent "
        "of the bookkeeping set's current contents"
    )
    print("  PASS: session_count (running total) unaffected by the prune")

    # active_ip's fresh entry must survive.
    active_seen = updated_corpus[active_ip]["_seen_case_ids"]
    assert "IR-new0001" in active_seen and "IR-new0002" in active_seen, (
        f"fresh entries were incorrectly pruned: {active_seen}"
    )
    print("  PASS: fresh _seen_case_ids entries (same-run) survived")


def test_f3_prune_is_size_only_not_shape_changing(t43):
    """The fix must not change the KEY NAME or the per-entry SHAPE of
    _seen_case_ids -- only which keys are present. This is what makes it
    safe for Tool 27 (TTL cache reader) and Tool 50 (is_tor/is_vpn/is_proxy
    cross-reference), neither of which touches _seen_case_ids at all."""
    now = datetime.now(timezone.utc)
    ip = "203.0.113.55"
    existing_corpus = {
        ip: {
            "first_seen": iso(now), "last_seen": iso(now),
            "session_count": 1, "login_success_count": 0,
            "last_session_severity": "LOW", "ttps_observed": [],
            "commands_observed": False, "malware_downloaded": False,
            "abuse_score": None, "country": None, "asn": None,
            "isp": None, "org": None, "is_tor": False,
            "is_proxy": False, "is_vpn": False, "otx_pulses": 0,
            "enriched_at": iso(now), "enrichment_ttl_days": 30,
            "_seen_case_ids": {"IR-x": iso(now - timedelta(days=10))},
        }
    }
    updated_corpus, _ = t43.build_actor_corpus([], [], existing_corpus, now)
    entry = updated_corpus[ip]
    assert "_seen_case_ids" in entry, "F3 REGRESSION: key name changed or key removed"
    assert isinstance(entry["_seen_case_ids"], dict), (
        "F3 REGRESSION: shape changed from dict to something else"
    )
    print("  PASS: _seen_case_ids key name and dict shape preserved (size-only change)")


def main():
    t43 = _load_tool43()
    tests = [
        test_f3_stale_ip_absent_from_delta_is_still_pruned,
        test_f3_prune_is_size_only_not_shape_changing,
    ]
    failures = 0
    for test in tests:
        print(f"{test.__name__} ...")
        try:
            test(t43)
        except AssertionError as e:
            failures += 1
            print(f"  FAIL: {e}")
    print()
    if failures:
        print(f"{failures}/{len(tests)} test(s) FAILED")
        sys.exit(1)
    print(f"All {len(tests)} tests PASSED")


if __name__ == "__main__":
    main()
