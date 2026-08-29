# Enriched Corpus — Schema Reconciliation
*Compiled against `thir-ha` oracle-ha branch, live data 2026-08-21. 1035 ir_cases, 74 unique IPs today.*

This is the implementation contract. Where the design doc (`THIR_HA_Enriched_Pipeline_Review_v1`) assumed a field that doesn't exist, the derivation logic required is specified. Build against this document, not Section 3/4 of the original review directly.

---

## 1. Actor Corpus — source: `ir_cases.json` + `threat_ips.json`

| Design doc field | Real source | Status | Derivation needed |
|---|---|---|---|
| `first_seen` (per IP, cross-run) | `ir_cases[].first_seen` (per case) | MISMATCH | New accumulation: `min(first_seen)` across all cases for that IP, across all runs — persisted in corpus, not recomputed from a single run |
| `last_seen` (per IP, cross-run) | `ir_cases[].last_seen` (per case) | MISMATCH | New accumulation: `max(last_seen)` across all cases for that IP, across all runs |
| `session_count` (cross-run) | Not present per-IP anywhere; per-run counts exist in `ssh_fingerprints.json` and `command_clusters.json` but scoped to fingerprint/cluster, not IP | MISMATCH | New accumulation: increment a persisted counter per IP each time that IP appears in a new `case_id` not previously seen |
| `login_success_count` | Does not exist. Real fields: `ir_cases[].login_attempts` (int) + `ir_cases[].login_success` (bool) | MISMATCH | Derive per case: `1 if login_success else 0`, sum across all cases for that IP, accumulate cross-run |
| `last_session_severity` | `ir_cases[].severity` (present, e.g. `"HIGH"`) | MATCH | Direct copy from most recent case by timestamp |
| `ttps_observed` (union, cross-run) | `ir_cases[].ttps` — flat list of TTP ID strings, e.g. `["T1078","T1592"]` | PARTIAL MATCH | Field exists per-case; union-across-runs accumulation logic does not exist and must be built |
| `commands_observed` (bool) | Does not exist as bool. Real field: `ir_cases[].commands` — a list, e.g. `["uname -s -v -n -r -m"]`, empty list `[]` when none | MISMATCH | Derive: `len(commands) > 0` |
| `malware_downloaded` (bool) | Does not exist as bool. Real field: `ir_cases[].downloads` — a list, empty `[]` when none | MISMATCH | Derive: `len(downloads) > 0` |
| `abuse_score` | `threat_ips[].abuse_score` (int, e.g. `5`) | MATCH | Direct copy |
| `country` / `asn` / `isp` / `org` | `threat_ips[].country`, `.asn`, `.isp`, `.org` — all present and correctly named | MATCH | Direct copy |
| `is_tor` / `is_proxy` / `is_vpn` | `threat_ips[].is_tor`, `.is_proxy`, `.is_vpn` — all present as booleans | MATCH | Direct copy |
| `otx_pulses` | `threat_ips[].otx_pulses` (int) | MATCH | Direct copy |
| `enriched_at` | Not currently written anywhere — `threat_ips.json` has `last_seen` (enrichment timestamp of the *run*, not per-IP TTL tracking) | NEW | Must be added when the cache/TTL layer is built in Tool 27 — doesn't exist today at all, confirmed in prior session |
| `enrichment_ttl_days` | N/A — config value, not a data field | NEW | Introduced by the corpus build itself; no prior art |

**Net assessment:** the reputation half (`threat_ips.json` → `abuse_score`/`country`/`asn`/`is_tor` etc.) matches the design doc closely — near copy-paste. The behavioral half (`ir_cases.json` → everything about sessions/logins/commands) requires real derivation logic that the design doc assumed was already shaped as booleans/counts. It isn't. Every accumulation field (`first_seen`, `last_seen`, `session_count`, `ttps_observed` union) has **zero prior art** — nothing in the current 40 tools does cross-run persistence except `alert_history.json`'s dedup pattern, which the original design doc cites correctly as the template.

---

## 2. Campaign Corpus — source: `command_clusters.json`

| Design doc field | Real source | Status |
|---|---|---|
| `sequence_hash` (natural key) | `clusters[].sequence_hash`, e.g. `"d2ac04915390abe8"` | MATCH |
| Cluster identity | `clusters[].cluster_id` (e.g. `"CLU-001"`), `.campaign_name`, `.campaign_severity`, `.campaign_description` | MATCH — richer than the design doc assumed, includes `matched_campaigns[]` with `pattern_hits`/`pattern_total` fidelity scoring not mentioned in the design doc at all |
| `session_count` | `clusters[].session_count` (e.g. `51`) | MATCH |
| IP participation | `clusters[].unique_ips`, `.unique_ip_count` | MATCH |
| TTP combination | `clusters[].ttps` — list of `{id, name}` objects | MATCH, though note: some `name` values are just the ID repeated (e.g. `{"id":"T1078","name":"T1078"}`) — a data quality gap in Tool 36 itself, unrelated to corpus build but will surface in `campaign_highlights.json` "top TTP combinations" if not filtered |

**Net assessment:** best-aligned source in the whole set. `sequence_hash` exists exactly as assumed. Only new work is the cross-run tracking (when did this campaign start, is it still active, when did it go quiet) — same category of net-new accumulation as the Actor Corpus, no prior art.

---

## 3. Credential Corpus — source: `credentials.json`

| Design doc field | Real source | Status |
|---|---|---|
| `SHA256(username\|password)` (natural key) | Not present — real structure is `top_pairs[]` with `{username, password, count}` and separate `success_pairs[]` with `{username, password, src_ip, timestamp}` | NEW — key must be computed, doesn't exist in source |
| Pair accumulation | `top_pairs[].count` is a per-run count, not cross-run | MISMATCH | Cross-run accumulation needed, same pattern as above |
| Spray pattern data | `top_usernames`, `top_passwords`, `unique_pairs`, `unique_usernames`, `unique_passwords` all present at top level | MATCH — good aggregate data already computed per-run, just needs cross-run diffing (new pairs this month vs last) |

**Net assessment:** straightforward — compute `SHA256(username|password)` as the key at ingestion, everything else is standard accumulation. Design doc's approach holds up.

---

## 4. Fingerprint Corpus — source: `ssh_fingerprints.json`

| Design doc field | Real source | Status |
|---|---|---|
| HASSH (natural key) | `fingerprints[].hassh` (e.g. `"0a07365cc01fa9fc82608ba4019af499"`) | MATCH |
| Client family / botnet signature | `fingerprints[].client_family`, `.botnet_signature` | MATCH — already resolved to human labels (`"Go SSH scanner"`, `"Generic scanner"`) |
| `session_count` | `fingerprints[].session_count` (e.g. `850`) — per-run | MATCH format, cross-run accumulation still new |
| Session linkage | `fingerprints[].sessions[]` — list of actual `case_id` strings (`"IR-17921542c4b9"`, etc.) | BETTER than design doc assumed — gives a direct join key back to `ir_cases.json` for free |

**Net assessment:** second-best-aligned source. Design doc's key assumption (HASSH) is exactly right. The `sessions[]` array is a bonus not mentioned in the design doc — useful for the eventual Evidence Graph (Tool 50).

---

## 5. Malware Corpus — source: `malware_report.json` + `yara_matches.json`

| Design doc field | Real source | Status |
|---|---|---|
| SHA256 (natural key) | `samples[].sha256` | MATCH |
| Threat scoring | `samples[].threat_score` (0–100), `.severity` | MATCH |
| ELF arch | `samples[].elf_arch` — present, `null` when not applicable (e.g. Python scripts) | MATCH |
| VirusTotal data | `samples[].virustotal.{found, malicious, suspicious, harmless, undetected, total, names}` | MATCH — richer than design doc described, includes engine consensus and sample aliasing (`names[]`) |
| Suspicious indicators | `samples[].suspicious_indicators[]` — `{indicator, match}` pairs | MATCH, more detail than assumed |
| YARA family | Separate file `yara_matches.json`, top-level: `families_detected`, `severity_summary`, `critical_samples`, `results[]` | MATCH structurally, not yet sampled at the individual-result level |

**Net assessment:** well-aligned, richest schema of the six. SHA256 vault concept holds up directly.

---

## 6. Infrastructure Corpus — source: `asn_clusters.json`

| Design doc field | Real source | Status |
|---|---|---|
| ASN (natural key) | `clusters[].asn` (e.g. `"AS9498"`) | MATCH |
| Risk data | `.avg_abuse_score`, `.max_abuse_score`, `.risk_tier`, `.tags` | MATCH |
| Anonymous infra flags | `.tor_count`, `.proxy_count`, `.vpn_count`, `.anon_count` | MATCH |
| `first_seen` / `last_seen` | Present per-cluster **already** — `.first_seen`, `.last_seen` | MATCH — but currently these are *per-run* timestamps (both showed same-day values in the sample), not accumulated across months. Cross-run accumulation still needed despite fields existing with the right names. |

**Net assessment:** best surface-level match of all six (field names are literally identical to the design doc), but the `first_seen`/`last_seen` values are deceptive — they look like they're already doing the cross-run job the corpus needs, but they're actually reset/recomputed every 2h run. Worth flagging specifically so nobody assumes this one needs less work than it does.

---

## Cross-cutting finding

**Every corpus needs the same net-new capability: cross-run persistence and accumulation.** Six different source files, six different natural keys, but one identical missing primitive underneath all of them. Only `alert_history.json` currently does this anywhere in the codebase (confirmed: hash-keyed dedup, accumulates forever). That one existing pattern is the actual template to generalize — not six separate accumulation implementations.

**Scale check for engineering estimates:** live data today shows 1035 ir_cases from 74 unique IPs in a single day. At that rate the Actor Corpus alone would carry meaningful cross-run state within the first week — worth load-testing the JSON file size/git diff size early rather than assuming it stays small.
