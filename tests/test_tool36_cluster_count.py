#!/usr/bin/env python3
"""
Regression test for Q-21 -- tools/36_command_clustering_live.py

F5 (Q-16/Q-20) writes a per-case `session_count` field on consolidated
`ir_cases.json` entries. Tool 36 originally computed each cluster's
`session_count` as len(cl["members"]) -- a count of CASES, not of the raw
sessions those cases represent. Post-F5, a single consolidated case can
stand in for hundreds or thousands of raw sessions, so counting cases
silently collapsed cluster volume (confirmed on the live corpus: the
CLU-013 flood cluster dropped from 1,809 to 4 when measured this way).

Fix has two parts, both required:
  1. extract_command_sessions() must carry case.get("session_count", 1)
     onto each session dict -- without this, cl["members"] entries never
     have the field and any later `.get("session_count", 1)` silently
     no-ops to the default.
  2. build_output() must sum member session_count, not count members.

This test exercises the real public pipeline (extract_command_sessions ->
cluster_sessions -> build_output), not a private helper, so it fails if
either half of the fix is reverted independently.

No test framework dependency -- plain assert, __main__-invocable, matching
the repo's existing convention. Filename starts with a digit
(36_command_clustering_live.py) so it is loaded via
importlib.util.spec_from_file_location, same pattern as the other test
files in this directory.
Run directly: python3 tests/test_tool36_cluster_count.py
"""

import importlib.util
from pathlib import Path

TOOL36_PATH = Path(__file__).resolve().parent.parent / "tools" / "36_command_clustering_live.py"


def _load_tool36():
    spec = importlib.util.spec_from_file_location("tool36", TOOL36_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _case(case_id, src_ip, cmds, session_count=None, ts="2026-09-24T12:00:00.000000Z"):
    c = {
        "case_id": case_id,
        "src_ip": src_ip,
        "commands": cmds,
        "first_seen": ts,
        "timestamp": ts,
    }
    if session_count is not None:
        c["session_count"] = session_count
    return c


def test_pre_f5_cases_unaffected(t36):
    """Cases with no session_count field (pre-F5 shape) must behave exactly
    as before the fix: cluster session_count equals the number of member
    cases, since each contributes the .get(..., 1) default of 1."""
    cases = [
        _case("a", "1.2.3.4", ["uname -a"]),
        _case("b", "1.2.3.4", ["uname -a"]),
        _case("c", "1.2.3.4", ["uname -a"]),
    ]
    sessions = t36.extract_command_sessions(cases)
    clusters = t36.cluster_sessions(sessions, similarity_threshold=0.7)
    out = t36.build_output(clusters, total_sessions=len(sessions))
    assert len(out["clusters"]) == 1
    assert out["clusters"][0]["session_count"] == 3


def test_consolidated_cases_weighted_not_counted(t36):
    """The core Q-21 fix: a cluster with mixed singleton and F5-consolidated
    members must SUM session_count, not count members. Three cases, one of
    which represents 500 raw sessions, must report 502 -- not 3."""
    cases = [
        _case("a", "1.2.3.4", ["uname -a"], session_count=1),
        _case("b", "1.2.3.4", ["uname -a"], session_count=500),
        _case("c", "1.2.3.4", ["uname -a"], session_count=1),
    ]
    sessions = t36.extract_command_sessions(cases)
    clusters = t36.cluster_sessions(sessions, similarity_threshold=0.7)
    out = t36.build_output(clusters, total_sessions=len(sessions))
    assert len(out["clusters"]) == 1
    assert out["clusters"][0]["session_count"] == 502, (
        f"expected 502 (1+500+1), got {out['clusters'][0]['session_count']} "
        "-- if this is 3, extract_command_sessions() is not carrying "
        "session_count through and the sum is degenerating to a count"
    )


def test_extraction_carries_session_count_field(t36):
    """Isolates fix-part 1: extract_command_sessions() must place
    session_count on the session dict itself, independent of clustering."""
    cases = [_case("a", "1.2.3.4", ["uname -a"], session_count=42)]
    sessions = t36.extract_command_sessions(cases)
    assert sessions[0].get("session_count") == 42


def test_extraction_defaults_missing_session_count_to_one(t36):
    """A case with no session_count key must extract as 1, not crash and
    not silently vanish -- this is the pre-F5 compatibility path."""
    cases = [_case("a", "1.2.3.4", ["uname -a"])]  # no session_count arg
    sessions = t36.extract_command_sessions(cases)
    assert sessions[0].get("session_count", 1) == 1


def test_singleton_and_consolidated_mixed_across_two_clusters(t36):
    """Two distinct command signatures -> two clusters, each summing only
    its own members' session_count. Confirms the fix doesn't leak weight
    across clusters."""
    cases = [
        _case("a", "1.2.3.4", ["uname -a"], session_count=100),
        _case("b", "5.6.7.8", ["whoami"], session_count=200),
    ]
    sessions = t36.extract_command_sessions(cases)
    clusters = t36.cluster_sessions(sessions, similarity_threshold=0.9)
    out = t36.build_output(clusters, total_sessions=len(sessions))
    assert len(out["clusters"]) == 2
    counts = sorted(c["session_count"] for c in out["clusters"])
    assert counts == [100, 200]


def run_all():
    t36 = _load_tool36()
    tests = [
        test_pre_f5_cases_unaffected,
        test_consolidated_cases_weighted_not_counted,
        test_extraction_carries_session_count_field,
        test_extraction_defaults_missing_session_count_to_one,
        test_singleton_and_consolidated_mixed_across_two_clusters,
    ]
    passed = 0
    for fn in tests:
        fn(t36)
        passed += 1
        print(f"  PASS  {fn.__name__}")
    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_all()
