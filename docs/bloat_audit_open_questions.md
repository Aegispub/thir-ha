# THIR.HA Bloat Audit — Open Questions Register

**Generated:** 2026-09-11
**Provenance:** Consolidated from four prior audit turns against the `thir-ha` repo snapshot extracted from `thir-HA.zip`:
1. Initial bloat extraction/triage ("I'll extract the zip and take a look...")
2. Full bloat-audit summary (Areas A–J)
3. Fix-order validation (dependency graph, urgency ranking, effective production order)
4. Phase 1 implementation of F1–F4 (this session)

F1–F5 are **settled and out of scope** for this register — see `tools/37_alerts_live.py`, `tools/43_enriched_corpus.py`, `tools/48_fingerprint_corpus.py` diffs (F1–F4, shipped this session) and the F5 entries below (explicitly deferred, not fixed). This document captures only the **residual uncertainty** that remains after those fixes.

## Counts by status

| Status | Count |
|---|---|
| OPEN | 8 |
| PARTIALLY ANSWERED | 3 |
| ANSWERED | 2 |
| DEFERRED | 3 |
| **Total** | **15** |

---

## Register

Sorted: blocking-and-urgent → non-blocking-but-urgent → non-blocking-non-urgent.

---

### Q-01 — Does F2's "unconditional call" fully eliminate the write-only-dict failure pattern, or will the next tool reintroduce it?

- **Source:** Fix-order validation turn ("whether the whole `alert_history.json` file needs a structural refactor to prevent the same 'write-only dict' pattern recurring in future tools")
- **Status:** PARTIALLY ANSWERED
- **What it blocks:** No shipped fix. Blocks confidence that F1–F4's pattern (write-only bookkeeping dict, no delete path) won't recur in a *sixth* tool built after this session.
- **Answer so far:** F2 (Bundle A, shipped) and F3/F4 (Bundles B/C, shipped) all fix the *specific instances* found. They do not add a lint rule, base-class helper, or code-review checklist item that would catch a *new* instance of the same pattern before it ships. The `prune_seen_success_ips`/`prune_seen_asns`/whole-corpus-prune functions are each hand-written per-tool, not a shared utility — three near-identical ~15-line prune functions now exist in `tools/37_alerts_live.py`, `tools/43_enriched_corpus.py`, and `tools/48_fingerprint_corpus.py` with no shared implementation.
- **Next action:** Extract the three prune functions into a single shared helper (e.g. `tools/_dedup_prune.py`, `def prune_stale_keys(d: dict, timestamp_field_or_extractor, max_age_days: int) -> int`) and have all three call sites use it. This is a refactor PR, separate from F1–F4's bug fixes — do not bundle with them. Estimate: 1-2 hours.
- **Owner:** engineering
- **Urgency:** Blocks a future fix (the next corpus-builder tool), not a shipped one.

---

### Q-02 — Tool 26 HTTP-path consolidation referenced in whitepaper v3.2 §5.5: does it exist in code anywhere, and if not, does F5's design need to account for two consolidation mechanisms (SSH + HTTP) or can it be unified?

- **Source:** Original bloat-extraction turn ("Whether the HTTP-path consolidation referenced in whitepaper v3.2 §5.5 actually exists in code, and where — the Tool 26 file provided contains only Cowrie SSH parsing")
- **Status:** OPEN
- **What it blocks:** F5's design (explicitly deferred, not implemented this session). If F5 is scoped as "port the HTTP threshold to SSH," and no HTTP threshold exists yet in code, that framing is invalid and F5's design brief needs correcting before work starts.
- **Next action:** `grep -rn "HTTP_NOISE_THRESHOLD\|request_count\|consolidat" tools/26_incident_timeline_live.py tools/42*.py 2>/dev/null` against the actual repo (Tool 42 doesn't exist as a numbered file in the current `tools/` listing — it's described in the whitepaper as "the `elif http.*` branch inside Tool 26," so also grep for any `http.request`/`attack_vector.*http` handling inside `26_incident_timeline_live.py` itself). If neither exists, file this as a precondition on F5's design doc: "HTTP honeypot (Tool 41/42) has not shipped as of this audit; F5 design must not assume a working HTTP consolidation reference implementation exists to port from."
- **Owner:** design
- **Urgency:** Blocks a future fix (F5). Not urgent today since F5 itself is deferred, but must be resolved before F5 design work starts.

---

### Q-03 — F5's three downstream contract risks: are they fully enumerated, or does the schema drift after F1–F4 change any of them?

- **Source:** Original bloat-extraction turn (Tool 26 consolidation contract risks: (i) ir_cases.json schema impact on Tools 28/35/43, (ii) Tool 43 session_count derivation undercounting once one case represents N sessions, (iii) severity aggregation across collapsed sessions)
- **Status:** PARTIALLY ANSWERED
- **What it blocks:** F5 design start.
- **Answer so far:** Risk (ii) is now **more precisely understood** after this session's F3 fix. Tool 43's `session_count` is `prior_running_session_count + len(genuinely_new_case_ids)` — a count of distinct `case_id` values ever seen (confirmed in `tools/43_enriched_corpus.py`, the accumulation loop, and directly exercised by this session's regression test `test_f3_prune_is_size_only_not_shape_changing`). If F5 collapses N raw SSH sessions into 1 `case_id` (per-IP consolidation, the CLU-002 fix), `session_count` will silently become "distinct *consolidated* cases" not "distinct *raw* sessions" — a real semantic change to a field three other tools may reasonably assume means "attack volume." This is now a **confirmed**, not merely hypothesized, consequence of F5, because the exact mechanism (`genuinely_new_case_ids` counting) was read in full during F3's implementation.
- **Next action:** Before F5 design starts, grep every reader of `enriched_corpus.json`'s `session_count` field (`tools/27_threat_intel_feeder_live.go`, `tools/50_infrastructure_corpus.py`, and the dashboard `js/data.js` if it displays this field) and confirm whether any of them present `session_count` to a human as "number of attacks" — if so, F5's design doc must either (a) add a separate `raw_session_count` field alongside the consolidated `session_count`, or (b) explicitly document the semantic change in the dashboard copy.
- **Owner:** design
- **Urgency:** Blocks a future fix (F5). Not urgent today.

---

### Q-04 — Has `data/.rollup_monthly_pending` (Tool 37's monthly sentinel) ever actually fired in production?

- **Source:** Bloat-audit-summary turn AND fix-order-validation turn (raised independently in both, merged here)
- **Status:** OPEN
- **What it blocks:** Confidence in the 180-day `alerts` dict prune (`prune_alert_history`, unchanged by this session's fixes) actually running as designed. Indirectly relevant to Q-01's refactor scope — if the sentinel pattern itself is unreliable, the shared-helper refactor in Q-01 should not blindly copy it.
- **Next action:** Pull GitHub Actions run history for `.github/workflows/pipeline.yml` filtered to runs where the step log contains `"[Tool37] Monthly sentinel present"` (the print statement at the call site). Count occurrences across the repo's full run history. This requires GitHub API/UI access, not available from a repo file snapshot alone.
- **Owner:** ops
- **Urgency:** Non-blocking for any shipped fix. Worth resolving this quarter since it validates a pattern Q-01's refactor may propagate further.

---

### Q-05 — Is `enriched_corpus.yml`'s 15-minute offset from `pipeline.yml` reliable under GitHub Actions runner load, or can the two workflows interleave unpredictably?

- **Source:** Bloat-audit-summary turn (identical wording preserved from source)
- **Status:** OPEN
- **What it blocks:** Confidence in this session's Bundle B/C effective-timing claims ("executes on the next scheduled run after merge") — those claims assume `enriched_corpus.yml` reads `ir_cases.json`/`ssh_fingerprints.json` *after* `pipeline.yml` has finished writing them for that cycle. If runner queue delays ever invert this, Tool 43/48 could read a stale or mid-write delta file for one cycle. This does not affect F3/F4's *correctness* (the whole-corpus prune is unconditional and doesn't depend on delta freshness), only the freshness of the accumulation half of the same functions.
- **Next action:** Pull GitHub Actions run start-timestamps for both workflows over a representative window (e.g. the last 30 days) and compute the actual gap between `pipeline.yml`'s commit step completing and `enriched_corpus.yml`'s first read step starting. If the gap is ever negative or under a few seconds, that's evidence of interleaving risk.
- **Owner:** ops / monitoring
- **Urgency:** Non-blocking for shipped fixes. Worth a monitoring dashboard entry, not urgent.

---

### Q-06 — Has Tool 40's write to `alert_history.json` ever caused an observed data-loss or race scenario in production (manual re-trigger overlapping a scheduled run)?

- **Source:** Bloat-audit-summary turn AND fix-order-validation turn (the fix-order turn additionally identified this as a previously-**omitted** dependency edge — Tool 40 writes the same file Bundle A modifies, confirmed via `tools/40_failover_notifier.py` line 358)
- **Status:** ANSWERED (by static analysis; runtime confirmation still open)
- **What it blocks:** Confidence that Bundle A (shipped this session) is safe under all trigger conditions, not just the scheduled sequential case.
- **Answer so far:** By code inspection, Tool 40 (`pipeline.yml` line 200) runs strictly before Tool 37 (line 650) in every scheduled invocation, and Tool 40 only ever writes top-level `failover40_*`-namespaced keys — confirmed via `grep -n "credential_ips\|asn_seen" tools/40_failover_notifier.py` returning zero hits both before and after this session's edits. **This means Bundle A's `seen_asns` shape change (list→dict) is safe with respect to Tool 40 under the normal scheduled sequence** — Tool 40 round-trips whatever shape it finds untouched. What is *not* verified is whether a manually re-triggered `pipeline.yml` run (via `workflow_dispatch`) could ever overlap a scheduled run for the same repo checkout, producing two concurrent writers of `alert_history.json` — a scenario GitHub Actions' default concurrency settings may or may not prevent, and which no file in the repo can confirm either way.
- **Next action:** Check `.github/workflows/pipeline.yml` for a `concurrency:` block (`grep -n "concurrency" .github/workflows/pipeline.yml`). If absent, add one (e.g. `group: pipeline, cancel-in-progress: false`) to guarantee sequential execution even under manual re-trigger, and confirm via a deliberate test: trigger the workflow manually while a scheduled run is in flight, observe whether both complete without data loss.
- **Owner:** engineering / ops
- **Urgency:** Non-blocking for Bundle A as shipped (the sequential scheduled case is provably safe). Worth resolving this quarter to close the manual-trigger gap.

---

### Q-07 — Does `check_campaign_alerts`' `campaign_name` dedup key reproduce F1's ordering-bug mechanism?

- **Source:** Fix-order-validation turn ("if the clusterer names campaigns by hashing member-session order, the same ordering bug class as F1 could recur")
- **Status:** ANSWERED
- **What it blocks:** Nothing — resolved as clean.
- **Answer:** Traced `campaign_name`'s origin to `tools/36_command_clustering_live.py` lines 305-312: `cluster["campaign_name"] = top["name"]`, where `top` comes from `match_known_campaigns(all_cmds)` — a **static, fixed-signature lookup table** (confirmed campaign names like `"mdrfckr SSH Key Injection"` are pre-defined string literals, not derived from member-session ordering, hashing, or list-joining). `campaign_name` is therefore deterministic and stable across runs for the same underlying campaign, regardless of session accumulation order. **F1's ordering-bug mechanism does not reproduce here.** No fix needed.
- **Next action:** None — closed. (Retained in the register per the "do not silently drop" instruction, marked ANSWERED for audit trail.)
- **Owner:** — (closed)
- **Urgency:** None.

---

### Q-08 — Does the extra ~5.9MB parse of `enriched_corpus.json` meaningfully affect GitHub Actions runner minutes?

- **Source:** Bloat-audit-summary turn
- **Status:** OPEN
- **What it blocks:** Nothing directly — this is a cost/performance question, not a correctness one. Indirectly informs whether Q-01's refactor (or a future more aggressive prune) is worth prioritizing on cost grounds alone, separate from the correctness/staleness reasoning that justified F3/F4.
- **Next action:** Pull GitHub Actions billing/usage data for `enriched_corpus.yml` runs before and after F3/F4 ship (this session's fixes will shrink the file — a natural before/after comparison point). Compare wall-clock step duration for the "Tool 43 — Actor Corpus" and "Tool 48 — Fingerprint Corpus" steps specifically, isolating parse+prune+write time from network/setup overhead.
- **Owner:** ops / monitoring
- **Urgency:** Non-blocking, non-urgent. Natural side-effect measurement now that F3/F4 are shipped — low-effort to capture, worth doing opportunistically rather than as a dedicated task.

---

### Q-09 — What is the real-world growth rate of `asn_seen["seen_asns"]`, and was 180 days the right default for its prune window?

- **Source:** Bloat-audit-summary turn ("what is the real-world growth rate of `asn_seen["seen_asns"]`, and does it need its own freshness field?") — **partially superseded** by this session's Bundle A implementation, which *did* add the freshness field (the original question asked "does it need one"; the answer, discovered during implementation, was yes, and it now has one).
- **Status:** PARTIALLY ANSWERED
- **What it blocks:** Nothing shipped — `prune_seen_asns`'s 180-day default (Bundle A) is a reasonable placeholder, explicitly documented in its own docstring as "no pre-existing design intent documented for ASN staleness," but it is not validated against real growth data.
- **Answer so far:** The freshness field now exists (`{asn: first_seen_iso}`, shipped this session). The *value* of 180 days was chosen by analogy to Tool 43/48's existing 180-day entry-level prune conventions, not by measuring actual ASN churn. Real-world ASN space is bounded (a few hundred thousand allocated globally) and low-cardinality relative to IP-level bloat, so this is lower priority than Q-04/Q-05, but the number itself is still a guess.
- **Next action:** After 1-2 months of the new `prune_seen_asns` running in production, pull `data/alert_history.json`'s `asn_seen.seen_asns` dict size over time (a simple size-over-time sample, same technique used in this session's original bloat measurements) and check whether 180 days is retaining ASNs that genuinely never recur, or pruning ones that would have recurred just past the window.
- **Owner:** monitoring
- **Urgency:** Non-blocking, non-urgent. Revisit after ~60 days of production data exists.

---

### Q-10 — Should the "unsorted join as dedup-key material" pattern be enforced by a lint rule, given F1's root cause and the (cleared) near-miss in Q-07?

- **Source:** Fix-order-validation turn (cross-cutting observation: "Unsorted joins used as dedup-key material are a repeating near-miss")
- **Status:** OPEN
- **What it blocks:** Nothing shipped. Preventive/process question, not a bug.
- **Next action:** Add a one-line code-review convention note to a `CONTRIBUTING.md` or equivalent: "Any `", ".join(some_list)` that feeds into a dedup key, alert title used for deduplication, or cache key must sort the list first, or document explicitly why order is guaranteed stable." This is a documentation/process change, not code — can be written in under 15 minutes once someone is assigned. A lint rule (AST-based, catching `", ".join(` calls that flow into a variable also passed to a known dedup-key function) is a heavier option; recommend starting with the documentation note and only building tooling if the pattern recurs a third time.
- **Owner:** engineering (process)
- **Urgency:** Non-blocking, non-urgent.

---

### Q-11 — Is F5 (Tool 26 SSH per-IP consolidation) still correctly scoped as "last / deferred," or has this session's finding in Q-03 changed its priority?

- **Source:** NEW — not from prior audit chain. Surfaced by this session's F3 implementation work (Q-03's answer).
- **Status:** OPEN
- **What it blocks:** F5's position in any future ship-order plan.
- **Next action:** Re-run the urgency ranking from the fix-order-validation turn's Section 4 methodology, but now include F5 with the sharper understanding of its `session_count` semantic-change risk from Q-03. F5 was previously ranked implicitly "lowest priority, needs design" — that may still be correct, but it should be a deliberate re-ranking decision, not an assumption carried forward from before Q-03's answer existed.
- **Owner:** design / engineering leadership
- **Urgency:** Non-blocking for any shipped fix. Worth a 30-minute discussion next planning cycle, not urgent.

---

### Q-12 — Do the three new regression test files (`tests/test_tool37_dedup_pruning.py`, `tests/test_tool43_whole_corpus_prune.py`, `tests/test_tool48_whole_corpus_prune.py`) need to be wired into CI, or do they only run manually?

- **Source:** NEW — not from prior audit chain. This is an artifact of this session creating the repo's first-ever test files (confirmed: no `tests/` directory or test framework existed before this session).
- **Status:** OPEN
- **What it blocks:** Whether F1–F4's regression protection is durable (catches a future accidental revert) or only exists as a one-time manual verification (as performed in this session).
- **Next action:** Add a step to `.github/workflows/pipeline.yml` or a new lightweight `tests.yml` workflow: `run: for f in tests/test_*.py; do python3 "$f" || exit 1; done`, triggered on every PR touching `tools/*.py`. This is a small, contained addition — estimate 30 minutes including verifying it doesn't break the existing pipeline schedule.
- **Owner:** engineering
- **Urgency:** Non-blocking for the fixes as shipped (they are correct today), but this is the difference between "fixed once" and "fixed durably." Recommend treating as near-term, not backlog.

---

### Q-13 — DEFERRED: F5 design work itself

- **Source:** Settled context (all four prior turns) — explicitly out of scope for implementation this session, per repeated instruction.
- **Status:** DEFERRED
- **Reason:** Requires a dedicated design pass addressing the three contract risks (Q-03), plus Q-02's precondition check, plus Q-11's re-ranking. Not a "next Monday" task — this is a multi-day design effort.
- **What it blocks:** The CLU-002-style scanner-flood bloat in `ir_cases.json` (78% of that file's bytes, per the original bloat audit) remains unfixed until F5 ships.
- **Next action:** Once Q-02 and Q-03 are answered, write a standalone design doc proposing the consolidation approach, explicitly addressing all three contract risks with proposed schema changes, before any code is written.
- **Owner:** design
- **Urgency:** Known, accepted, deferred by explicit decision across all four audit turns. Not being tracked as "blocking" anything currently shipped.

---

### Q-14 — DEFERRED: Whether `alert_history.json`'s three-dict structure (`alerts` / `credential_ips` / `asn_seen`) should be split into three separate files

- **Source:** NEW — surfaced during Bundle A implementation while examining Tool 40's read-modify-write chain (Q-06) and the shared-pattern question (Q-01).
- **Status:** DEFERRED
- **Reason:** A structural split (one file per concern) would eliminate Tool 40's incidental full-file round-trip of unrelated `credential_ips`/`asn_seen` data on every failover-notification run, and would make Q-06's concurrency question moot for two of the three concerns. But this is a larger, riskier refactor than anything scoped in F1–F5, touches both `37_alerts_live.py` and `40_failover_notifier.py`'s file paths, and was explicitly not requested.
- **What it blocks:** Nothing currently. A "nicer" future state, not a bug.
- **Next action:** Raise as a discussion item alongside Q-01's shared-helper refactor — if that refactor happens, this is the natural moment to also evaluate the file-split, since both touch the same three prune functions' call sites.
- **Owner:** engineering (design discussion)
- **Urgency:** None currently identified. Pure architecture-quality question.

---

### Q-15 — DEFERRED: Whether Tool 44/47/49/50's lack of the `_seen_*` bookkeeping pattern (confirmed clean in the bloat-audit-summary turn) means they use a fundamentally safer accumulation strategy that F3/F4's fix should have adopted instead

- **Source:** NEW — surfaced by re-reading the bloat-audit-summary turn's "Already-Fixed / Not-a-Bug" section during this session's implementation, which noted Tools 44/47/49/50 rely on `unique_ips_ever`-style set growth instead of per-event timestamped dicts.
- **Status:** DEFERRED
- **Reason:** F3/F4's whole-corpus prune (shipped this session) is a correct, minimal fix to the *existing* design (timestamped bookkeeping dicts). Switching to a `unique_ips_ever`-style set-only design instead would be a larger, different fix — not what F3/F4 were scoped to do, and would lose the exact-dedup precision the module docstrings in Tool 43/48 explicitly call out as an advantage over Tool 44's "weaker IP-set-growth fallback" (`tools/48_fingerprint_corpus.py` docstring, line ~16-19).
- **What it blocks:** Nothing — this is a design-philosophy question about whether the *fixed* pattern is still the right pattern, not whether the fix is correct.
- **Next action:** No action needed unless a future audit finds the whole-corpus prune itself becoming a performance bottleneck (see Q-08) — if so, revisit whether the set-only design's lower precision is an acceptable trade for lower cost.
- **Owner:** design (future, conditional)
- **Urgency:** None. Purely speculative future consideration.

---

## If only three questions get answered this quarter, they should be:

**Q-06** (Tool 40 / Tool 37 concurrency under manual re-trigger), **Q-04** (has the monthly sentinel ever fired), and **Q-12** (wire the new tests into CI).

Reasoning: Q-06 is the only question in this register that touches the *correctness* of a fix already shipped this session under a condition not yet proven safe — everything else is either closed (Q-07), cosmetic/process (Q-10), speculative (Q-09, Q-15), or blocks only *future* work (Q-01 through Q-03, Q-11, Q-13, Q-14). Q-04 is cheap to answer (a GitHub Actions log search) and directly informs whether the 180-day `alerts` prune — which Q-01's proposed shared-helper refactor would otherwise blindly generalize — is a pattern worth propagating or a pattern that's never actually been exercised. Q-12 is the cheapest of the three (an estimated 30 minutes) and is the difference between F1–F4 being *fixed* versus *fixed and protected against regression* — without it, this session's entire regression-test effort has no durability beyond the one-time verification already performed.
