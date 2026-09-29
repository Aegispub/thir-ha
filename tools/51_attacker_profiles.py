#!/usr/bin/env python3
"""
Tool 51 -- Attacker Profiles

Closes the open action on Q-18 and Q-19 (docs/bloat_audit_open_questions.md)
by building a reproducible artifact instead of leaving both findings
recorded only as a byte-count audit result.

Q-18 -- Credential Replay
  A credential pair is flagged when the number of DISTINCT source IPs in
  its success_events list exceeds --credential-threshold (default 50).
  This is exactly the shape of the original finding: one credential pair,
  839 unique source IPs, over three-plus weeks -- a signature of
  credential stuffing against a known-valid credential, not organic
  discovery. Source: data/credential_corpus.json.

Q-19 -- Fingerprint Concentration
  An SSH client fingerprint (HASSH) is flagged when its cumulative
  session_count exceeds --fingerprint-threshold (default 10,000) while
  unique_ip_count_ever stays below --fingerprint-max-ips (default 10) --
  i.e. a small, fixed set of sources sustaining very high session volume
  under one client signature. Source: data/fingerprint_corpus.json.

Both thresholds are deliberately conservative defaults matched to the
finding that motivated this tool, not tuned against a larger dataset --
there is no larger dataset yet. Adjust via CLI flags as the corpus grows.

Output: data/attacker_profiles.json (machine-readable) plus a
human-readable summary printed to stdout, matching the repo's existing
tool convention (see Tool 30's stdout summary pattern).

No new dependencies. Standard library only, consistent with every other
tool in this pipeline (see docs/THIR_Domain_Reference_v1.docx Layer 3:
"Standard library only -- no pip install, no package managers").
"""

import argparse
import json
from datetime import datetime, timezone


def load_json(path: str, label: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[Tool51] WARNING: {label} not found at {path} -- skipping that source")
        return {}
    except json.JSONDecodeError as e:
        print(f"[Tool51] WARNING: {label} at {path} is not valid JSON ({e}) -- skipping")
        return {}


def find_credential_replay(corpus: dict, threshold: int) -> list:
    """Q-18. Flag credential pairs whose success_events span more distinct
    source IPs than `threshold`. Returns a list sorted by IP count,
    highest first."""
    flagged = []
    for key, entry in corpus.items():
        events = entry.get("success_events", [])
        unique_ips = {e.get("src_ip") for e in events if e.get("src_ip")}
        if len(unique_ips) > threshold:
            flagged.append({
                "corpus_key": key,
                "username": entry.get("username", ""),
                "password": entry.get("password", ""),
                "unique_source_ips": len(unique_ips),
                "total_success_events": len(events),
                "first_seen": entry.get("first_seen", ""),
                "last_seen": entry.get("last_seen", ""),
                "note": (
                    f"{len(unique_ips)} distinct source IPs successfully "
                    f"authenticated with this credential pair -- consistent "
                    f"with credential stuffing or botnet replay of a known-"
                    f"valid credential, not organic independent discovery."
                ),
            })
    flagged.sort(key=lambda x: -x["unique_source_ips"])
    return flagged


def find_fingerprint_concentration(corpus: dict, session_threshold: int,
                                     max_ips: int) -> list:
    """Q-19. Flag SSH client fingerprints with high session_count
    concentrated behind a small fixed set of source IPs. Returns a list
    sorted by session_count, highest first."""
    flagged = []
    for hassh, entry in corpus.items():
        session_count = entry.get("session_count", 0)
        ip_count = entry.get("unique_ip_count_ever", 0)
        if session_count > session_threshold and 0 < ip_count <= max_ips:
            flagged.append({
                "hassh": hassh,
                "client_family": entry.get("client_family", ""),
                "botnet_signature": entry.get("botnet_signature", ""),
                "version_strings": entry.get("version_strings", []),
                "session_count": session_count,
                "unique_ip_count_ever": ip_count,
                "sessions_per_ip": round(session_count / ip_count, 1) if ip_count else None,
                "first_seen": entry.get("first_seen", ""),
                "last_seen": entry.get("last_seen", ""),
                "note": (
                    f"{session_count} cumulative sessions from only "
                    f"{ip_count} distinct source IP(s) sharing one SSH "
                    f"client fingerprint -- a small, fixed, sustained "
                    f"source set, not broad opportunistic scanning."
                ),
            })
    flagged.sort(key=lambda x: -x["session_count"])
    return flagged


def build_output(credential_flags: list, fingerprint_flags: list,
                  credential_threshold: int, fingerprint_threshold: int,
                  fingerprint_max_ips: int) -> dict:
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "thresholds": {
            "credential_replay_min_unique_ips": credential_threshold,
            "fingerprint_concentration_min_sessions": fingerprint_threshold,
            "fingerprint_concentration_max_ips": fingerprint_max_ips,
        },
        "credential_replay": {
            "description": "Q-18 -- credential pairs replayed from an unusually large set of distinct source IPs",
            "flagged_count": len(credential_flags),
            "entries": credential_flags,
        },
        "fingerprint_concentration": {
            "description": "Q-19 -- SSH client fingerprints with high session volume from a small fixed source set",
            "flagged_count": len(fingerprint_flags),
            "entries": fingerprint_flags,
        },
    }


def print_summary(output: dict) -> None:
    cred = output["credential_replay"]
    fp = output["fingerprint_concentration"]
    print(f"[Tool51] Credential replay (Q-18): {cred['flagged_count']} flagged")
    for e in cred["entries"][:5]:
        print(f"[Tool51]   {e['unique_source_ips']} IPs -> "
              f"{e['username']}/{e['password']} "
              f"({e['total_success_events']} events, "
              f"{e['first_seen']} .. {e['last_seen']})")
    print(f"[Tool51] Fingerprint concentration (Q-19): {fp['flagged_count']} flagged")
    for e in fp["entries"][:5]:
        print(f"[Tool51]   {e['session_count']} sessions / {e['unique_ip_count_ever']} IPs "
              f"({e['sessions_per_ip']}/IP) -> {e['hassh'][:16]}... "
              f"[{e['client_family']}, {e['botnet_signature']}]")
    print(f"[Tool51] Done -- {cred['flagged_count'] + fp['flagged_count']} total finding(s) surfaced")


def main():
    parser = argparse.ArgumentParser(description="Tool 51 -- Attacker Profiles (Q-18 / Q-19)")
    parser.add_argument("--credential-corpus", default="data/credential_corpus.json",
                         help="Path to credential_corpus.json")
    parser.add_argument("--fingerprint-corpus", default="data/fingerprint_corpus.json",
                         help="Path to fingerprint_corpus.json")
    parser.add_argument("--output", default="data/attacker_profiles.json",
                         help="Output path")
    parser.add_argument("--credential-threshold", type=int, default=50,
                         help="Flag a credential pair when distinct source IPs exceed this")
    parser.add_argument("--fingerprint-threshold", type=int, default=10000,
                         help="Flag a fingerprint when cumulative session_count exceeds this")
    parser.add_argument("--fingerprint-max-ips", type=int, default=10,
                         help="...and unique_ip_count_ever is at or below this")
    args = parser.parse_args()

    cred_corpus = load_json(args.credential_corpus, "credential_corpus.json")
    fp_corpus = load_json(args.fingerprint_corpus, "fingerprint_corpus.json")

    credential_flags = find_credential_replay(cred_corpus, args.credential_threshold)
    fingerprint_flags = find_fingerprint_concentration(
        fp_corpus, args.fingerprint_threshold, args.fingerprint_max_ips
    )

    output = build_output(
        credential_flags, fingerprint_flags,
        args.credential_threshold, args.fingerprint_threshold, args.fingerprint_max_ips,
    )

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print_summary(output)
    print(f"[Tool51] Written -> {args.output}")


if __name__ == "__main__":
    main()
