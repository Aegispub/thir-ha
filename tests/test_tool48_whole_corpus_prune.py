#!/usr/bin/env python3
"""
Regression test for Bundle C (F4) -- tools/48_fingerprint_corpus.py

Symmetric to tests/test_tool43_whole_corpus_prune.py: a HASSH whose key
is ABSENT from the current run's ssh_fingerprints.json input, but which
has a stale _seen_sessions sub-dict left over from a previous run, must
still be pruned by build_fingerprint_corpus().

Run directly: python3 tests/test_tool48_whole_corpus_prune.py
"""

import sys
import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path

TOOL48_PATH = Path(__file__).resolve().parent.parent / "tools" / "48_fingerprint_corpus.py"


def _load_tool48():
    spec = importlib.util.spec_from_file_location("tool48", TOOL48_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def iso(dt: datetime) -> str:
    return dt.isoformat()


def test_f4_stale_hassh_absent_from_delta_is_still_pruned(t48):
    """A HASSH with old _seen_sessions entries that does NOT appear in
    this run's ssh_fingerprints.json must still have those stale entries
    removed."""
    now = datetime.now(timezone.utc)

    absent_hassh = "aaaa1111bbbb2222cccc3333dddd4444"  # not in this run's input
    active_hassh = "eeee5555ffff6666aaaa7777bbbb8888"  # in this run's input

    existing_corpus = {
        absent_hassh: {
            "hassh": absent_hassh,
            "client_family": "known-scanner",
            "botnet_signature": None,
            "version_strings": ["SSH-2.0-libssh_0.9.6"],
            "kex_algs": "curve25519-sha256",
            "enc_algs": "aes128-ctr",
            "mac_algs": "hmac-sha2-256",
            "comp_algs": "none",
            "session_count": 3,
            "unique_ips_ever": ["198.51.100.1"],
            "unique_ip_count_ever": 1,
            "first_seen": iso(now - timedelta(days=30)),
            "last_seen": iso(now - timedelta(days=15)),
            "_seen_sessions": {
                "IR-old0001": iso(now - timedelta(days=12)),  # stale, >2d
                "IR-old0002": iso(now - timedelta(days=20)),  # stale, >2d
            },
        },
        active_hassh: {
            "hassh": active_hassh,
            "client_family": "openssh",
            "botnet_signature": None,
            "version_strings": ["SSH-2.0-OpenSSH_8.9"],
            "kex_algs": "curve25519-sha256",
            "enc_algs": "aes128-ctr",
            "mac_algs": "hmac-sha2-256",
            "comp_algs": "none",
            "session_count": 1,
            "unique_ips_ever": ["198.51.100.2"],
            "unique_ip_count_ever": 1,
            "first_seen": iso(now - timedelta(days=1)),
            "last_seen": iso(now),
            "_seen_sessions": {
                "IR-new0001": iso(now),  # fresh, must survive
            },
        },
    }

    # This run's input only contains active_hassh.
    fingerprints = [
        {
            "hassh": active_hassh,
            "client_family": "openssh",
            "sessions": ["IR-new0002"],
            "unique_ips": ["198.51.100.2"],
            "first_seen": iso(now),
            "last_seen": iso(now),
            "kex_algs": "curve25519-sha256",
            "enc_algs": "aes128-ctr",
            "mac_algs": "hmac-sha2-256",
            "comp_algs": "none",
            "version_strings": ["SSH-2.0-OpenSSH_8.9"],
        }
    ]

    updated_corpus, stats = t48.build_fingerprint_corpus(
        fingerprints, existing_corpus, now
    )

    absent_seen = updated_corpus[absent_hassh]["_seen_sessions"]
    assert absent_seen == {}, (
        f"F4 REGRESSION: absent_hassh's stale _seen_sessions entries were "
        f"not pruned even though the HASSH never appeared in this run's "
        f"input. Found: {absent_seen}"
    )
    print("  PASS: HASSH absent from current delta still had its stale _seen_sessions pruned")

    assert updated_corpus[absent_hassh]["session_count"] == 3, (
        "F4 REGRESSION: pruning _seen_sessions incorrectly altered "
        "session_count, which must remain a running total"
    )
    print("  PASS: session_count (running total) unaffected by the prune")

    active_seen = updated_corpus[active_hassh]["_seen_sessions"]
    assert "IR-new0001" in active_seen and "IR-new0002" in active_seen, (
        f"fresh entries were incorrectly pruned: {active_seen}"
    )
    print("  PASS: fresh _seen_sessions entries (same-run) survived")


def main():
    t48 = _load_tool48()
    tests = [test_f4_stale_hassh_absent_from_delta_is_still_pruned]
    failures = 0
    for test in tests:
        print(f"{test.__name__} ...")
        try:
            test(t48)
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
