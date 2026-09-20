#!/usr/bin/env python3
"""
Regression tests for Bundle A (F1 + F2) -- tools/37_alerts_live.py

Covers:
  F1 -- YARA dedup key must be order-independent (sorted family join)
  F2 -- seen_success_ips must be pruned past its 7-day window, and a
        pruned IP must correctly be re-treated as "new" on the next call
  F2 -- seen_asns must be pruned past its 180-day window, including the
        legacy bare-list/set shape upgrade path

No test framework dependency -- plain assert, __main__-invocable, matching
the repo's existing convention of no committed test harness (confirmed:
no tests/ directory, no pytest/unittest usage anywhere in tools/*.py as
of this patch). Run directly: python3 tests/test_tool37_dedup_pruning.py
"""

import sys
import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOL37_PATH = Path(__file__).resolve().parent.parent / "tools" / "37_alerts_live.py"


def _load_tool37():
    """Load tools/37_alerts_live.py as a module. Filename starts with a
    digit so it isn't importable via a normal `import` statement."""
    spec = importlib.util.spec_from_file_location("tool37", TOOL37_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def iso(dt: datetime) -> str:
    return dt.isoformat()


def test_f1_yara_key_order_independent(t37):
    """Two YARA results with the same family SET in different orders must
    produce the same title and the same alert_key hash. This is the exact
    failure mode: pre-fix, family order was preserved verbatim in the
    join, so 'Gafgyt, Rootkit' and 'Rootkit, Gafgyt' produced different
    titles and different dedup keys for what is really one alert type."""
    yara_a = {
        "results": [{
            "filename": "sample.bin",
            "severity": "HIGH",
            "classified": True,
            "families": ["Gafgyt", "Rootkit", "XMRig"],
        }]
    }
    yara_b = {
        "results": [{
            "filename": "sample.bin",
            "severity": "HIGH",
            "classified": True,
            "families": ["XMRig", "Gafgyt", "Rootkit"],  # same set, different order
        }]
    }

    alerts_a = t37.check_malware_alerts({}, yara_a)
    alerts_b = t37.check_malware_alerts({}, yara_b)

    assert len(alerts_a) == 1 and len(alerts_b) == 1, "expected exactly one alert per input"

    title_a, title_b = alerts_a[0]["title"], alerts_b[0]["title"]
    assert title_a == title_b, (
        f"F1 REGRESSION: same family set produced different titles: "
        f"{title_a!r} vs {title_b!r}"
    )

    key_a = t37.alert_key(alerts_a[0]["type"], alerts_a[0]["key_detail"])
    key_b = t37.alert_key(alerts_b[0]["type"], alerts_b[0]["key_detail"])
    assert key_a == key_b, (
        f"F1 REGRESSION: same family set produced different dedup keys: "
        f"{key_a} vs {key_b}"
    )
    print("  PASS: same family set, different order -> identical title + dedup key")


def test_f2_seen_success_ips_pruned_and_ip_becomes_new_again(t37):
    """An 8-day-old seen_success_ips entry must be removed by the prune;
    a same-day entry must survive; and a subsequent check_credential_alerts
    call must correctly re-treat the pruned IP as 'new' (i.e. fire an
    alert for it again), proving the prune doesn't just delete bytes but
    actually restores correct alerting behaviour."""
    now = datetime.now(timezone.utc)
    stale_ip = "203.0.113.9"      # 8 days old -- must be pruned
    fresh_ip = "203.0.113.10"     # same-day -- must survive

    cred_history = {
        "seen_success_ips": {
            stale_ip: iso(now - timedelta(days=8)),
            fresh_ip: iso(now),
        }
    }

    removed = t37.prune_seen_success_ips(cred_history, max_age_days=7)
    assert removed == 1, f"expected exactly 1 stale entry removed, got {removed}"

    seen = cred_history["seen_success_ips"]
    assert stale_ip not in seen, "F2 REGRESSION: 8-day-old entry survived the prune"
    assert fresh_ip in seen, "F2 REGRESSION: same-day entry was incorrectly pruned"
    print("  PASS: stale (8d) entry removed, fresh (0d) entry survived")

    # Now prove the pruned IP is correctly treated as NEW on the next run --
    # this is the actual security consequence the audit flagged: before
    # this fix, a returning attacker IP with a successful auth >7 days ago
    # would be silently suppressed forever because the stale entry never
    # left the dict for check_credential_alerts' freshness check to miss.
    cred_data = {
        "success_pairs": [
            {"src_ip": stale_ip, "username": "root", "password": "toor"},
        ]
    }
    alerts = t37.check_credential_alerts(cred_data, cred_history)
    assert len(alerts) == 1, (
        "F2 REGRESSION: pruned IP was not re-treated as new -- "
        "a genuine new-auth-success alert would be silently suppressed"
    )
    assert alerts[0]["key_detail"] == stale_ip
    print("  PASS: pruned IP correctly re-fires a new-auth-success alert")


def test_f2_seen_asns_pruned_past_180_days_and_legacy_shape_upgraded(t37):
    """seen_asns must gain a real delete path. Covers both the normal
    dict shape and the legacy bare-list shape that existed before this
    fix (no per-entry timestamp -- upgraded in place, stamped 'now', not
    deleted or backdated)."""
    now = datetime.now(timezone.utc)
    stale_asn = "AS64500"    # 200 days old -- must be pruned
    fresh_asn = "AS64501"    # 10 days old -- must survive

    asn_history = {
        "seen_asns": {
            stale_asn: iso(now - timedelta(days=200)),
            fresh_asn: iso(now - timedelta(days=10)),
        }
    }
    removed = t37.prune_seen_asns(asn_history, max_age_days=180)
    assert removed == 1, f"expected exactly 1 stale ASN removed, got {removed}"
    assert stale_asn not in asn_history["seen_asns"]
    assert fresh_asn in asn_history["seen_asns"]
    print("  PASS: stale (200d) ASN removed, fresh (10d) ASN survived")

    # Legacy shape: a bare list with no timestamps at all (the pre-fix
    # on-disk shape). Must be upgraded in place, not crash, and entries
    # must NOT be deleted on first encounter (we don't know their true
    # age, so "now" is the only non-destructive assumption).
    legacy_history = {"seen_asns": ["AS64502", "AS64503"]}
    removed_legacy = t37.prune_seen_asns(legacy_history, max_age_days=180)
    assert removed_legacy == 0, "legacy entries must not be deleted on first encounter"
    assert isinstance(legacy_history["seen_asns"], dict), (
        "F2 REGRESSION: legacy list shape was not upgraded to a timestamped dict"
    )
    assert set(legacy_history["seen_asns"].keys()) == {"AS64502", "AS64503"}
    print("  PASS: legacy bare-list seen_asns upgraded to timestamped dict without data loss")


def test_f2_prune_is_not_gated_behind_prune_days(t37):
    """Static check: the unconditional prune calls must exist in main()
    OUTSIDE the `if args.prune_days > 0:` block, at the module source
    level. This is a source-text check because it's a wiring/placement
    bug, not a pure-function bug -- the functions above could be perfectly
    correct while still being called in the wrong place."""
    src = TOOL37_PATH.read_text()

    call_idx = src.index("prune_seen_success_ips(cred_history)")
    asn_call_idx = src.index("prune_seen_asns(asn_history)")
    gate_idx = src.index("if args.prune_days > 0:")

    assert call_idx < gate_idx, (
        "F2 REGRESSION: prune_seen_success_ips() call site is not before "
        "the monthly --prune-days gate -- it would only run ~once/month"
    )
    assert asn_call_idx < gate_idx, (
        "F2 REGRESSION: prune_seen_asns() call site is not before "
        "the monthly --prune-days gate -- it would only run ~once/month"
    )
    print("  PASS: both prune calls are unconditional, ahead of the monthly gate")


def main():
    t37 = _load_tool37()
    tests = [
        test_f1_yara_key_order_independent,
        test_f2_seen_success_ips_pruned_and_ip_becomes_new_again,
        test_f2_seen_asns_pruned_past_180_days_and_legacy_shape_upgraded,
        test_f2_prune_is_not_gated_behind_prune_days,
    ]
    failures = 0
    for test in tests:
        print(f"{test.__name__} ...")
        try:
            test(t37)
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
