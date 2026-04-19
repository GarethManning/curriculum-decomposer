# STATE.md — Curriculum Harness

Live state register. Updated at the end of every Claude Code session. Distinct from `docs/plans/curriculum-harness-remaining-build-plan-v5.md` (forward-looking) and `docs/project-log/harness-log.md` (historical). See `docs/process/state-md-discipline.md` for update protocol.

## 1. Last session

**Session 4c-2b** — 2026-04-19 — head `6d44042 [gen] Secondary RSHE 2025 — 4c-2b fresh run (gate-calibrated)`.

Gate recalibration session. Three gate fixes delivered: Commit A (19 transfer/integration verbs added to OBSERVABLE_VERBS and _VERB_BUCKETS), Commit B (_topic_lemmas() lemmatisation fix — single_construct morphology-aware), Fix 1 (six additional verbs: attempt, acknowledge, validate, discuss, locate, determine). All three are pure additive changes; no gate ceiling loosened.

4c-2b gate counts before/after on Secondary RSHE 2025 fresh run:
- `observable_verb`: 17 → 0 (fixed by Commit A + Fix 1)
- `single_construct`: 6 → 2 (fixed by Commit B; 2 residual are genuine lemmatiser-gap artefacts)
- `competent_framing_regex`: 1 → 1 (unchanged)

3 persistent single_construct false positives identified as lemmatiser-gap artefacts (vocabulary depth-shift pattern; `-ful`/`-fully` morphology, hyphen splitting, name/identify coupling not covered by current `_lemmatise()`). cluster_06_lt_02 and cluster_14_lt_01 persist in fresh run. Flagged for teacher review. Scoped to 4c-2c.

RSHE 2025 fresh run (4c-2b): 66 LTs / 26 clusters / 62 rubrics (10 gate-fail, 7 gen-fail) / 44 supporting components / ~$7.64. Gate improvements significantly reduced gate-fail count (4c-2a: 26 gate-fail → 4c-2b: 10 gate-fail). Supporting components increased from 28 to 44 as a result.

Methodological lesson captured in VALIDITY.md: in-memory gate re-validation against fixed rubrics predicts gate logic correctness but not gate coverage on fresh generations.

## 2. Verified working

- **Phase 0 acquisition layer — complete.** Five source-type primitives at `curriculum_harness/phases/phase0_acquisition/sequences.py`; manifest schema 0.6.0 at `manifest.py:280`; ten ingestion artefacts under `docs/run-snapshots/` (nine prior + secondary-rshe-2025) covering all three domain types.
- **Welsh CfW Health & Wellbeing reference — complete.** `docs/reference-corpus/welsh-cfw-health-wellbeing/` — pre-4c-1 note applies (criteria.json predates halts-to-flags refactor).
- **Common Core 7.RP reference — complete.** `docs/reference-corpus/common-core-g7-rp/` — same pre-4c-1 note.
- **Ontario G7 History reference — complete (4b-5).** `docs/reference-corpus/ontario-g7-history/` — same pre-4c-1 note.
- **AP US Gov CED Unit 1 reference — complete (4c-1 re-run).** `docs/reference-corpus/ap-usgov-ced-unit1/` — 26 LTs / 26 rubrics (10 pass / 9 gate-fail / 7 gen-fail) / 50 flags / 5 CSVs.
- **Secondary RSHE 2025 reference — complete (4c-2b).** `docs/reference-corpus/secondary-rshe-2025/` — 149 KUD / 26 clusters / 66 LTs / band sets / 4 obs indicator sets / 62 rubrics (10 gate-fail, 7 gen-fail) / 44 supporting components / 5 CSVs. `england_rshe_secondary` progression type (single-band "End of Secondary", ages 11-16). Gate-calibrated: obs=0, sc=2, comp=1. 2 persistent single_construct false positives (lemmatiser-gap; flagged for teacher review).
- **Reference-authoring criterion gates — recalibrated (4c-2b).** `criterion_gates.py` OBSERVABLE_VERBS expanded to 44 verbs (19 transfer/integration verbs Commit A + 6 additional verbs Fix 1). `_topic_lemmas()` lemmatisation-aware (Commit B). `generate_criteria.py` _VERB_BUCKETS kept in sync. Adversarial suite: 16/16 pass.
- **Reference-authoring pipeline — Sonnet default (4c-2a).** `DEFAULT_MODEL = SONNET_MODEL` in all 7 per-item stages. `--model` flag propagates through to all stages. `--cluster-model` Opus escalation unchanged.
- **Token logging — complete (4c-2a).** `curriculum_harness/_anthropic.py`: `TokenLedger`, `LEDGER`, cost constants (Haiku/Sonnet/Opus).
- **`detect_progression.py` — `england_rshe_secondary` added (4c-2a).** Curated entry for DfE RSHE statutory guidance.
- **Reference-authoring pipeline v0.6 — halts-to-flags shipped (4c-1).** Unchanged from 4c-1.
- **Criterion bank schema v1.** `docs/schemas/criterion-bank-v1.md` — target schema for 4c-4.
- **VALIDITY.md populated.** Seven validator scripts plus `run_all.py` driver in `scripts/validity-gate/`. Methodological lesson added: in-memory gate validation is not a substitute for fresh-run validation.

## 3. Verified broken

- **English-only Phase 1 cue list.** `curriculum_harness/phases/phase1_ingestion.py:202-245`.
- **Hardcoded GCSE_AQA_EXAM_BLOCK in Phase 4.** `curriculum_harness/phases/phase4_lt_generation.py:132-138`.
- **Phase 5 strand routing.** `curriculum_harness/phases/phase5_formatting.py:70-86`.
- **Phase 3 flag-and-continue for `classification_unreliable`.** Phase 3 still emits items without a regeneration loop.
- **Welsh/Common Core/Ontario criteria.json predate 4c-1.** Rubric gen halts remain in `halted_lts`. Re-run not required but would update format.
- **`_lemmatise()` derivational morphology.** `-ful`/`-fully` morphology, hyphen splitting, name/identify coupling not resolved. Causes 2 persistent single_construct false positives on RSHE 2025. Scoped to 4c-2c.

## 4. Unverified

- **RSHE 2025 Type 3 rate (3.4%).** RSHE uses propositional framing ("pupils should know that...") for outcomes that are pedagogically dispositional. Whether 3.4% is a classification limitation or genuinely reflects the source's framing is unresolved. Teacher review needed to assess.
- **Phase 3 consolidation collapse on felvételi.** Observable only in a Phase 3 run output.
- **Reference-authoring gate pass rates for Welsh CfW / Common Core under a fresh re-run.** Not re-verified since 4c-1.
- **AP US Gov rubric flag rate after gate recalibration.** 4c-2b gate improvements not yet applied to an AP US Gov re-run. Expected improvement; not verified.

## 5. Next session

**Recommendation: 4c-3a (strand detection)** — higher value to harness completion than 4c-2c (lemmatiser improvements). The 2 residual single_construct false positives are lemmatiser-gap artefacts flagged for teacher review; they are not blocking production use. Strand detection unlocks DfE KS3 Maths and multi-strand sources, which are the key gap in corpus breadth.

**4c-3a — Strand detection.** Multi-strand sources (DfE KS3 Maths, NZ Curriculum Social Sciences) halt at the `artefact_count_ratio` gate. Build strand detection: identify top-level divisions in a source so the pipeline can sub-run each strand separately. See `docs/plans/curriculum-harness-remaining-build-plan-v5.md` for full spec.

**4c-2c (deferred) — Lemmatiser improvements.** `-ful`/`-fully` morphology, hyphen splitting, name/identify coupling. Covered by existing adversarial tests; estimated under 30 lines. Defer unless teacher review flags the 2 persistent single_construct false positives as blocking.

Invocation:
```
cd ~/Github/curriculum-harness && claude --dangerously-skip-permissions --model sonnet
```

## 6. Open questions

- **RSHE KUD count (149 vs expected 30-55).** The briefed expectation was 30-55 items post-filtering. Actual: 149. The higher count is defensible — RSHE numbered bullets contain multiple distinct "should know" sub-items; the classifier correctly splits them. Not a gate failure but worth noting for future sources with similarly verbose numbered lists.
- **LOW confidence tier not seen in any run.** Defined in 4c-1; hasn't fired yet. Requires multiple gate failures AND unstable rubric simultaneously.
- **Welsh/Common Core/Ontario not re-run.** Pre-4c-1 criteria.json format. Re-run needed if 4c-4 requires their output in new format.
- **Ontario LT halts on large Opus clusters.** Carry-forward from 4b-5. Pick up in 4c-7.
- **Second hierarchical source gap.** DfE KS3 Maths (full programme) failed ratio gate. Scoped re-ingestion (one strand only) needed in 4c-3a.
- **AP US Gov rubric flag rate after 4c-2b gate recalibration.** Not yet re-run. Pick up in 4c-3a or dedicated session.

---

*Last updated 2026-04-19 at end of Session 4c-2b. Update at end of every session per `docs/process/state-md-discipline.md`.*
