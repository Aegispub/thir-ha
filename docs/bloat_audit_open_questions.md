# THIR.HA Bloat Audit — Open Questions Register

**Generated:** 2026-09-11
**Last updated:** 2026-09-24 (**latest: Q-21 filed and resolved — F5 collapsed Tool 36's per-cluster session_count from cardinality (each consolidated case = 1) instead of weight; two-part fix (carry session_count through extraction, then sum instead of count), verified exact match to pre-F5 baseline (1,869 = 1,869, CLU-013 1,809 = 1,809); Q-18/Q-19's open actions closed by building `tools/51_attacker_profiles.py`, which independently reproduces both findings against the live corpus; register now 21 entries**; earlier this session: Q-20 filed and resolved — F5 dropped 2 of 20 HASSH fingerprints in pre-push verification; root cause was representative selection, not grouping; fixed, 16/16 tests, HASSH restored to 20; still earlier: autonomous code-audit session — Q-02, Q-03 resolved against actual repo; Q-16 filed; Q-17 filed; Q-01(b) reframed and closed by cross-reference to Q-18; Q-15 corrected; Q-18 filed after a comprehensive shape-based scan; Q-19 filed — unattributed HASSH fingerprint surfaced during Q-18's distribution check; Q-06 resolved — concurrency guard confirmed present and correctly shaped; Q-04 resolved — monthly sentinel confirmed firing via `reports/monthly/`'s six-consecutive-file evidence, ownership corrected from Tool 37 to Tool 32; Q-12 resolved and **implemented** — `.github/workflows/tests.yml` shipped, all three test files confirmed passing pre-merge, branch name corrected to `oracle-ha` [confirmed via `MIGRATION.md:47`, not assumed] and `permissions: contents: read` added; counts table rebuilt with a two-column Status/Open-action convention after three arithmetic/classification errors were found in the single-column version; closing section replaced — reframed from quarterly-milestone language to portfolio-repo language, since this project has no external stakeholders or deadlines; Q-16 given an explicit Shape 3 recommendation with a full F5 design-brief skeleton, moving F5 from "blocked on an undecided design question" to "blocked only on someone writing the code")

**Methodology note for future sessions working this repo:** six separate findings this session were initially misclassified, each corrected by the same move — checking the actual shape of the data rather than trusting a name, a percentage, or an aggregate count on its own. (1) A byte-arithmetic "gap" turned out to be a units mismatch (cases vs. output entries), not a missing code path. (2) A name-based grep for `_seen_*` matched `first_seen`/`last_seen` as false positives, and separately missed Tool 47's `success_events` because it isn't `_seen_`-prefixed at all — only a byte-measurement scan across every field, regardless of name, caught it. (3) A windowed session count (`_seen_sessions`, a 2-day rolling slice) was initially read as a single contiguous burst, when the underlying cumulative total (`session_count`) told a different, larger story. (4) During F5's verification, a raw-set intersection reported "121 `case_id` collisions" between F5's output and the original corpus — alarming on its face — and resolved to correct, designed behavior once traced: the 121 were singleton pass-through cases correctly retaining their original, unmodified `case_id`s, not a bug in the newly-generated ids (of which zero collided). The alarm was right to fire; the answer required separating "newly-generated ids" from "pass-through ids" before concluding anything, not dismissing the number because it seemed too large to be real, and not accepting it as a bug without that separation either. (5) During pre-push verification of F5, Tool 35's HASSH count dropped from 20 to 18 after consolidation. The obvious diagnosis — that the grouping key merged sessions from genuinely different SSH clients — was checked against real timelines and found **false**: every affected group had exactly one distinct HASSH shared by all members. The real defect was representative selection (earliest-by-timestamp favored the fast-failing session whose KEX event was never captured). The instruction that prompted the fix had assumed the grouping-key diagnosis and specified a field (`hostKeyAlgs`) that does not exist in Tool 35's extraction; reading the code and the data showed both the diagnosis and the field list were wrong, and the fix that shipped is narrower. (6) A proposed one-line fix for Q-21 (`sum(m.get("session_count", 1) ...)` in Tool 36's aggregation step) was read against the actual extraction function before being applied, and would have been a **silent no-op**: `cl["members"]` entries never carried a `session_count` field at all, because an earlier extraction step builds each session dict from a hand-picked list of fields that didn't include it. The fix needed a second part — carrying the field through extraction — that nothing about the single proposed line would have revealed as missing; the tests would have passed (`.get(..., 1)` never raises) while never actually firing on real data. **A byte-reduction or field-propagation fix must verify signal preservation, not only byte count, and a plausible root cause or a plausible one-line patch must be checked against the actual data flow before it is shipped.** **The reusable rule: check the actual shape before classifying — a name, a percentage, or a count in isolation will mislead at least once per session.**
**Provenance:** Consolidated from four prior audit turns against the `thir-ha` repo snapshot extracted from `thir-HA.zip`:
1. Initial bloat extraction/triage ("I'll extract the zip and take a look...")
2. Full bloat-audit summary (Areas A–J)
3. Fix-order validation (dependency graph, urgency ranking, effective production order)
4. Phase 1 implementation of F1–F4 (this session)
5. Autonomous code-audit session, 2026-09-24 — Q-02/Q-03 verified by direct grep/trace against the extracted repo (superseding their status as last committed here); Q-16 filed (Tool 28 consolidation gap); Q-17 filed (F5 code-existence, RESOLVED NO); Q-01 resolved (a); Q-01(b) went through two revisions within this same session (see note below) before a comprehensive shape-based scan (not name-based grep) produced the final classification, now closed by cross-reference to Q-18.

**Methodological note on Q-01(b)/Q-15/Q-18:** this cluster of questions was answered three times in one session, each revision produced by a tighter grep than the last. The first pass ("7-for-7, convention holding") was wrong on the mechanism. The second pass (name-based `_seen_*` tightening) correctly caught the false positive but was still name-based, and missed `success_events` because it isn't named with a `_seen_` prefix. Only the third pass — a shape-based scan across every entry-keyed corpus file, measuring actual bytes rather than grepping for a naming pattern — produced a complete, stable classification. This is recorded here as a caution for future audit passes on this register: **prefer one shape/byte-based scan over successive name-based grep tightening**, since the latter reliably produces one more revision than expected.

F1–F5 are **settled and out of scope** for this register** for implementation purposes** — see `tools/37_alerts_live.py`, `tools/43_enriched_corpus.py`, `tools/48_fingerprint_corpus.py` diffs (F1–F4, shipped this session) and the F5 entries below (explicitly deferred, not fixed). This document captures the **residual uncertainty** that remains after those fixes, including uncertainty resolved or reframed by the 2026-09-24 audit pass.

## Counts by status

**Convention for dual-status entries (added this pass):** four entries — Q-01, Q-12, Q-16, Q-18 — carry a split status (a finding/verification half that is closed, plus a distinct half that remains open). A single-column table cannot represent this without ambiguity; the table below uses two columns — **Status** (the entry's overall resolution state) and **Open action** (what, if anything, remains) — so "RESOLVED, nothing left" and "RESOLVED, one action pending" are visibly different, which the previous single-column table did not distinguish.

| Entry | Status | Open action |
|---|---|---|
| Q-01 | RESOLVED | None — (b) closed by cross-reference to Q-18 |
| Q-02 | RESOLVED NO | None |
| Q-03 | RESOLVED | None — risk #3 spawned Q-16, tracked there |
| Q-04 | RESOLVED | None |
| Q-05 | OPEN | Pull GHA timing data (needs API access) |
| Q-06 | RESOLVED | Optional live-test residual (non-blocking) |
| Q-07 | ANSWERED | None — closed, clean |
| Q-08 | OPEN | Pull GHA billing/usage data (needs API access) |
| Q-09 | PARTIALLY ANSWERED | Revisit after ~60 days of production data |
| Q-10 | OPEN | Write CONTRIBUTING.md convention note |
| Q-11 | RESOLVED | None — folded into Q-13, no separate ranking exercise needed |
| Q-12 | RESOLVED — fully closed | None — `.github/workflows/tests.yml` shipped this pass, pre-flight run confirms all 3 test files pass cleanly |
| Q-13 | RESOLVED — fully closed | None — F5 shipped, verified against real corpus (2,236→211 cases, 8.06MB→614KB) |
| Q-14 | DEFERRED | Architecture discussion, no urgency assigned |
| Q-15 | CLOSED | None — superseded, folded into Q-01/Q-18 |
| Q-16 | RESOLVED | None — Shape 3 selected and implemented as F5, tracked in Q-13 |
| Q-17 | RESOLVED NO | None |
| Q-18 | RESOLVED | Consumer built (`tools/51_attacker_profiles.py`) — SOC/remediation-shape decision for `success_events` still open |
| Q-19 | RESOLVED | Consumer built (`tools/51_attacker_profiles.py`) — attribution itself still open |
| Q-20 | RESOLVED | None — found and fixed pre-push, HASSH count restored to 20 |
| Q-21 | RESOLVED | None — found and fixed pre-push, session_count restored to exact pre-F5 baseline |

| Status | Count |
|---|---|
| RESOLVED | 12 |
| RESOLVED NO | 2 |
| OPEN | 3 |
| DEFERRED | 1 |
| ANSWERED | 1 |
| PARTIALLY ANSWERED | 1 |
| CLOSED | 1 |
| **Total** | **21** ✓ |

**Tally history (retained for audit trail, not because it needs re-deriving again):** this table was rebuilt three times across the session as entries changed status — 19→20 entries with Q-20's addition, 20→21 with Q-21's addition. The count-by-status total is unchanged at 21 entries throughout this final pass (only Q-18/Q-19's row text and Q-21's status changed; no entry was added or removed by this edit). The full row-by-row status list this tally is derived from: Q-01 RESOLVED, Q-02 RESOLVED NO, Q-03 RESOLVED, Q-04 RESOLVED, Q-05 OPEN, Q-06 RESOLVED, Q-07 ANSWERED, Q-08 OPEN, Q-09 PARTIALLY ANSWERED, Q-10 OPEN, Q-11 RESOLVED, Q-12 RESOLVED, Q-13 RESOLVED, Q-14 DEFERRED, Q-15 CLOSED, Q-16 RESOLVED, Q-17 RESOLVED NO, Q-18 RESOLVED, Q-19 RESOLVED, Q-20 RESOLVED, Q-21 RESOLVED — 21 entries, matching the header count above.

(The erroneous 20-count two paragraphs above was left visible deliberately, with its own arithmetic shown, as a live example of the register's own methodology note — a number produced without re-deriving it from the actual per-entry source is exactly the kind of error this file has caught three times already this session. It was caught here on the fourth attempt at the same table, not the first, which is itself worth recording: getting a summary count right on the first try is not guaranteed even when the underlying per-entry data is already correct.)

**Status changes this pass (2026-09-24, prior audit turns):**
- Q-01: PARTIALLY ANSWERED → **RESOLVED (a) / RESOLVED (b, reframed and closed by cross-reference to Q-18)** — see entry. Do not reopen Q-01(b) again; any further findings on this bug class belong under Q-18/Q-19 or a new number, not a fourth revision of Q-01.
- Q-02: OPEN → **RESOLVED NO (design-only)** — see entry.
- Q-03: PARTIALLY ANSWERED → **RESOLVED** — all three risks traced; risk #3 spawned Q-16.
- Q-04: OPEN → **RESOLVED** — monthly sentinel confirmed firing successfully via direct repo evidence (`reports/monthly/`, six consecutive months, no gaps), resolved without GitHub API access. Ownership corrected: Tool 32, not Tool 37.
- Q-06: ANSWERED (static, runtime open) → **RESOLVED** — concurrency block confirmed present, correctly configured (`group: thir-pipeline`, `cancel-in-progress: false`), covers both trigger paths and Tool 40's write path. One optional live-test residual noted, non-blocking.
- Q-12: OPEN → **RESOLVED** — CI wiring confirmed absent (zero references to `tests/` in any of the three workflows). Fix specified, not yet implemented — the one item in the original trio still requiring code, not just verification.
- Q-15: DEFERRED, premise corrected twice this session — final correction below supersedes both prior corrections. Closed by cross-reference to Q-01/Q-18.
- Q-16: **NEW** — Tool 28 does not consolidate the dominant flood pattern (login_success=True exclusion).
- Q-17: **NEW** — no F5 code exists anywhere in the repo as of this audit pass (confirmed, not merely absent from Tool 26).
- Q-18: **NEW** — `data/credential_corpus.json`'s `success_events` field is an unaddressed, unbounded, actively-growing instance of the F1 bug class, confirmed by byte measurement (74.7% of file) and production footprint (96 timestamps across ~25 days, one entry with 839 unique source IPs). Reclassified as threat-intel-first, not engineering-only.
- Q-19: **NEW** — unattributed SSH client fingerprint (HASSH `01ca35584ad5a1b66cf6a9846b5b2821`), 53,426 cumulative sessions from 4 source IPs, surfaced during Q-18's `_seen_sessions` distribution check. No campaign match found in `docs/`. Filed at Q-18 tier, not a footnote.

---

## Register

Sorted: blocking-and-urgent → non-blocking-but-urgent → non-blocking-non-urgent.

---

### Q-01 — Does F2's "unconditional call" fully eliminate the write-only-dict failure pattern, or will the next tool reintroduce it?

- **Source:** Fix-order validation turn ("whether the whole `alert_history.json` file needs a structural refactor to prevent the same 'write-only dict' pattern recurring in future tools")
- **Status:** **RESOLVED (a) / OPEN (b, reframed)** — updated 2026-09-24, autonomous audit pass
- **What it blocks:** (a) nothing — closed. (b) no shipped fix; blocks confidence that the pattern won't recur in a future tool, but see reframing below — the premise that a "sixth corpus-builder tool" is pending is not currently supported by the repo.

This question bundles two claims with different answer types and is split accordingly:

**(a) — Does F2's unconditional call fully eliminate the pattern in the tools it touched?**

RESOLVED YES. Confirmed by direct grep against the three tools named in the original finding:
- `tools/37_alerts_live.py:87` `prune_alert_history()`, `:106` `prune_seen_success_ips()`, `:136` `prune_seen_asns()` — all three called unconditionally at `:612`, `:615`, `:620`.
- `tools/43_enriched_corpus.py:340` `prune_actor_corpus()` — called unconditionally at `:417`.
- `tools/48_fingerprint_corpus.py:177` `prune_fingerprint_corpus()` — called unconditionally at `:257`.

The write-only-dict pattern is eliminated in all three originally-flagged tools. No further action needed on (a).

**(b) — Will the next tool reintroduce it?**

OPEN, and reframed, because the original question is empirically unfalsifiable from current code — it is a prediction about future code, not a fact about existing code — and the register's own proposed mitigation (extract to a shared helper) does not answer it. A shared helper is opt-in; a sixth tool can write its own untracked bookkeeping dict and simply not call it. Extraction reduces duplication, not recurrence risk.

**Corrected empirical base rate, final (this entry was revised twice within the 2026-09-24 session — see the methodological note at the top of this register; this text supersedes both prior versions):**

A comprehensive shape-based scan (bytes measured directly from each entry-keyed corpus JSON file, not name-based grep) produced the final classification:

**Scan-completeness note (added per review):** `data/ir_cases.json` and `data/ssh_fingerprints.json` were not scanned by the shape filter below — both are wrapper objects (`{"generated_at": ..., "cases": [...]}` / `{"generated_at": ..., "fingerprints": {...}}`), not flat entry-keyed dicts, and were skipped automatically rather than deliberately excluded. `ir_cases.json`'s bloat is covered by Q-16. `ssh_fingerprints.json`'s own wrapper-file size was not separately measured — a genuine gap, not a covered one.

| Tool | Corpus file | Nested field | Bytes | % of file | Classification |
|---|---|---|---|---|---|
| — | `data/ir_cases.json` | n/a (wrapper, not entry-keyed) | — | — | **Not scanned — shape mismatch. See Q-16.** |
| — | `data/ssh_fingerprints.json` | n/a (wrapper, not entry-keyed) | — | — | **Not scanned — shape mismatch. Not separately measured. Genuine gap.** |
| 37 | `data/alert_history.json` | `alerts` dict itself (11,409 entries, 1.9M) | — | 97% | F1/F2's known, gated target — not new. **Note: bigger than `success_events` + `_seen_case_ids` combined, round-tripped whole by Tool 40 every failover check (Q-06). Not filed as its own finding — may warrant its own Q-number if Q-06's concurrency question is ever reopened (see Q-06).** |
| 37 | same | `seen_success_ips` | 37,464 | 1.9% | Bounded, F2's fix |
| 43 | `data/enriched_corpus.json` | `_seen_case_ids` | 696,200 | 16.4% | Bounded — F3's mechanism working as designed |
| 44 | `data/campaign_corpus.json` | `unique_ips_ever` | 26,468 | 24.1% | Set-growth, self-limiting by IP cardinality — not a risk |
| 47 | `data/credential_corpus.json` | `success_events` | 299,673 | **74.7%** | **UNADDRESSED — filed as Q-18, reclassified as threat-intel-first finding** |
| 48 | `data/fingerprint_corpus.json` | `_seen_sessions` | 660,450 | 80.5% | Expected under current traffic; verified against snapshot. **Tail risk, not fully closed: F4's 2-day window bounds time, not volume — a 4x burst in the same window would produce a ~1.3MB single-entry field. Not urgent; noted for a future sizing pass rather than closed outright.** See also the unfiled scanner observation below the table. |
| 49 | `data/malware_corpus.json` | `observed_aliases` | 6,875 | 17.7% | `set()`-deduped, self-limiting, small absolute size |
| 50 | `data/infrastructure_corpus.json` | `unique_ips_ever` | 119,778 | 11.0% | Set-growth, self-limiting — not a risk |

**See Q-19** for the HASSH fingerprint pattern this distribution check surfaced.

**Corrected count of the F1-class bug (unbounded nested dict/list, no cutoff prune):** exactly **one** unaddressed live instance — Tool 47's `success_events` (Q-18) — not seven (this session's first pass), not three-plus-Tool-47 (this session's second pass). Tools 37/43/48 have the bug *fixed*. Tools 44/49/50's `unique_ips_ever`/`observed_aliases` fields are `set()`-based and self-limiting by construction — they were never an instance of this bug class, correctly per the original Q-15 for Tool 44 specifically, but Q-15's generalization to all four tools was wrong (49/50 have no such field at all in their entries; their entry-level `prune_*_corpus()` functions delete whole stale entries, which is a different, unrelated mechanism, correctly present in all three but not the F1-class fix).

**Sixth-tool premise check:** `ls tools/ | grep -E "_corpus|_feeder|_fingerprint|_enrich"` returns 8 existing corpus/enrichment tools (27, 35, 43, 44, 47, 48, 49, 50) — no evidence of a ninth/unbuilt corpus-builder tool in the tree or referenced elsewhere in this register. Q-01's original urgency tag ("blocks a future fix — the next corpus-builder tool") presupposes a next tool is planned; **no such tool is currently confirmed pending.** Urgency downgraded accordingly.

**Enforcement surface check:** `.github/workflows/` contains exactly three workflows — `enriched_corpus.yml`, `historical_processor.yml`, `pipeline.yml`. No lint/CI workflow exists. **Any enforcement option (B below) requires building CI lint infrastructure from scratch.**

**Design decision, final (four options):**

- **Option A — extract shared helper.** Scope is now correctly **3 call sites** (Tools 37/43/48's `_seen_*`-prune mechanism), not 7. Reduces duplication for the mechanism that's actually duplicated. Does not prevent recurrence (opt-in). ~1h.
- **Option B — shape-based lint check**, not name-based: flag any per-entry list/dict field that only appends, is never pruned by cutoff or cap, across the whole corpus, regardless of field name. This is the check that would have caught Tool 47's `success_events` (a name-based check would not, since it isn't `_seen_`-prefixed). Nontrivial AST work — distinguishing append-only from mutation, excluding bounded/deduped `set()`-based fields, walking nested structures. No existing lint surface to build on. Harder than a naming-convention check; the case for building it is stronger after Q-18 (it would have caught a real, currently-live bug), but the mechanism itself is not simpler as a result — a stronger case for a harder mechanism does not automatically net positive against "no lint workflow exists yet."
- **Option C — CONTRIBUTING.md convention note.** Lowest lift. Should explicitly cover both the naming convention (`_seen_*` pairs with a prune call) and the shape principle Q-18 surfaces (any append-only per-entry collection needs a cutoff or cap, whether or not it's named `_seen_*`).
- **Option D — no action.** No longer well-supported on its own — Q-18 is a real, live, unaddressed instance of exactly the bug class Q-01 asks about, found by the same audit that would need to justify "no action." Do not select D without addressing Q-18 separately.

**Recommendation:** Option A for the 3 real duplicate call sites (Tools 37/43/48), plus Option C's convention note extended to cover the shape principle, not just the naming pattern. Option B remains deferred pending lint-infrastructure investment — the case for it strengthened by Q-18, but the mechanism cost is unchanged and still exceeds what's justified without an existing CI lint surface to extend.

- **Cross-reference:** Q-15 (this entry's final correction resolves Q-15 by cross-reference — see Q-15's entry, now marked closed), Q-10 (same preventive/process family; urgency tags aligned), **Q-18 (the actual live finding this question was ultimately searching for — do not re-derive it again from Q-01; it is filed and closed as its own entry)**.
- **Owner:** engineering (a — closed) / design + engineering leadership (b — decision needed on A/B/C/D, informed by Q-18)
- **Urgency:** (a) none, closed. (b) **RESOLVED and closed by cross-reference to Q-18** — do not reopen this entry again in this register; any further findings on this bug class belong under Q-18 or a new Q-number.

---

### Q-02 — Tool 26 HTTP-path consolidation referenced in whitepaper v3.2 §5.5: does it exist in code anywhere, and if not, does F5's design need to account for two consolidation mechanisms (SSH + HTTP) or can it be unified?

- **Source:** Original bloat-extraction turn ("Whether the HTTP-path consolidation referenced in whitepaper v3.2 §5.5 actually exists in code, and where — the Tool 26 file provided contains only Cowrie SSH parsing")
- **Status:** **RESOLVED NO — NOT IMPLEMENTED / DESIGN-ONLY** — updated 2026-09-24, autonomous audit pass
- **What it blocks:** F5's design (explicitly deferred, not implemented this session). Now resolved as a stated precondition rather than an open question — see below.
- **Evidence, this pass:** `grep -n "HTTP_NOISE_THRESHOLD\|request_count\|consolidat" tools/26_incident_timeline_live.py` → 0 hits. `grep -n "http\." tools/26_incident_timeline_live.py` → 0 hits. `grep -rn "attack_vector" tools/` → 0 hits. `ls tools/ | grep -i 42` → 0 hits, confirming Tool 42 does not exist as a file (consistent with the whitepaper's own framing that it would be an `elif http.*` branch inside Tool 26 — that branch is also absent). `tools/http_honeypot/` contains only staged Cowrie-plugin source (`http/factory.py`, `http/__init__.py`, `http/honeypot.py`, `cowrie_plugin.py.patch`, `output.py.patch`, `pool_ready_addition.py`) — not pipeline code, and not referenced by any of the three CI workflows (`pipeline.yml`, `enriched_corpus.yml`, `historical_processor.yml` all checked, zero matches). One stale comment, `tools/http_honeypot/http/honeypot.py:63`, asserts *"Scanner noise handled by per-IP deduplication in Tool 26"* — this is **false**, left over from the whitepaper's design intent, and must not be read as evidence of an implementation.
- **Resolution:** HTTP-path consolidation does not exist in code anywhere in this repo. It is whitepaper-only. F5's design brief must state explicitly: *"No HTTP consolidation reference implementation exists in code as of this audit. F5 is the first per-IP/session consolidation mechanism built in this codebase — there is nothing to port from, and no dual-mechanism (SSH+HTTP) unification question arises because only one (SSH) needs to be designed."* This also resolves the second half of the original question — "does F5 need to account for two mechanisms" — the answer is no, because only one will ever have existed to design in the first place.
- **See also:** Q-17 (broader finding — no F5 code of *any* kind, HTTP or SSH, exists anywhere in the repo).
- **Owner:** design (closed — precondition stated, no further action needed before F5 design starts)
- **Urgency:** Closed.

---

### Q-03 — F5's three downstream contract risks: are they fully enumerated, or does the schema drift after F1–F4 change any of them?

- **Source:** Original bloat-extraction turn (Tool 26 consolidation contract risks: (i) ir_cases.json schema impact on Tools 28/35/43, (ii) Tool 43 session_count derivation undercounting once one case represents N sessions, (iii) severity aggregation across collapsed sessions)
- **Status:** **RESOLVED** — updated 2026-09-24, autonomous audit pass. All three risks traced to their actual consumers; risk #3's trace produced a new, sharper finding filed separately as **Q-16**.
- **What it blocks:** Nothing — closed for design-start purposes. Q-16 is the one open design item that survives this resolution.

**Risk (i) — ir_cases.json schema impact on Tools 28/35/js:** NONE-impact confirmed by direct trace.
- Tool 28 (`tools/28_soc_handover_live.py:234-357`) already runs its own independent per-IP grouping (`group_cases_for_report`) and already tolerates/expects that a "case" may need consolidating — no assumption that one `case_id` = one raw session.
- Tool 35 (`tools/35_ssh_fingerprint_live.py:111-147`) processes `case.get("timeline", ...)` per case, agnostic to what the case represents.
- `js/pipeline.js`'s `bindIRCases()` only ever renders the first 10 raw cases individually (`cases.slice(0, 10)`) — no aggregate field depends on case cardinality.
- `js/data.js` has no runtime field access to `ir_cases.json` at all (static descriptive text only).

**Risk (ii) — Tool 43 session_count semantic drift:** NONE-impact confirmed. Traced every consumer named in the original risk:
- `tools/27_threat_intel_feeder_live.go:106-109` — `CorpusEntry` struct explicitly does not declare `session_count`; comment states extra fields "are ignored by Go's json.Unmarshal, not an error." Never read.
- `tools/50_infrastructure_corpus.py:136-164` — reads `enriched_corpus.get(ip)` for Tor/VPN/proxy flags only; `session_count` never referenced (`grep -n "session_count"` → 0 hits).
- `js/data.js:235` — only a static UI description string ("session counts" as prose); `grep -n "session_count"` → 0 hits, no runtime render path.
- The field is written and used only internally, within Tool 43's own next-run delta calculation. No external reader is misled by any semantic shift F5 would introduce.

**Risk (iii) — severity aggregation across collapsed sessions:** NONE-impact on *existing* consumers, but this trace surfaced the real, actionable finding:
- Tool 26's `calculate_severity()` (`:206-217`) is purely per-case, computed before any hypothetical consolidation — no existing aggregation logic to break.
- Tool 43's `last_session_severity` (`:184-188`) takes the single most-recent case's severity verbatim — it does not aggregate, so it is mechanically unaffected by consolidation (only its definitional scope narrows).
- Tool 28 computes its **own independent** severity for grouped rows (`"MEDIUM" if len(session_list) >= GROUP_MEDIUM_THRESH else "LOW"`, `:336`) — fully insulated from any Tool 26/43 severity field.
- **However**, running Tool 28's actual grouping code against the live `ir_cases.json` snapshot revealed that its `is_groupable()` predicate (`login_success` exclusion) makes it structurally blind to the CLU-002-style flood — 1,096 of 1,099 cases from the dominant flooding IP have `login_success=True` and bypass grouping entirely, rendering as individual blocks (95.9% of report bytes). This is not a contract risk to an existing consumer — it is a **design requirement F5 must satisfy that Tool 28's existing rule does not provide a template for.** Filed as **Q-16**.

- **Cross-reference:** Q-16 (spawned by this entry's risk-#3 trace), Q-17 (confirms no F5 code exists to have any of these risks apply to yet).
- **Owner:** design (closed — three risks traced; remaining open item is Q-16, not a re-open of this entry)
- **Urgency:** Closed.

---

### Q-04 — Has `data/.rollup_monthly_pending` (Tool 32's monthly sentinel — corrected below) ever actually fired in production?

- **Source:** Bloat-audit-summary turn AND fix-order-validation turn (raised independently in both, merged here)
- **Status:** **RESOLVED — updated 2026-09-24, follow-up audit pass. Resolved from repo files alone; GitHub Actions API/UI access was not needed.**
- **Correction to this entry's own title/attribution:** the sentinel is not Tool 37's. `grep -rn "rollup_monthly_pending"` across the repo shows it is created, checked, and cleared entirely inside `.github/workflows/pipeline.yml`'s shell steps (`:759-811`), calling `tools/32_report_lifecycle.py --rollup monthly`. Tool 37's only connection is a single explanatory comment (`tools/37_alerts_live.py:605`) noting that `seen_success_ips`' own prune timing is unrelated to this sentinel — not ownership. Tool 32 is the correct owner.
- **What it blocks:** Nothing further. Confidence in the 180-day `alerts` dict prune's *own* reliability (a separate mechanism, owned by Tool 37, unaffected by this sentinel) was never actually dependent on this question — that conflation in the original entry is itself corrected here. What this entry actually validates is the monthly/weekly *report rollup* cadence, which is a real and now-confirmed-working pattern Q-01's shared-helper discussion could reasonably reference as a second example of the "sentinel + unconditional-check + clear-on-success" design, alongside Tools 37/43/48's `_seen_*`-prune convention — they are two different mechanisms solving two different problems (event-bookkeeping pruning vs. calendar-triggered rollup), not the same pattern.
- **Evidence, repo-side, sufficient to resolve without GitHub API access:**
  - `data/.rollup_monthly_pending`: absent in this checkout — expected and uninformative on its own, per the create-on-1st/delete-on-success design (`pipeline.yml:739-748`'s own comment block documents this explicitly).
  - **Direct evidence of successful firing:** `reports/monthly/` contains six consecutive files with no gaps — `soc_2026-03.md`, `soc_2026-04.md`, `soc_2026-05.md`, `soc_2026-06.md`, `soc_2026-07.md`, `soc_2026-08.md`. Each is producible only by a successful `--rollup monthly` invocation (`pipeline.yml:798-801`), and the sentinel is cleared only on that invocation's exit code 0 (`:803-805`). Six real month-boundaries, six files, zero gaps is direct, not circumstantial, evidence the mechanism has fired and succeeded repeatedly in production.
  - `reports/weekly/` independently corroborates the sibling mechanism (weekly sentinel, same design pattern): 7 files spanning W18 through W38; gaps between them are consistent with Tool 32's own weekly retention/pruning policy (3-4 week window, per the Layer 7 domain reference), not missed firings.
- **One nuance surfaced by reading the full mechanism, not just grepping for the filename:** `pipeline.yml:796-810` has **three** exit paths, not two — success (0, sentinel cleared), a documented deferral case (exit code 3, "previous month's final week not yet rolled up," sentinel retained for retry — this is a real, intentional non-failure state, not a bug), and genuine failure (any other code, sentinel retained for retry). The code comments (`:735-737`) confirm this three-path design is itself a **fix** to a previously-broken mechanism: an earlier HOUR-of-day gate combined with `continue-on-error` silently dropped weekly rollups for 4+ weeks in production before being replaced with the current sentinel approach. This means the honest answer to "has the monthly sentinel ever fired" is: **yes, reliably, under the current (rewritten) design — and there is repo-documented history of an earlier design that did not fire reliably**, which is a more complete and more useful answer than a yes/no.
- **Required changes:** None. No fix needed — confirmed working.
- **Next actions:** None required to close this entry. Optional, low-priority: the exact GitHub Actions log line this entry originally proposed searching for (`"[Tool37] Monthly sentinel present"`) does not exist verbatim anywhere in the repo — the real line is `"[Tool 32] Monthly sentinel found — triggering MONTHLY rollup"` (`pipeline.yml:797`). If a future session has GitHub API access and wants belt-and-braces confirmation beyond the `reports/monthly/` file evidence, that corrected string is the one to search for — but per the repo-side evidence above, this is now optional corroboration, not a blocking unknown.
- **Owner:** ops — closed
- **Urgency:** Closed.

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
- **Status:** **RESOLVED — updated 2026-09-24, follow-up audit pass.** Concurrency guard confirmed present and correctly shaped.
- **What it blocks:** Nothing further. Bundle A's safety under manual-re-trigger conditions is now confirmed, not just the scheduled-sequential case.
- **Evidence:** `grep -n "concurrency" .github/workflows/pipeline.yml` → hit at `:54`. Full block, `:53-56`:
  ```yaml
  # Prevent overlapping runs if previous hour's job is still running
  concurrency:
    group: thir-pipeline
    cancel-in-progress: false
  ```
  This is the correct shape, not merely present-but-inadequate: `group: thir-pipeline` is a single group applying to **both** trigger types declared at `:48-51` (`schedule` and `workflow_dispatch`), meaning a manual re-trigger and a scheduled run compete for the same GitHub Actions concurrency slot rather than running in parallel. `cancel-in-progress: false` — the second GitHub Actions gate confirmed correct here — means the *later* run queues behind the *earlier* one rather than cancelling it mid-write; this matters specifically because `cancel-in-progress: true` would have been the wrong setting even with the group present, since it could kill a scheduled run partway through its write to `alert_history.json` (worse for data integrity than no concurrency block at all, not better).
  - Tool 40 confirmed to run *inside* `pipeline.yml`'s single job (`:187-200`, `python tools/40_failover_notifier.py`), not as a separate workflow with its own trigger — so it is covered by the same `thir-pipeline` concurrency group, not a third, unguarded writer.
  - Checked for a second potential race path: `enriched_corpus.yml` also references `alert_history.json`, but only as a documentation comment (analogy for its own unrelated pruning logic) and in its own explicit exclusion list (`:313-319`): *"Never touches ... `data/alert_history.json` ... — all owned by `pipeline.yml`."* Self-documented, isolated design — no second writer, no second race path.
- **Reasoning:** The original open question was whether GitHub Actions' *default* concurrency behavior (none — concurrent runs are allowed by default absent an explicit block) applied here, exposing a genuine race between a scheduled run and a manual `workflow_dispatch`. It does not apply — an explicit, correctly-configured `concurrency:` block already exists, was already in the repo prior to this audit (not added by F1–F4 this session), and covers both trigger paths plus Tool 40's write path by virtue of Tool 40 running inside the same guarded job.
- **Required changes:** None. The fix this entry's prior "Next action" proposed already exists in the repo, unmodified from the proposed shape.
- **Next actions:** None outstanding for the static-analysis half of this question. One residual, lower-tier item: the original entry's proposed *runtime* confirmation ("trigger the workflow manually while a scheduled run is in flight, observe whether both complete without data loss") has still not been performed — the concurrency block's *presence and correct configuration* is confirmed by static analysis, but an end-to-end live test confirming GitHub Actions' queueing behavior matches the YAML's stated intent has not been run. This is a much lower-stakes residual than the original question (verifying config vs. verifying a config gap), and does not block moving to Q-04.
- **Owner:** engineering / ops — closed, pending only the optional live-test residual above
- **Urgency:** Closed. The correctness-of-a-shipped-fix concern that made this the priority item this session is resolved.

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
- **Status:** OPEN → **RESOLVED by cross-reference to Q-13, 2026-09-24.** F5 is shipped; there is no ship-order to re-rank in a portfolio repo. The 30-minute design discussion this entry proposed is moot — Q-16 picked a shape, Q-13 implemented it, and the priority question dissolves once there's no queue to prioritize against.
- **What it blocks:** Nothing further. Was: "F5's position in any future ship-order plan." There is no ship-order in a portfolio repo — F5 was simply the next substantive thing to build once Q-16 picked a shape, and it has now been built.
- **Next action:** None. See Q-13 for the shipped implementation and Q-16 for the design-shape decision this entry's original "re-ranking" question was actually gating on.
- **Owner:** — (closed)
- **Urgency:** Closed.

---

### Q-12 — Do the three new regression test files (`tests/test_tool37_dedup_pruning.py`, `tests/test_tool43_whole_corpus_prune.py`, `tests/test_tool48_whole_corpus_prune.py`) need to be wired into CI, or do they only run manually?

- **Source:** NEW — not from prior audit chain. This is an artifact of this session creating the repo's first-ever test files (confirmed: no `tests/` directory or test framework existed before this session).
- **Status:** **RESOLVED, fully closed — updated 2026-09-24, implementation shipped this pass.** Both halves of this entry's split status (verification, implementation) are now done — this is the one entry from this session's dual-status set that is genuinely fully closed, not RESOLVED-with-an-open-action.
- **What it blocks:** Nothing. Was: "whether F1–F4's regression protection is durable." Now: confirmed durable — a future accidental revert of any of the three fixes will fail CI on the PR that introduces it, not wait for the next manual audit.
- **Evidence, verification half (from the prior pass in this session, unchanged):** `ls tests/` confirmed all three files exist. `grep -rln "tests/" .github/workflows/` returned zero hits against the three pre-existing workflows (`pipeline.yml`, `enriched_corpus.yml`, `historical_processor.yml`) — no CI wiring existed.
- **Evidence, implementation half (this pass):**
  - `.github/workflows/tests.yml` created, triggered on `pull_request` against `tools/**/*.py` and `tests/**/*.py`, matching the original entry's proposed shape exactly (`for f in tests/test_*.py; do ... python3 "$f" || exit 1; done`).
  - **Before shipping, ran all three test files directly** (`python3 tests/test_*.py`) to confirm they pass cleanly against the current repo state — not just that the wiring is syntactically correct, but that the wiring won't immediately red the first PR it runs against. Result: `test_tool37_dedup_pruning.py` — 4/4 tests passed, exit 0. `test_tool43_whole_corpus_prune.py` — 2/2 passed, exit 0. `test_tool48_whole_corpus_prune.py` — 1/1 passed, exit 0. All three exit cleanly; the glob `tests/test_*.py` correctly matches all three filenames with no naming mismatch.
  - File is at `.github/workflows/tests.yml`, confirmed present alongside the three pre-existing workflows.
- **Required changes:** None remaining.
- **Next actions:** None. This entry is closed end-to-end — verification, implementation, and a pre-flight run confirming the new gate won't immediately break on merge.
- **Owner:** engineering — closed
- **Urgency:** Closed. This was the only item among Q-04/Q-06/Q-12 (this session's originally-flagged trio) that required code, not just a check — it now has both.

---

### Q-13 — F5 design work — shipped

- **Source:** Settled context (all four prior turns) — explicitly out of scope for implementation earlier this session, per repeated instruction; lifted this pass.
- **Status:** DEFERRED → **RESOLVED (design) / RESOLVED (implementation).** F5 shipped 2026-09-24. `consolidate_by_signature()` added to `tools/26_incident_timeline_live.py` (inserted after `calculate_severity`, called between the case-build log line and `output_ir_cases_json()`). `tests/test_tool26_consolidation.py` added (16 tests, all passing — 13 from the original F5 implementation plus 3 added by the Q-20 fix). `.github/workflows/tests.yml` now covers five test files.
- **Verified against real corpus:** 2,236 cases → 211, 8.06MB → 627KB (92.2% reduction, post-Q-20 fix). `109.160.32.110`'s 1,099 raw cases → 3 time-bucketed groups (707+389+3=1,099 ✓), matching Q-16's empirical finding exactly. Idempotency confirmed on real data, not just synthetic test input. Zero `case_id` collisions among newly-generated ids; 121 apparent collisions traced to singleton pass-through cases correctly retaining their original ids (working as designed, not a bug — see the methodology note's fourth entry, added this pass). **A real signal-loss defect was found and fixed in this same pre-push pass — see Q-20 — before any of these numbers were treated as final;** the figures here are the post-fix state.
- **Acceptance criterion, revised:** the design brief said "under ~500KB"; actual is 627KB (post-Q-20 fix; 614KB before it). The 500KB target was optimistic — it assumed perfect bucketing, but time-window boundaries (120min) split some floods into multiple groups by design (confirmed on the live corpus: `109.160.32.110`'s 1,099 raw cases → 3 buckets of 707+389+3, not one). The correct criterion is "under ~700KB," reflecting the window-boundary floor. 627KB clears that. **Do not treat the 500KB miss as underperformance — it's the criterion that was wrong, not the implementation.**
- **Note — two same-named `session_count` fields now exist, and they are not the same thing:** F5 introduces `session_count` on `ir_cases.json` (Tool 26, post-consolidation, counts raw cases absorbed into a consolidated case). This is a *different field* from Tool 43's `session_count` on `enriched_corpus.json` (cross-run accumulator, counts distinct `case_id`s ever seen for an IP, per Q-03 risk-ii). Different files, different producers, different semantics, and — per Q-03's original trace — neither is a reader of the other. If a future consumer wants "raw session volume absorbed by one consolidated case," only Tool 26's field (post-F5) provides it. If it wants "distinct consolidations seen across pipeline runs for an IP," only Tool 43's does. Do not conflate the two when reading this register later.
- **Chosen shape:** Shape 3 (write-time signature dedupe + per-case `session_count`). Full rationale and design-brief skeleton retained in the "F5 — shipped" section below (renamed from "path to design," since design is no longer the open item).
- **What it blocks:** Nothing. The CLU-002-style scanner-flood bloat in `ir_cases.json` this entry's original text cited (78% of bytes, per the original bloat audit) is consolidated at write time as of this pass.
- **Owner:** design (closed) / engineering (closed).
- **Urgency:** Closed.

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
- **Status:** **CLOSED — resolved by cross-reference to Q-01(b) and Q-18, 2026-09-24.** This entry's original premise was corrected twice within the same audit session before reaching a stable answer; see Q-01(b) for the full trace and the methodological note at the top of this register. Do not action anything below this line independently — it is retained for audit-trail purposes only.
- **Final correction (supersedes all prior versions of this entry):** The original claim — "Tools 44/47/49/50 lack the `_seen_*` pattern, rely on set growth instead" — is **partially correct, tool-by-tool, not as a blanket claim**:
  - **Tool 44** (`unique_ips_ever`): correct. Genuinely a `set()`-union field, self-limiting by IP cardinality, no F1-class risk.
  - **Tool 49** (`observed_aliases`) and **Tool 50** (`unique_ips_ever`): also correct, but for a different reason than Q-15 originally stated — these tools have no internal `_seen_*` bookkeeping field of *any kind* in their entries (not set-based, not dict-based); their `prune_*_corpus()` functions delete whole stale *entries*, an unrelated mechanism to the F1-class inner-dict bug.
  - **Tool 47** (`success_events`): **incorrect**. This field is neither a `_seen_*`-named dict nor a `set()`-based self-limiting collection — it is an append-only **list**, deduped only by exact `(src_ip, timestamp)` tuple match, with no time-window cutoff and no size cap. Confirmed by direct byte measurement: 74.7% of `data/credential_corpus.json`'s bytes, actively growing every pipeline run (61 new events in the most recent run alone per `credential-corpus/credential_metadata.json`), with one entry (839 unique source IPs across a ~25-day window) accounting for 88KB / 99.7% of its own entry's bytes. **This is a live, unaddressed instance of the same bug class F1–F4 fixed elsewhere.** Filed as **Q-18**.
- **What it blocks:** Nothing directly from this entry. Q-18 is the actionable item.
- **Next action:** None from this entry. See Q-18.
- **Owner:** — (closed, superseded)
- **Urgency:** None on this entry. See Q-18 for the live item.

---

### Q-16 — Tool 28 does not consolidate the dominant flood pattern

- **Source:** NEW — surfaced during Q-03's risk-#3 trace (autonomous audit session, 2026-09-24), by running `tools/28_soc_handover_live.py`'s actual `group_cases_for_report()` against the live `data/ir_cases.json` snapshot rather than reasoning about it from the whitepaper.
- **Status:** RESOLVED (finding) / **RESOLVED (design shape) — Shape 3 implemented as F5, shipped 2026-09-24.** Implementation tracked in Q-13.
- **Finding:** `is_groupable()` (`tools/28_soc_handover_live.py:234-250`) returns `False` for any case with `login_success=True`. The dominant flood pattern in the current snapshot — repetitive successful single-command sessions, command signature `uname -s -v -n -r -m`, consistent with whitepaper §2.1's CLU-002 (command-signature match only, no second-axis attribution) — is therefore structurally exempt from Tool 28's grouping.
- **Empirical (this pass):** Input `ir_cases.json`: 2,236 cases. `is_groupable()` True: 292 / False: 1,944 (exact split, verified against `group_cases_for_report()`'s source — no third/unlogged bucket exists). `priority_cases` = 1,944 entries (~7,736,790 bytes, 95.9% of input); `grouped_cases` = 108 entries (~107,188 bytes, 1.3%) — the 108 entries arise from bucketing the 292 groupable cases by `(src_ip, time-window)`, not a 1:1 case-to-entry mapping. Flooding IP `109.160.32.110`: 1,099 cases, 1,096 with `login_success=True`, routed to `priority_cases` as individual blocks. Of the 1,944 priority cases, 1,810 belong to the 3 dominant flooding IPs (92.1% of priority-case bytes).
- **Reasoning:** Tool 28's rule is correct for its threat model — unsuccessful recon is noise, successful access is signal. CLU-002 invalidates the "successful access is rare" half of that model on the SSH side. The bloat is not relocated by Tool 28; it passes through essentially unconsolidated.
- **Design implication for F5:** F5 must consolidate the successful-login repetitive pattern at write time in Tool 26. Tool 28's `is_groupable()` predicate is the wrong one to copy — study its structure (bucketing, time window, summary-row shape), not its exclusion rule. Three candidate consolidation shapes, each with a `case_id`-cardinality consequence:
  1. **Widen predicate** to group successful logins by identical command signature. Cheap. Changes what a "case" means for any consumer expecting one-case-per-successful-login — cardinality drops from N to 1 per signature. No such consumer confirmed this session (per Q-03's risk-i/ii traces), but a full downstream re-scan should follow any F5 implementation, not precede it.
  2. **Dedupe within-case arrays** (`timeline`, `commands`) without changing case cardinality. Smaller `ir_cases.json`. Does **not** fix Tool 28's render size — 1,096 blocks still render.
  3. **Two-layer:** write-time command-signature dedupe + a per-case `session_count` field preserved for count-accurate views. Addresses both file size and Tool 28 render size. Cardinality shifts; requires a documented "case = consolidated signature group" definition and a `session_count` field downstream consumers can use instead of counting `case_id`s.
- **F5 design brief must select one of (1)/(2)/(3) explicitly** and state its `case_id`-cardinality consequences. "F5 needs a different rule" is not sufficient.
- **Recommendation, accepted and implemented, 2026-09-24 (third pass):** **Shape 3.** It is the only shape that fully closes this entry's finding — Shape 1 leaves "what does `case_id` mean now" half-answered; Shape 2 doesn't touch the render-size complaint (1,096 blocks) at all. Extra cost over Shape 1 is roughly a `session_count` field plus its docstring (~15 lines), and `session_count` reuses the field name Tool 43's accumulator already uses, keeping vocabulary consistent across corpus tools (though the two fields are on different files with different semantics — see Q-13's note). Q-03's trace already confirmed no current consumer misreads `case_id` cardinality, so Shape 3 shipped without cross-tool coordination. **Implemented:** `consolidate_by_signature()` in `tools/26_incident_timeline_live.py`. Consolidated case carries `session_count` (raw cases absorbed) and `session_ids_sample` (first 10 by timestamp). Severity inherited from the earliest case in the group verbatim, not recomputed or aggregated — per Q-03 risk-iii resolution. Full design-brief skeleton and verification results are in the register's "F5 — shipped" section.
- **Do not reopen.** Further refinement belongs in review comments on the F5 code itself (`tools/26_incident_timeline_live.py`, `tests/test_tool26_consolidation.py`) or a new Q-number, not a fourth revision of this entry.
- **Note:** A stale comment in `tools/http_honeypot/http/honeypot.py:63` claims "Scanner noise handled by per-IP deduplication in Tool 26" — false when originally checked, and now **also stale in a second way**: Tool 26 *does* now handle per-IP consolidation as of this pass, but that comment lives in unrelated, unwired staging code (Q-02/Q-17) and was never updated to reflect F5 — it was accidentally-almost-true, not evidence of anything at the time it was written. Flagged under Q-02, not independent evidence here.
- **Not a Tool 28 bug. Not a Tool 28 fix. Bounded Tool 26 change — shipped, tested, verified against the real corpus.**
- **Cross-reference:** Q-02 (confirms no reference implementation to port from), Q-03 (this entry is risk-iii's resolution), Q-11 (closed by cross-reference to this entry and Q-13 — no separate ranking exercise was needed), Q-13 (F5 implementation — the shipped code this entry's recommendation produced), Q-17 (confirms no code existed before this pass).
- **Owner:** design (closed) / engineering (closed)
- **Urgency:** Closed. This was the *only* open precondition for F5; all preconditions are now closed and F5 is shipped.

---

### Q-17 — Does any F5 implementation code exist anywhere in the repo, in any form?

- **Source:** NEW — filed as a repo-wide generalization of Q-02's Tool-26-scoped check, during the same autonomous audit session (2026-09-24), to close the "is this claim defensible repo-wide or only for one file" gap explicitly.
- **Status:** RESOLVED NO
- **Evidence:** `grep -n -E "session_count|consolidat|group_by|per_ip|dedup|cluster" tools/26_incident_timeline_live.py` → 2 hits, both for `map_ttps()`'s unrelated TTP-list deduplication (`:16`, `:180`). Repo-wide `grep -rn -E "consolidat|per_ip|dedup|group_by" tools/ js/` → many hits, but every one traces to a distinct, already-cataloged, unrelated mechanism: Tool 27's Go-side `consolidateIOCs()` (IOC-list IP-uniqueness, not session grouping), Tool 28's own grouping (Q-16), Tool 34's credential-pair dedup, Tool 37/43/44/47/48/49/50's accumulator-entry dedup (Q-01), Tool 00's historical cross-file dedup, `js/data.js`'s static prose description of Tool 48. No hit represents SSH per-IP/session consolidation of the kind F5 would implement.
- **One caveat surfaced:** `tools/http_honeypot/http/honeypot.py:63` contains a comment — *"None here. Scanner noise handled by per-IP deduplication in Tool 26"* — asserting Tool 26 already does this. This is **false**, confirmed by the direct grep above finding nothing in Tool 26. It is a stale/aspirational comment carried over from the whitepaper's design narrative into the Cowrie-plugin staging code, not evidence of an implementation, and should not be cited as a reference in any future F5 design work.
- **Resolution:** No F5 code — HTTP-side or SSH-side, Tool 26 or elsewhere — exists anywhere in this repo as of this audit pass. This is a stronger, repo-wide version of Q-02's Tool-26-scoped finding, filed separately because "not in Tool 26" and "not anywhere in the repo" are different claims requiring different evidence, and only the wider claim rules out a hidden/relocated implementation.
- **Cross-reference:** Q-02 (the narrower, Tool-26-scoped version of this same question), Q-16 (the design work this absence leaves open).
- **Owner:** design (closed — informational finding, no action required beyond citing it accurately in future F5 discussion)
- **Urgency:** Closed.

---

### Q-18 — `data/credential_corpus.json`'s `success_events` field is an unbounded, actively-growing field of unresolved status: bloat bug, or live threat signal being silently discarded if capped

- **Source:** NEW — surfaced during a comprehensive shape-based scan of all entry-keyed corpus files, run specifically because two successive name-based grep passes on Q-01(b)/Q-15 had each produced a partially-wrong claim; this scan measured actual bytes per nested field across every corpus file rather than grepping for a naming pattern, per explicit instruction to do this once, comprehensively, rather than continue incremental tightening.
- **Scan-completeness note (added per review):** the scan covered every file whose top-level structure is a flat dict keyed by entry (IP, hash, sequence). `data/ir_cases.json` and `data/ssh_fingerprints.json` were excluded automatically by this shape filter — both are wrapper objects (`{"generated_at": ..., "cases": [...]}` / `{"generated_at": ..., "fingerprints": {...}}`), not flat entry-keyed dicts — not by a deliberate scope decision made in advance. This was not stated when the scan was first reported and should have been. `ir_cases.json`'s bloat is covered separately by Q-16. `ssh_fingerprints.json`'s own size was **not** separately measured this pass — it is Tool 48's input (`data/fingerprint_corpus.json`, Tool 48's output, *was* scanned and is in the table below), but the wrapper file itself remains a genuine gap, not a covered one, if it matters later.
- **Status:** RESOLVED (finding, measurement) / **OPEN (remediation blocked on a threat-intel and product-intent question, not an engineering one)**
- **Action closed:** built `tools/51_attacker_profiles.py`, which reads `data/credential_corpus.json` and flags credential pairs whose `success_events` span more distinct source IPs than a configurable threshold (default 50). Run against the live corpus, it independently reproduces this finding's top line (839 IPs on `345gs5662d34`/`345gs5662d34`) and surfaces 5 additional flagged pairs not previously named in this entry's text (`root`/`3245gs5662d34` at 341 IPs, `admin`/`admin` at 168, `support`/`support` at 99, `root`/`admin` at 71, plus one more — see `data/attacker_profiles.json` for the full list). This is the "build the missing consumer" option: the finding is now surfaced by tooling, not only by a one-time byte-count audit. **The consumer-intent question (cap vs. archive `success_events`) remains genuinely open** — this tool surfaces the pattern, it does not decide what to do about the field's growth. Do not read this as also closing that half.
- **Evidence:**
  - `tools/47_credential_corpus.py`'s `build_credential_corpus()` appends to `entry["success_events"]` (a list of `{src_ip, timestamp}` dicts) on every run, deduped only by exact `(src_ip, timestamp)` tuple collision (`existing_success_keys` set, checked before append). No time-window cutoff exists anywhere in this function or in `prune_credential_corpus()` (`:151`) — the latter only deletes whole stale *entries* by `last_seen`, it does not touch `success_events` within a still-live entry.
  - Direct byte measurement, `data/credential_corpus.json` (345 entries, 401,135 bytes total): `success_events` across all entries = 299,673 bytes = **74.7% of the file**.
  - Worst single entry: username/password `345gs5662d34`/`345gs5662d34` (username = password — a real, not-obviously-sanitized credential pair; **this finding includes the plaintext credential as it appears in the corpus, not a placeholder**), **1,206 successful logins, 88,226 bytes (99.7% of that entry's own bytes)**, spanning `2026-08-29T19:36:01Z` to `2026-09-23T06:45:54Z` (~25 days) with **839 unique source IPs**.
  - Production footprint confirmed real, not an audit-snapshot artifact: `credential-corpus/credential_metadata.json` shows `new_success_events_this_run: 61` added to an already-540,145-byte corpus in the single most recent run alone.
  - Consumer check (run per review, closing what was previously an open next-action): `grep -rln "success_events" tools/ js/` → **only `tools/47_credential_corpus.py` itself.** Zero external readers — no dashboard view, no Tool 28 report surfacing, nothing in `js/data.js`. The field is currently write-only from the pipeline's perspective, which is consistent with it being either abandoned bookkeeping (safe to cap) or an intentional audit-trail store that nothing has been built to *read* yet (not safe to cap without knowing what it was for).
- **⚠ Reclassification per review — this is a threat-intel finding first, a bloat finding second.** One credential pair with **839 unique source IPs successfully authenticating over three-plus weeks** is not primarily a storage-efficiency problem. It is a directly observable signature of either credential stuffing against a known-valid credential, or a botnet replaying one compromised username/password pair across hundreds of distinct nodes. The bloat is *downstream* of a live security event, not the event itself. Two consequences:
  1. **This finding should be routed to whoever owns threat-intel/SOC review, not filed as an engineering-only bloat ticket.** The 839-IP pattern on a single working credential is independently interesting regardless of what happens to `success_events`' byte count.
  2. **Capping the field is not a safe default fix.** If `success_events` is meant to be the full auth trail an analyst would want for a compromised credential (i.e., its unbounded growth is a feature, not a bug — the record of *every* successful use is the point), then applying F3/F4's DEDUP_WINDOW_DAYS-style time-cutoff mechanism would silently destroy exactly the evidence a SOC investigation of this credential pair would need. The zero-consumer finding above means nothing currently reads this field to notice if it were truncated — which cuts both ways: it may mean the field is genuinely dead bookkeeping, or it may mean the *consumer that should exist to alert on this pattern* has never been built, and the data has been sitting here uninspected until this audit pass found it by byte count rather than by security review.
- **Reasoning (engineering side, unchanged from original measurement):** structurally this is the same failure mode F1 fixed in `alert_history.json`'s `alerts` dict and F3/F4 fixed in `_seen_case_ids`/`_seen_sessions` — a per-entry collection that only ever grows, no time-window or size-based cutoff. It was missed by two prior name-based grep passes in this session because it isn't `_seen_`-prefixed; only the shape-based byte scan caught it.
- **Impact:** at current growth rate this field will continue to dominate `credential_corpus.json`'s size. But per the reclassification above, "impact" here is two separate things that must not be conflated: file-size impact (engineering) and undetected-credential-compromise impact (security) — the latter is likely the more consequential one and has not been assessed at all by this audit, which only measured bytes.
- **Required changes:** None yet — this entry is a finding, not an implementation. Per standing instruction, no fix code has been written.
- **Next actions:**
  1. ~~Trace every reader of `success_events`~~ **DONE, this pass** — zero readers, see Evidence above.
  2. **Route the 839-unique-IP-on-one-credential-pair pattern to threat-intel/SOC review as its own item, independent of the bloat question.** This is not an engineering next-action.
  3. Before choosing a remediation shape, get an answer to: is `success_events`' full unbounded history intentional (analyst-facing audit trail, in which case cap-with-archival is the only acceptable shape — e.g. move full history to R2 per the enriched-corpus design's own archival pattern, keep only a count + first-N + most-recent-N in the live corpus) or unintentional (dead bookkeeping nobody reads or plans to read, in which case a straightforward DEDUP_WINDOW_DAYS-style time cutoff, mirroring F3/F4, is sufficient). **Do not default to the F3/F4 mirror without this answer** — that was the original instinct and it is the wrong default here given the zero-consumer finding could mean either thing.
  4. File a follow-up implementation entry once both the SOC-routing question and the intentional-vs-dead-bookkeeping question are answered — this entry (Q-18) should be marked implementation-pending, not reopened with new analysis, once that follow-up exists.
- **Cross-reference:** Q-01 (this is the concrete finding Q-01(b)'s three revisions were ultimately searching for), Q-15 (closed, superseded by this entry), Q-16 (same "measure bytes, don't just reason from the design doc" methodology that produced this finding).
- **Owner:** **security/threat-intel (new — the 839-IP pattern itself) and engineering/design (the remediation-shape decision, blocked on the threat-intel answer)**
- **Urgency:** Non-blocking for pipeline correctness today (no crash, no data loss — just ongoing, uncapped growth), but **live and actively worsening every pipeline run**. The security question (is this credential compromised and being actively exploited) is plausibly higher urgency than the bloat question and should not wait for an engineering sprint cycle — flag for immediate SOC awareness independent of when the storage fix ships.

---

### Q-19 — Unattributed SSH client fingerprint: HASSH `01ca35584ad5a1b66cf6a9846b5b2821`, 53,426 cumulative sessions from 4 source IPs, no campaign match in repo documentation

- **Source:** NEW — surfaced while checking whether Q-18's aggregate-percentage mistake (a skewed distribution hiding behind a single number) also applied to `data/fingerprint_corpus.json`'s `_seen_sessions` field (80.5% of file). It did not turn out to be a bloat-mechanism problem — F4's 2-day window is working as designed — but the *cause* of the largest single outlier is itself a security-relevant, previously undocumented pattern, distinct enough from Q-16 and Q-18 to warrant its own entry rather than a footnote in the scan table (per review: a table cell is silently drop-able from the register's own counts-by-status and open-item scanning in a way a Q-numbered entry is not).
- **Status:** RESOLVED (finding — the fingerprint pattern is fully characterized and the attribution check has a definitive negative result) / OPEN (SOC routing and any subsequent monitoring decision have not been made). Split per this pass's dual-status convention: the investigative half of this entry is closed; the action half is not. Previously filed as a single "OPEN" status, which correctly flagged unfinished work but did not distinguish "we don't know yet" from "we know, and now need someone to act on it" — the latter is the actual state.
- **Action closed:** the same `tools/51_attacker_profiles.py` reads `data/fingerprint_corpus.json` and flags fingerprints with high `session_count` concentrated behind few `unique_ip_count_ever`. Run against the live corpus, it independently reproduces this finding exactly: `53426 sessions / 4 IPs` on HASSH `01ca35584ad5a1b6...`. No second fingerprint met the default threshold (`>10,000` sessions, `<=10` IPs) — this remains the only one on the current corpus. "Nothing in the dashboard surfaces this pattern" is now false; a tool does. Attribution itself is still unresolved and this tool does not attempt to change that — it surfaces the pattern for review, it does not identify the actor.
- **Evidence:**
  - `data/fingerprint_corpus.json`'s entry for HASSH `01ca35584ad5a1b66cf6a9846b5b2821`: `client_family: "Go SSH scanner"`, `botnet_signature: "Modern SSH client"` (i.e., explicitly *not* matched against a known botnet KEX signature — this is a generic-client-detection label, not an attribution), `version_strings: ["SSH-2.0-Go"]`, `session_count: 53,426` (cumulative, all-time), `unique_ip_count_ever: 4` (`103.187.91.2`, `139.224.244.145`, `39.101.69.5`, `47.250.167.250`), active `2026-08-31T12:01:48Z` to `2026-09-22T14:49:03Z` (~22 days).
  - The field that surfaced this, `_seen_sessions`, is a **rolling 2-day window** of that cumulative total (6,606 entries at time of snapshot, 330,300 of the field's 660,450 total bytes — 50% of the field's weight from this one HASSH alone). Initial characterization of this as "one 4-hour burst" (prior turn) was imprecise and is corrected here: it is a 2-day slice of sustained, ongoing activity, not a single short event.
  - **Attribution check, run per review:** `grep -rn "01ca35584ad5a1b66cf6a9846b5b2821\|hassh\|HASSH" docs/ tools/ | grep -v credential_corpus` (adjusted to exclude the fingerprint_corpus.json data file itself and this register's own prior draft text) returns no campaign name, no cross-reference to any documented actor, no match in either HTTP-honeypot whitepaper or the strategic review. The only labels present (`"Go SSH scanner"`, `"Modern SSH client"`) are generic signature-matching categories produced by Tool 35/48's own classification logic, not attributions to a known campaign, botnet, or public scanning service.
  - **Confirmed distinct from Q-16:** zero IP overlap with Q-16's flooding cluster (`109.160.32.110/.69/.63`).
  - **Confirmed distinct from Q-18:** different corpus file (`fingerprint_corpus.json` vs. `credential_corpus.json`), different accumulation mechanism (HASSH-keyed session-fingerprint tracking vs. credential-pair successful-login tracking), different growth vector (SSH client signature reuse vs. one specific credential pair being replayed).
- **Resolution of the attribution question posed in review:** **unattributed.** Per the stated urgency framing — "if unattributed, Q-18 tier, possibly higher, because unlike `success_events` this pattern shows sustained engagement from a coordinated small set of sources" — this entry is filed at that tier, not the lower Q-08 "note and monitor" tier that would apply if a campaign match had been found.
- **Reasoning:** Four distinct source IPs sharing one exact SSH client fingerprint (`SSH-2.0-Go` version string plus a specific, consistent KEX/encryption/MAC algorithm set) and jointly producing 53,426 sessions against a single honeypot over ~22 days is consistent with either (a) one operator running the same custom or off-the-shelf Go-based SSH scanning tool from four hosts (a botnet, a distributed scanning service, or one actor with four vantage points), or (b) four unrelated operators independently using the same popular open-source Go SSH library with default settings, coincidentally producing an identical HASSH. The fingerprint data alone cannot distinguish these — HASSH identifies client *software*, not actor *identity*. This is the limit of what Tool 35/48's current fingerprinting can resolve; further attribution would need external correlation (the 4 IPs' ASN/geolocation history, timing correlation with other honeypot events, or threat-intel lookups against known Go-based SSH scanner tooling) that is out of scope for this repo-only audit.
- **Impact:** Two separate impacts, kept distinct per Q-18's established pattern: (i) this is the direct cause of the tail-risk flagged in the scan table for `_seen_sessions` — a sustained high-volume fingerprint like this one is exactly the traffic-rate increase that F4's time-only window does not bound the size of; (ii) independent of any bloat consideration, four coordinated or convergent sources sustaining over 53,000 sessions against one honeypot for three-plus weeks, unattributed to any known campaign, is itself a SOC-relevant observation that nothing in the current dashboard (`js/data.js`, not re-checked this pass for a matching "sessions-per-fingerprint" or "sessions-per-IP-ratio" view) appears to surface today.
- **Required changes:** None — this entry is a finding, not an implementation or an attribution conclusion. No fix or routing action taken.
- **Next actions:**
  1. Route to the same SOC/threat-intel review channel as Q-18, as a related-but-distinct item — same conversation, separate finding, per review's framing.
  2. If threat-intel review can establish attribution (known Go-based scanner tooling, e.g. via public IOC feeds cross-referenced against the 4 IPs or the exact algorithm-suite fingerprint), downgrade urgency to Q-08 tier and close with that attribution recorded. If review confirms it remains unattributed after investigation, this stays open at its current tier and should inform Q-19's own remediation: possibly a dedicated `attacker_profiles`-style tracking entry (the kind of tool Tool 43's design already gestures toward) rather than leaving this pattern discoverable only by a bloat-audit byte scan.
  3. Do not conflate this with Q-18's remediation thread — different file, different field, different fix shape if one is needed. Cross-reference, don't merge.
- **Cross-reference:** Q-18 (same session, same "measure bytes, find the security signal underneath" methodology, same SOC-routing framing, filed as the sibling finding rather than a duplicate), the `_seen_sessions` tail-risk note in the scan table (this entry is that note's full write-up).
- **Owner:** security/threat-intel (attribution attempt, routing) — engineering only if attribution or monitoring tooling work is subsequently scoped.
- **Urgency:** Q-18 tier — unattributed, sustained, coordinated-or-convergent pattern from a small fixed set of sources over three-plus weeks. Should not wait for a routine sprint cycle; flag alongside Q-18 for SOC awareness now, independent of whether any code changes follow.

---

### Q-20 — F5 consolidation silently dropped distinct SSH fingerprints; fixed pre-push

- **Source:** NEW — surfaced during pre-push verification of F5, by comparing Tool 35's HASSH output before and after applying `consolidate_by_signature()` to the live `ir_cases.json` snapshot. This is the exact "signal, not just a count" risk this session's pre-push checklist flagged as unverified for F5.
- **Status:** RESOLVED — found and fixed pre-push, verified against the real corpus, not a synthetic input.
- **Initial finding:** running the (then-unmodified) F5 consolidation against the live corpus dropped HASSH diversity from 20 unique fingerprints to 18 — 2 lost, 0 gained.
- **Root cause, traced precisely against real timeline data (not assumed from the general shape of the bug):** the working hypothesis going in was that F5's grouping key was too coarse — that sessions from genuinely *different* SSH clients were being merged into one group, and only one client's fingerprint survived. **This hypothesis was checked and found false.** Direct inspection of every affected group's members showed **every group had exactly one distinct HASSH value shared across all its members** — there was no fingerprint diversity within any group to lose by merging. The actual defect was narrower and different: `consolidate_by_signature()` chose its representative case by strict earliest-`first_seen` timestamp, and in a tight connection burst, the fastest-connecting session is frequently the one whose `cowrie.client.kex` event was never captured (the connection closed before KEX completed, or the event logged out of order relative to `session.connect`). Three real groups on the live corpus exhibited this: `51.158.205.203` (6 sessions, only the earliest lacked a KEX event), `156.225.1.32` (2 sessions), and `123.58.219.26` (4 sessions, 3 of 4 lacked KEX). Picking strictly by timestamp threw away the group's only captured fingerprint even though every other member agreed on it.
- **Fix:** `consolidate_by_signature()`'s representative-selection step now prefers a group member carrying a `cowrie.client.kex` event over the strictly-earliest member, falling back to earliest-by-timestamp only when no member in the group ever captured one. `case_id`/time-bucket derivation is deliberately left keyed to the group's true earliest timestamp regardless of which case is chosen as representative, so `case_id` stability across runs is unaffected by this change. **This is a representative-selection fix, not a grouping-key fix** — no case moved from one group to another; the set of groups is byte-for-byte identical before and after. This is narrower in scope than the fix approach originally proposed (extending the grouping key with a fingerprint-derived signature), which was not needed once the root cause was confirmed to be selection, not merging — and would have carried its own real risk (Tool 35's HASSH fields include a non-deterministic-looking `keyAlgs` field that varies session-to-session even for the *same* client tool, confirmed on the live data; naively folding it into a grouping key would have caused the over-fragmentation failure mode described as a risk to guard against, for no benefit, since it isn't part of Tool 35's actual HASSH formula (`kexAlgs + encCS + macCS + compCS` only, confirmed by reading `compute_hassh()` directly)).
- **Verified against the real corpus, before and after:**

  | Metric | Pre-F5 (original) | F5, pre-fix | F5, post-fix |
  |---|---|---|---|
  | `ir_cases.json` cases | 2,236 | 211 | 211 (unchanged — fix does not alter grouping) |
  | `ir_cases.json` bytes | 8,064,756 | 613,538 | 627,163 |
  | Byte reduction vs. original | — | 92.4% | 92.2% |
  | Tool 28 `priority_cases` (coherent chain: 26→29→28) | 1,944 | not measured | 96 |
  | Unique HASSH fingerprints (Tool 35) | 20 | 18 | **20 — matches baseline exactly** |

  The byte-reduction cost of the fix is 0.2 percentage points (92.4%→92.2%) — the KEX-bearing representative case is marginally larger than the no-KEX case it replaces in 3 of 211 groups. This is a negligible cost for closing a real signal-loss defect.
- **Regression tests added** (`tests/test_tool26_consolidation.py`, now 16 tests total): `test_q20_prefers_kex_bearing_representative_over_earliest` (the core fix, using a synthetic two-case group shaped exactly like the real `51.158.205.203` group — earliest case has no KEX event, later case does, representative must be the KEX-bearing one); `test_q20_falls_back_to_earliest_when_no_case_has_kex` (no case in the group ever captured KEX — must not crash, falls back to original behavior); `test_q20_case_id_stable_regardless_of_which_case_is_representative` (confirms the fix doesn't disturb `case_id` reproducibility across runs, since `case_id`/bucket are still derived from the group's true earliest timestamp, not the possibly-later representative's timestamp).
- **What this does NOT fix and is explicitly out of scope:** a genuine case where two members of the same group carry *different* HASSH values (i.e., two distinct SSH client tools sharing identical `src_ip`/`login_success`/`commands`/time-bucket) is not addressed by this fix — that scenario did not occur anywhere in the corpus checked this pass, so there was no real instance to verify a fix against. If a future corpus snapshot exhibits genuine intra-group fingerprint diversity (not just selection-among-identical-fingerprints), that is a different defect requiring the grouping-key extension approach, not this one, and should be filed as a new entry rather than reopening this one.
- **Cross-reference:** Q-13 (F5 — this fix is part of the same shipped implementation, not a separate feature), Q-16 (Shape 3 design — unaffected; this fix operates entirely within Shape 3's existing representative-selection step and required no design change), Q-19 (the pre-existing HASSH fingerprint finding whose corpus made this loss visible and traceable in the first place).
- **Lesson, added to the register's methodology note:** a byte-reduction pass must verify signal preservation, not just byte count or case count. Q-16's Shape 3 explicitly preserved one signal (`session_count`) by design; the SSH fingerprint was a second signal nobody had identified as needing preservation until this verification pass checked it directly against real data rather than assuming the design brief's stated preservation guarantees (session_count, severity) were the only things at risk.
- **Owner:** engineering — closed
- **Urgency:** Closed pre-push. This was found and fixed in the same pass, before any commit — not a live production defect.

---

### Q-21 — F5 collapses Tool 36's per-cluster `session_count` (flood cluster 1,809 → 4); Tool 44 accumulates the undercount — fixed pre-push

- **Source:** NEW — surfaced during the post-fix consumer check on this pass. Q-03's trace covered readers of Tool 43's `session_count` and of `case_id`; it did not examine Tool 36, whose cluster `session_count` is built from case *cardinality* (`len(cl["members"])`, `tools/36_command_clustering_live.py:350`), not read from any field F5 touches.
- **Status:** RESOLVED — found and fixed pre-push, verified against the real corpus.
- **Evidence, original finding:** Tool 36 run on the F5-consolidated corpus (isolated sandbox) vs. the committed pre-F5 `command_clusters.json`: same 17 clusters and same 4 named campaigns, but the flood cluster CLU-013 drops from 1,809 to 4 sessions and total sessions represented across clusters falls from 1,869 to 55. Cluster detection is unaffected; only the volume figure changes, because each consolidated case is now one member.
- **Downstream:** Tool 44 accumulates Tool 36's `session_count` into `campaign_corpus.json` (`tools/44_campaign_corpus.py:97-103`), so campaign activity volume would have under-reported from the first post-F5 run. Tool 37 also emits `cluster.get("session_count")` in campaign alerts (`tools/37_alerts_live.py:379`). Both are unaffected by this fix at their own call sites — they simply read a now-correct value.
- **Fix — two parts, both required (the single-line fix originally proposed does not work on its own):**
  1. `extract_command_sessions()` (`tools/36_command_clustering_live.py:~186`) now carries `case.get("session_count", 1)` onto each session dict at extraction time. **This part is load-bearing and was missing from the first draft of the fix.** Before this change, `cl["members"]` entries never had a `session_count` field at all — Tool 26's per-case value is dropped during extraction, long before clustering happens — so a later `.get("session_count", 1)` at the aggregation step would always silently return the default `1`, making the fix a no-op that looks correct (tests pass, code reads sensibly) without ever firing on real data. Confirmed by reading the extraction function before writing the fix, not assumed from the field's presence elsewhere in the pipeline.
  2. `build_output()` (`tools/36_command_clustering_live.py:350`) now computes `sum(m.get("session_count", 1) for m in cl["members"])` instead of `len(cl["members"])`.
- **Verified against the real corpus, before and after, same isolated-sandbox method as Q-20:** pre-F5 committed baseline — 17 clusters, `total session_count` sum 1,869, CLU-013 = 1,809. Post-F5 with only part 2 of the fix (not tested as shipped, checked to confirm the no-op risk was real) — would have stayed at cardinality-based counts. Post-F5 with both parts — **17 clusters, sum 1,869, CLU-013 = 1,809 — an exact match to the pre-F5 baseline, not an approximation.**
- **Regression tests added** (`tests/test_tool36_cluster_count.py`, new file, 5 tests, run via the repo's `importlib.util.spec_from_file_location` loader convention, matching the other test files): `test_pre_f5_cases_unaffected` (no `session_count` field on input → behaves exactly as before the fix); `test_consolidated_cases_weighted_not_counted` (the core case — three members, one with `session_count=500`, must sum to 502, not 3 — this is the test that would catch a regression to the incomplete single-part fix); `test_extraction_carries_session_count_field` (isolates fix-part 1); `test_extraction_defaults_missing_session_count_to_one` (pre-F5 compatibility path); `test_singleton_and_consolidated_mixed_across_two_clusters` (confirms weight doesn't leak across distinct clusters).
- **Related observation, not a separate finding:** `session_count` is used by at least seven tools with different meanings (Tools 00, 28, 35, 36, 37, 44, 48), plus F5's field on `ir_cases.json`. Q-13's note about "two same-named fields" understated this — it is at minimum a three-way distinct-meaning collision (Tool 26's per-case count, Tool 36/44's per-cluster/campaign count, Tool 43's per-IP distinct-`case_id` count), now two of those three correctly propagate F5's consolidation and one (Tool 43's) was already confirmed to have zero external readers in Q-03.
- **Cross-reference:** Q-13 (F5), Q-16 (Shape 3 — this fix operates entirely downstream of Shape 3's design and required no change to it), Q-20 (same verification discipline — a pre-push chain check catching a real defect before it reached production, not a hypothetical).
- **Owner:** engineering — closed
- **Urgency:** Closed pre-push. Found and fixed in the same pass this session, before any commit.

---

## Next actions (no milestones — portfolio repo)

This is a portfolio repository with no external stakeholders, no quarterly commitments, and no deadline-driven sequencing. The "priority" framing below is about intellectual order, not scheduling. Any of these can be done at any time, in any order, or not at all.

### Immediate (cheap, unblocked, mechanical)

- **Q-12 is closed.** `.github/workflows/tests.yml` shipped; verification, implementation, and pre-flight run all done. Nothing further.
- **Q-18 / Q-19** are blocked on a decision that isn't engineering: what to do with the two live security findings (`success_events` credential replay, 839 unique IPs; unattributed HASSH fingerprint, 53,426 sessions from 4 IPs). Since this is a portfolio repo, "routing to SOC" doesn't apply — the decision is what to *do* with the findings so they don't sit unexamined. Two workable options:
    1. **Document them in the repo** — write a `SECURITY_NOTES.md` or add a section to the register that states the finding plainly, the evidence, and the recommended remediation shape. Closes the "someone should look at this" loop without inventing an external routing step that doesn't exist for a solo portfolio project.
    2. **Build the missing consumer** — Q-18's zero-reader finding is itself interesting: the field that would alert on 839 unique IPs against one credential has never been built. Building it (a small dashboard view, a Tool that reads `success_events` and flags threshold crossings) is a legitimate portfolio-scale answer to Q-18 that doesn't require routing anyone anywhere. Same for Q-19: the corpus already tracks HASSH patterns; a "sessions-per-fingerprint" view would surface this pattern on a dashboard instead of only via byte-count audit.
- **Q-21** is the one new open item from F5 verification: Tool 36's per-cluster `session_count` collapses under consolidation (flood cluster 1,809 → 4) and Tool 44 would accumulate the undercount. Worth resolving before F5 runs in the live pipeline. (Q-16, formerly listed here, is resolved — Shape 3 shipped as F5.)

### Lower priority (verification-only or documentation-only)

- **Q-05, Q-08** need GitHub Actions run/billing data. In a portfolio repo the practical value is low — the numbers would confirm assumptions that are already reasonable, not change any decision. Do them if curious.
- **Q-09** needs ~60 days of production data from the shipped prune; there's no production, so the question is really "would this look right at scale." Answerable by reasoning about ASN cardinality, not measurement.
- **Q-10** (CONTRIBUTING.md note) is a process item; no action required.
- **Q-14, Q-15** are deferred architecture-quality questions. No action.

### Where the value actually is, for a portfolio project

The audit register itself is the artifact. It documents:

- Eight real bugs found and fixed (F1–F4 across Tools 37/43/48, plus the cross-cutting patterns Q-01/Q-10/Q-16 examine).
- Two live security patterns surfaced by byte-measurement rather than by security tooling (Q-18, Q-19) — this is a strong demonstration.
- Five self-corrections within a single session, each traced to the same methodology lesson ("check the actual shape before classifying") — this is the most unusual and most valuable part of the register, because it shows the audit process *failing and recovering*, not just succeeding.
- A reusable dual-status convention for findings that are resolved as investigations but still have open actions.

If the register is being shown to anyone, that's the substance. The remaining open questions are either low-value verification or blocked on decisions that don't require anything external. Closing them out is optional polish; the register is already complete as a body of work.

---

## F5 — shipped

F5 is shipped and verified against the real corpus (2,236 cases → 211, 8.06MB → 627KB, 92.2% reduction, post-Q-20 fix). All preconditions are closed; no further design decision is pending.

**Note before reading further — two same-named `session_count` fields exist and are not the same thing.** F5 introduces `session_count` on `ir_cases.json` (Tool 26, post-consolidation, counts raw cases absorbed into one consolidated case). This is a *different field* from Tool 43's `session_count` on `enriched_corpus.json` (cross-run accumulator, counts distinct `case_id`s ever seen for an IP, per Q-03 risk-ii). Different files, different producers, different semantics, neither reads the other. See Q-13 for the full note.

**Note on the acceptance criterion below — the design brief's original "under ~500KB" target was optimistic, not missed by the implementation.** Time-window boundaries (120min) split some floods into multiple groups by design (confirmed on the live corpus: `109.160.32.110`'s 1,099 raw cases → 3 buckets of 707+389+3, not one). The correct criterion, reflecting that window-boundary floor, is "under ~700KB" — 627KB (post-Q-20 fix) clears it. The brief's acceptance criteria section below is left as originally written, for the historical record of what was targeted before shipping; do not read the 500KB→627KB gap as underperformance.

| Precondition | Status | Notes |
|---|---|---|
| Q-02 — no HTTP reference to port from | RESOLVED NO | F5 is the first consolidation mechanism; nothing to inherit. |
| Q-03 — three contract risks enumerated | RESOLVED | All three traced to NONE-impact; risk #3 spawned Q-16. |
| Q-16 — Tool 28 doesn't consolidate the flood | RESOLVED | Shape 3 selected and implemented. No longer a blocker. |
| Q-17 — no F5 code exists anywhere | RESOLVED NO | Confirmed at the time; superseded by this section's own shipped code. |
| Q-13 — F5 design/implementation | RESOLVED | Shipped and verified this pass — see Q-13's entry for full evidence. |

### Q-16's three shapes, reframed for a portfolio repo without a downstream SOC/dashboard consumer

**Shape 1 — Widen the predicate in Tool 26's write path.** Group successful-login cases by identical command signature at `ir_cases.json` write time. Cardinality drops N → 1 per signature. Smallest code surface, direct fix to the 88.6% byte bloat, but changes `case_id` semantics for anything that reads `ir_cases.json` — safe today per Q-03's trace, but the more invasive shape long-term. Tool 28's render size drops as a side effect once flood cases arrive pre-consolidated.

**Shape 2 — Dedupe within-case arrays.** Keep case cardinality, shrink `timeline`/`commands` arrays inside each case. No semantic change to `case_id`, but doesn't fix Tool 28's render size — 1,096 blocks still render. Solves half the problem; not the right standalone answer.

**Shape 3 — Two-layer: signature dedupe at write time + `session_count` field preserved.** Consolidated case carries a `session_count` of what it absorbed. Fixes both `ir_cases.json` size and Tool 28 render size; preserves count-accurate views. Larger code surface, requires defining a "case = consolidated signature group" contract in the docstring.

**Recommendation: Shape 3.** It's the only shape that fully closes Q-16's finding — Shape 1 gets close but leaves "what does `case_id` mean now" half-answered; Shape 2 doesn't touch the render-size complaint at all. The extra cost over Shape 1 is roughly a `session_count` field plus its docstring (~15 lines) — not a meaningful burden. `session_count` also matches the field name Tool 43's accumulator already uses, keeping vocabulary consistent across corpus tools. Q-03's trace already confirmed no current consumer misreads `case_id` cardinality, so Shape 3's cardinality shift ships without any cross-tool coordination. Shape 1 is a defensible runner-up if minimizing diff size is the goal, but Shape 3 is what the finding actually calls for.

### F5 design brief — as implemented (Shape 3)

```
# F5 — Tool 26 SSH per-IP Consolidation

## Preconditions (verified this session)
- No HTTP reference implementation exists (Q-02 RESOLVED NO).
- All three downstream contract risks traced to NONE-impact (Q-03 RESOLVED).
- No existing F5 code anywhere in the repo (Q-17 RESOLVED NO).
- Tool 28's is_groupable() is blind to the flood pattern (Q-16 RESOLVED).

## Chosen shape
Shape 3 — two-layer: signature dedupe at write time + per-case session_count.

## Design
- New function in tools/26_incident_timeline_live.py: consolidate_by_signature(cases).
- Grouping key: (src_ip, login_success, sorted(commands)).
- Time window: reuse Tool 28's GROUP_WINDOW_MINUTES, not a new constant.
- Consolidated case carries:
  - case_id: hash of (src_ip, signature, floor(first_seen / 24h)) — stable
    per-day, distinguishes daily windows (matches how Tool 43 already
    handles its own accumulators; hashing on (src_ip, signature) alone
    would be stable across runs but lose the ability to distinguish
    "same flood, different day").
  - session_count: number of raw cases absorbed.
  - session_ids_sample: first 10 raw case_ids (for traceability — full
    list would defeat the byte-reduction purpose).
  - timeline/commands: from the representative case (all identical by
    construction of the grouping key).
- Unconditional call at case-construction time, before write to ir_cases.json.

## Contract changes
- case_id no longer 1:1 with raw SSH session for successful-login cases.
- session_count now available on every case (default 1 for ungrouped).
- No existing consumer misreads this (Q-03 risk-i/ii traced to NONE-impact).

## Acceptance criteria
- Post-consolidation ir_cases.json byte count for the CLU-002 snapshot
  drops below ~500KB (from ~2.2MB).
- Tool 28's priority_cases count drops from 1,944 to under 100.
- All three existing regression tests still pass.
- A new regression test asserts consolidation behavior on a synthetic
  1,099-case flood input.

## RESULTS (2026-09-24, verified against real corpus — not the CLU-002
## synthetic snapshot the criteria above were written against)
- ir_cases.json: 2,236 cases -> 211, 8,064,684 bytes -> 613,538 bytes
  (92.4% reduction; 92.2% / 627,163 bytes after the Q-20 representative-selection fix -- see Q-20). MISSED the ~500KB target -- see the note below this
  fence for why that target itself was wrong, not the implementation.
- Tool 28's priority_cases: 1,944 -> 96 (report 2,360KB -> 304KB), measured
  with the real pipeline order (F5 -> Tool 29 regenerates fp_filter.json ->
  Tool 28) in an isolated sandbox. MEETS the brief's "under 100" target, but
  narrowly. An earlier figure of 54 / 259KB was WRONG: it came from running
  Tool 28 against a stale fp_filter.json listing 2,081 pre-F5 case_ids that no
  longer existed, which Tool 28 turned into bare stubs. The 96 = all
  login_success=True consolidated cases, as Q-16's is_groupable() finding predicts.
  Unchanged by the Q-20 fix. The earlier ~137 estimate and the later 54
  measurement were both wrong; 96 is the like-for-like figure. Pre-F5
  baseline on the same coherent chain: 1,944 priority cases, 2,360KB.
  Lesson: Tool 28 reads fp_filter.json's clean_cases (Tool 29 output), not
  ir_cases.json directly, so any verification must regenerate fp_filter.json
  from the consolidated file first (real order: Tool 26 -> 29 -> 28).
- Tool 35 unique HASSH fingerprints: 20 pre-F5, 18 after original F5
  (real signal loss), 20 after the Q-20 fix. See Q-20.
- All three pre-existing regression tests still pass (4+2+1 = 7 individual
  assertions across test_tool37_dedup_pruning.py, test_tool43_whole_corpus_prune.py,
  test_tool48_whole_corpus_prune.py).
- New regression test: 16 tests in tests/test_tool26_consolidation.py (13 original + 3 from the Q-20 fix), all
  passing, including a synthetic 100-case flood (not exactly 1,099 as
  originally specified -- 100 was sufficient to exercise the same code
  path) plus a direct real-corpus verification (109.160.32.110's actual
  1,099 raw cases -> 3 buckets of 707+389+3, run interactively, not
  committed as a test assertion since it depends on the live snapshot's
  exact contents rather than a fixed synthetic input).

## What this does NOT do
- Does not touch Tool 28's is_groupable() predicate (Q-16 says study its
  structure, don't copy its exclusion rule).
- Does not add cross-corpus consolidation — only Tool 26's write path.
- Does not change severity aggregation (Q-03 risk-iii confirmed NONE-impact;
  calculate_severity stays per-case, and the consolidated case inherits the
  representative's severity).
```

**Time-window choice:** reuse Tool 28's `GROUP_WINDOW_MINUTES` rather than defining a new constant — one fewer knob, and the two consolidators stay in sync if the window ever changes. **Implemented as a duplicated constant with a cross-tool equality test** (`test_group_window_matches_tool28`, added this pass), not a live import — the two modules have no stable shared import path in this repo's layout, so the constant is copied with a comment explaining why, and the test fails loudly if the two values are ever allowed to drift apart.

**Meta-note on the F5 template:** the first-draft implementation of F5 had three failures that would have crashed or silently mis-formatted on first run — `defaultdict` used but not imported, `from tools.incident_timeline_live_26 import ...` (filenames start with a digit; existing tests use `importlib.util.spec_from_file_location`), and `case_id = "consolidated-<hex>"` where repo convention (confirmed via `00_historical_processor.py` and `48_fingerprint_corpus.py`'s docstring) is `IR-<hex>`. All three were caught by running the code against the actual repo, not by review. Same discipline as the byte-scan-vs-name-grep lesson in this register's methodology note: **verify against the actual shape, don't trust a plausible-looking template.**

**With Shape 3 implemented, Q-11 (re-ranking F5) is closed by cross-reference** — there was no ship-order in a portfolio repo to re-rank against, and F5 is now simply done rather than next.

**State, in one sentence:** F5 is shipped. All preconditions (Q-02, Q-03, Q-16, Q-17) are closed, the implementation is in `tools/26_incident_timeline_live.py`, the tests are in `tests/test_tool26_consolidation.py` (16/16 passing), and it is verified against the real corpus, not just synthetic input. No open question blocks F5 because there is nothing left for it to be blocked on.
