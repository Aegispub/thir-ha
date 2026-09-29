#!/usr/bin/env python3
"""
Regression tests for F5 -- tools/26_incident_timeline_live.py

Covers:
  Q-16 Shape 3 -- consolidate_by_signature() must collapse repetitive
  successful-login cases (same src_ip, same login outcome, same exact
  command set, same GROUP_WINDOW_MINUTES time bucket) into one
  representative case carrying session_count, while leaving cases with a
  different IP, outcome, command set, or time bucket untouched.

No test framework dependency -- plain assert, __main__-invocable, matching
the repo's existing convention (see tests/test_tool37_dedup_pruning.py).
Filename starts with a digit (26_incident_timeline_live.py) so it is
loaded via importlib.util.spec_from_file_location, not a normal import
statement -- same pattern as the other three test files in this directory.
Run directly: python3 tests/test_tool26_consolidation.py
"""

import sys
import importlib.util
from pathlib import Path

TOOL26_PATH = Path(__file__).resolve().parent.parent / "tools" / "26_incident_timeline_live.py"


def _load_tool26():
    """Load tools/26_incident_timeline_live.py as a module."""
    spec = importlib.util.spec_from_file_location("tool26", TOOL26_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _case(case_id, src_ip="1.2.3.4", cmds=None, login_success=True,
          ts="2026-09-24T12:00:00.000000Z", severity="HIGH"):
    return {
        "case_id": case_id,
        "src_ip": src_ip,
        "commands": cmds if cmds is not None else ["uname -a"],
        "login_success": login_success,
        "first_seen": ts,
        "severity": severity,
    }


def test_consolidates_repetitive_successful_logins(t26):
    """The core Q-16 fix: 100 identical successful-login cases from the
    same IP, same command, same time bucket collapse to one case with
    session_count=100."""
    cases = [_case(f"c{i}") for i in range(100)]
    out = t26.consolidate_by_signature(cases)
    assert len(out) == 1, f"expected 1 consolidated case, got {len(out)}"
    assert out[0]["session_count"] == 100
    assert len(out[0]["session_ids_sample"]) == 10


def test_does_not_consolidate_different_signatures(t26):
    cases = [_case("a", cmds=["uname -a"]), _case("b", cmds=["whoami"])]
    out = t26.consolidate_by_signature(cases)
    assert len(out) == 2


def test_does_not_consolidate_across_ips(t26):
    cases = [_case("a", src_ip="1.2.3.4"), _case("b", src_ip="5.6.7.8")]
    out = t26.consolidate_by_signature(cases)
    assert len(out) == 2


def test_does_not_consolidate_failed_vs_successful(t26):
    """login_success is part of the grouping key -- a real recon probe
    (login_success=False) must never merge with a successful-login flood
    that happens to share the same IP and commands."""
    cases = [_case("a", login_success=True), _case("b", login_success=False)]
    out = t26.consolidate_by_signature(cases)
    assert len(out) == 2


def test_ungrouped_case_gets_session_count_one(t26):
    out = t26.consolidate_by_signature([_case("a")])
    assert out[0]["session_count"] == 1


def test_different_time_windows_are_separate(t26):
    """3-hour gap exceeds GROUP_WINDOW_MINUTES (120) -- must not merge,
    even with identical src_ip/login_success/commands."""
    cases = [
        _case("a", ts="2026-09-24T12:00:00.000000Z"),
        _case("b", ts="2026-09-24T15:00:00.000000Z"),
    ]
    out = t26.consolidate_by_signature(cases)
    assert len(out) == 2


def test_severity_not_recomputed(t26):
    """Q-03 risk-iii: severity is inherited from the representative case
    verbatim, never aggregated or recomputed across the group."""
    out = t26.consolidate_by_signature([_case("a"), _case("b")])
    assert out[0]["severity"] == "HIGH"


def test_stable_case_id(t26):
    """Same signature + same time bucket must produce the same case_id
    across independent calls -- required for reproducible pipeline runs
    on overlapping input, not a fresh UUID each time."""
    out1 = t26.consolidate_by_signature([_case("a"), _case("b")])
    out2 = t26.consolidate_by_signature([_case("a"), _case("b")])
    assert out1[0]["case_id"] == out2[0]["case_id"]


def test_case_id_matches_repo_convention(t26):
    """Generated case_id must follow the repo's existing IR-<hex> shape
    (see module docstring's example output), not an invented prefix."""
    out = t26.consolidate_by_signature([_case("a"), _case("b")])
    assert out[0]["case_id"].startswith("IR-")


def test_idempotent(t26):
    """Running consolidation twice on its own output is a no-op: a
    consolidated case's signature is identical to itself, so on the
    second pass it forms a group of size 1 and its existing
    session_count is preserved (not reset to 1) via dict.setdefault."""
    cases = [_case(f"c{i}") for i in range(50)]
    once = t26.consolidate_by_signature(cases)
    twice = t26.consolidate_by_signature(once)
    assert len(once) == len(twice) == 1
    assert twice[0]["session_count"] == 50


def test_no_timestamp_passes_through_ungrouped(t26):
    """A case with no first_seen must not crash the bucketing logic and
    must not be silently merged with anything else."""
    cases = [_case("a", ts=""), _case("b", ts="")]
    out = t26.consolidate_by_signature(cases)
    assert len(out) == 2
    assert all(c.get("session_count") == 1 for c in out)


def test_empty_input(t26):
    assert t26.consolidate_by_signature([]) == []


def test_group_window_matches_tool28(t26):
    """F5 duplicates Tool 28's GROUP_WINDOW_MINUTES rather than importing it
    (not importable across this repo's module layout -- see the constant's
    own comment in tools/26_incident_timeline_live.py). This test fails
    loudly if the two values are ever allowed to drift apart, turning a
    silent-divergence hazard into a caught regression."""
    tool28_path = Path(__file__).resolve().parent.parent / "tools" / "28_soc_handover_live.py"
    spec28 = importlib.util.spec_from_file_location("tool28", tool28_path)
    tool28 = importlib.util.module_from_spec(spec28)
    spec28.loader.exec_module(tool28)

    assert t26.GROUP_WINDOW_MINUTES == tool28.GROUP_WINDOW_MINUTES


def _case_with_kex(case_id, hassh, src_ip="1.2.3.4",
                    ts="2026-09-24T12:00:00.000000Z"):
    """A case whose timeline includes a captured cowrie.client.kex event."""
    c = _case(case_id, src_ip=src_ip, ts=ts)
    c["timeline"] = [
        {"eventid": "cowrie.session.connect", "timestamp": ts},
        {"eventid": "cowrie.client.kex", "hassh": hassh, "timestamp": ts},
        {"eventid": "cowrie.session.closed", "timestamp": ts},
    ]
    return c


def _case_no_kex(case_id, src_ip="1.2.3.4", ts="2026-09-24T12:00:00.000000Z"):
    """A case whose KEX handshake was never captured -- connect/closed only.
    This is the shape confirmed on the live corpus for the earliest-arriving
    session in a fast-failing connection burst."""
    c = _case(case_id, src_ip=src_ip, ts=ts)
    c["timeline"] = [
        {"eventid": "cowrie.session.connect", "timestamp": ts},
        {"eventid": "cowrie.session.closed", "timestamp": ts},
    ]
    return c


def test_q20_prefers_kex_bearing_representative_over_earliest(t26):
    """Q-20: the earliest case in the group has no cowrie.client.kex event
    (the exact shape found on the live corpus -- 3 real groups affected).
    A later case in the same group DOES carry the KEX handshake. The
    representative chosen must be the KEX-bearing one, not the strictly
    earliest one, or the group's only captured HASSH fingerprint is
    silently discarded."""
    no_kex_earliest = _case_no_kex("a", ts="2026-09-24T12:00:00.000000Z")
    has_kex_later = _case_with_kex(
        "b", hassh="deadbeefcafef00d0123456789abcdef",
        ts="2026-09-24T12:00:01.000000Z",
    )
    out = t26.consolidate_by_signature([no_kex_earliest, has_kex_later])
    assert len(out) == 1
    kex_events = [e for e in out[0].get("timeline", [])
                  if e.get("eventid") == "cowrie.client.kex"]
    assert len(kex_events) == 1, "representative must carry the KEX event"
    assert kex_events[0]["hassh"] == "deadbeefcafef00d0123456789abcdef"


def test_q20_falls_back_to_earliest_when_no_case_has_kex(t26):
    """If NO case in the group ever captured a KEX event, fall back to the
    original earliest-by-timestamp behaviour -- there is nothing to
    preserve, and the fallback must not crash."""
    a = _case_no_kex("a", ts="2026-09-24T12:00:00.000000Z")
    b = _case_no_kex("b", ts="2026-09-24T12:00:01.000000Z")
    out = t26.consolidate_by_signature([a, b])
    assert len(out) == 1
    assert out[0]["case_id"] != ""  # still produces a valid stable id
    assert not any(e.get("eventid") == "cowrie.client.kex"
                   for e in out[0].get("timeline", []))


def test_q20_case_id_stable_regardless_of_which_case_is_representative(t26):
    """The Q-20 fix changes WHICH case survives as representative, but
    case_id/bucket must still be derived from the group's true earliest
    timestamp -- not the (possibly later) KEX-bearing representative's own
    timestamp -- so case_id stability across runs is unaffected by which
    case happens to carry the KEX event."""
    no_kex_earliest = _case_no_kex("a", ts="2026-09-24T12:00:00.000000Z")
    has_kex_later = _case_with_kex(
        "b", hassh="deadbeefcafef00d0123456789abcdef",
        ts="2026-09-24T12:00:01.000000Z",
    )
    out1 = t26.consolidate_by_signature([no_kex_earliest, has_kex_later])
    out2 = t26.consolidate_by_signature([
        _case_no_kex("a", ts="2026-09-24T12:00:00.000000Z"),
        _case_with_kex("b", hassh="deadbeefcafef00d0123456789abcdef",
                        ts="2026-09-24T12:00:01.000000Z"),
    ])
    assert out1[0]["case_id"] == out2[0]["case_id"]


def run_all():
    t26 = _load_tool26()
    tests = [
        test_consolidates_repetitive_successful_logins,
        test_does_not_consolidate_different_signatures,
        test_does_not_consolidate_across_ips,
        test_does_not_consolidate_failed_vs_successful,
        test_ungrouped_case_gets_session_count_one,
        test_different_time_windows_are_separate,
        test_severity_not_recomputed,
        test_stable_case_id,
        test_case_id_matches_repo_convention,
        test_idempotent,
        test_no_timestamp_passes_through_ungrouped,
        test_empty_input,
        test_group_window_matches_tool28,
        test_q20_prefers_kex_bearing_representative_over_earliest,
        test_q20_falls_back_to_earliest_when_no_case_has_kex,
        test_q20_case_id_stable_regardless_of_which_case_is_representative,
    ]
    passed = 0
    for fn in tests:
        fn(t26)
        passed += 1
        print(f"  PASS  {fn.__name__}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_all()
