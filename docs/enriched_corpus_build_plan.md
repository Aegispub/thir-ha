# Enriched Corpus — Build Plan (Steps 3–5)
*Follows `enriched_corpus_schema_reconciliation.md` (Step 1–2). Grounded in live repo state, 2026-08-21.*

---

## Step 3 — Accumulation risk classification

### The template already exists and is load-tested

`data/alert_history.json` is the one file in the entire pipeline that already does cross-run, hash-keyed, forever-accumulating state — exactly the pattern all six corpora need. It is **2.38MB today**, accumulated since March 2026 (per its own `last_fired` timestamps spanning March–June), from alert dedup alone — a much lower-cardinality dataset than IP-level or session-level accumulation will be.

This is a real, measured data point, not a guess: `ir_cases.json` itself is already 5.79MB *today's data only* (1035 cases). The Actor Corpus's `enriched_corpus.json`, accumulating per-IP state indefinitely, will grow faster than `alert_history.json` did, because IP cardinality (74 unique today) compounds every day whereas alert hashes plateau once known threat patterns are seen once.

**Concrete implication for Step 5 below:** the pruning lifecycle (Section 5 of the original design doc — monthly R2 snapshot, git keeps current month only) is not a nice-to-have, it's load-bearing from day one. Skipping it even temporarily during initial build/testing risks a multi-MB commit within the first week.

### Classification: zero prior art vs. partial prior art

| Corpus | Prior art | Real risk |
|---|---|---|
| **Actor** | Zero — `first_seen`/`last_seen`/`session_count`/`ttps_observed` per IP across runs does not exist anywhere | HIGH — foundational, everything else depends on it (per design doc Section 9), and has the most schema mismatches (Step 1) |
| **Campaign** | Zero cross-run, but `sequence_hash` key and per-run cluster data already well-formed | MEDIUM — key derivation already solved, only the accumulation wrapper is new |
| **Credential** | Zero cross-run, key must be computed (SHA256 doesn't exist yet) | MEDIUM — same shape as Campaign |
| **Fingerprint** | Zero cross-run, but HASSH key exists and `sessions[]` already links back to `ir_cases.json` | LOW-MEDIUM — best raw material of the six |
| **Malware** | Zero cross-run, SHA256 key exists, richest schema already | LOW-MEDIUM — straightforward vault, low ambiguity |
| **Infrastructure** | Zero cross-run *despite* `first_seen`/`last_seen` field names existing — genuine trap (Step 1 finding) | MEDIUM — the deceptive part is realizing existing fields don't already solve this |

**Ranking by build risk, highest first: Actor > Campaign ≈ Credential ≈ Infrastructure > Fingerprint ≈ Malware.**

This inverts the design doc's Section 9 dependency ordering slightly — Section 9 lists Actor Corpus as feeding Tools 43/49 and therefore foundational by *consumption* order, which is still correct. But by *build risk*, Actor Corpus is also the hardest one to get right, which is exactly why it should be the PoC target (Step 4) rather than deferred.

---

## Step 4 — Proof-of-concept: Actor Corpus only

Build one corpus, end to end, before touching the other five or writing `enriched_corpus.yml` as a scheduled workflow.

### Scope

- New file: `data/enriched_corpus.json` — the vault, keyed by IP
- Reads: current `data/ir_cases.json` + `data/threat_ips.json` only
- Writes: `enriched_corpus.json` (full) + `enriched-data/enriched_highlights.json` (counts-only, per Section 7's no-raw-IP rule)
- **No workflow file yet.** Run it manually, once, against today's real `ir_cases.json`/`threat_ips.json` as a script — not scheduled, not committed to `.github/workflows/`.

### What the PoC needs to prove, specifically

1. **The derivation logic from Step 1 is correct** — run it against the real 1035 cases / 74 IPs and manually spot-check 3–5 IPs: does `session_count` match a manual `grep -c` of that IP in `ir_cases.json`? Does `ttps_observed` union correctly?
2. **The TTL/cache-check logic works** — this is also the Tool 27 quota-relief patch discussed earlier. Building it as part of the Actor Corpus PoC kills two birds: the corpus needs `enriched_at`/TTL tracking anyway (Step 1 finding — this field doesn't exist yet), and that's the same mechanism that solves the AbuseIPDB rate-limit problem. Confirm: on a second manual run, are previously-enriched IPs correctly skipped?
3. **File size trajectory is sane** — after one run, check `enriched_corpus.json` size. Extrapolate: at 74 new IPs/day (today's rate), what does 30 days look like before the first monthly prune? This validates or invalidates the urgency flagged in Step 3.
4. **The `.EOF`/sentinel pattern from Tool 32 is reusable** — the design doc's Section 5.1 monthly pruning sequence explicitly says to reuse Tool 32's existing weekly/monthly sentinel pattern. Confirm that pattern is copy-pasteable rather than assumed compatible.

### Explicit non-goals for the PoC

- Not building Campaign/Credential/Fingerprint/Malware/Infrastructure corpora yet
- Not writing `enriched_corpus.yml` as a scheduled GitHub Actions workflow yet
- Not touching Tool 27's *production* code path yet — the TTL/cache logic gets validated standalone first, then merged into `27_threat_intel_feeder_live.go` once proven

### Exit criteria to move past PoC

- Actor Corpus schema matches Step 1's reconciled field list, not the original design doc's assumed fields
- One real re-run demonstrates cache-hit skipping (proving the rate-limit fix works)
- File size after one run, projected to 30 days, is within a range that makes git-native storage viable for that period (if not, the pruning cadence needs to be more aggressive than monthly, and that's a Step-4 finding, not a Step-5 surprise)

---

## Step 5 — Coding debt, sequenced against the corpus build

These are the smaller open items from the Strategic Review, explicitly ordered by whether they block, parallelize with, or follow the corpus PoC.

### Fully parallel — no dependency either direction, do anytime

- **Cron path bug confirmation** (`sync_to_r2.sh` path fix) — live-VM state, unrelated to corpus work, already has a documented fix in the `#Update` section of the strategic doc. Just needs confirmation it was applied.
- **Watermark-vs-resync race condition documentation** — ARCHITECTURE.md note only, no code change, doesn't touch corpus files.
- **Tool 39 first-live-run verification** — failover-specific, orthogonal to corpus/IP-enrichment work entirely.

### Should happen before Actor Corpus PoC, not after

- **None identified.** Everything else in the debt list (DEBT-1 runbooks, HAProxy pollution fix) was already confirmed resolved in the live repo in the prior session. No remaining blocker sits between "now" and starting the Step 4 PoC.

### Should happen after Actor Corpus PoC succeeds, before full six-corpus build

- **Tool 27 production merge** — once the TTL/cache logic is validated standalone in the PoC, merge it into the real `27_threat_intel_feeder_live.go` and let it run in `pipeline.yml` for a few real cycles before building the other five corpora on top of it. This de-risks the foundation before adding load.
- **File-size/pruning cadence decision** — informed directly by the PoC's exit criteria above. If monthly pruning proves too slow given real growth rate, this needs to be decided before Campaign/Credential/etc. are built, not discovered after all six are live and git is already bloated.

---

## Summary — what this sequence buys you

Instead of building six corpora and a new scheduled workflow simultaneously against a design doc with unverified field-name assumptions, this plan:

1. Fixes the schema mismatches once, in writing, before any code (done — Step 1)
2. Identifies that the real engineering risk is concentrated in one capability (cross-run accumulation) rather than six independent problems (Step 3)
3. Proves that capability once, against real data, on the highest-risk/highest-value corpus, while also solving the original AbuseIPDB rate-limit problem as a side effect (Step 4)
4. Only then commits to the remaining five corpora and the scheduled workflow, with a validated pattern to replicate instead of six parallel first attempts (Step 5 exit)

Total new-code surface for the PoC: one script, one new JSON file, no changes to `pipeline.yml`, no changes to any tool that's currently live. Fully reversible if something in Step 4 invalidates an assumption.
