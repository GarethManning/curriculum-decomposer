# STATE.md — Curriculum Harness

Live state register. Updated at the end of every Claude Code session. Distinct from `docs/plans/curriculum-harness-remaining-build-plan-v5.md` (forward-looking) and `docs/project-log/harness-log.md` (historical). See `docs/process/state-md-discipline.md` for update protocol.

## 1. Last session

**Session 4c-2a** — 2026-04-19 — head `3f48683 [gen] Secondary RSHE 2025 — full reference-authoring pipeline run`.

Three tasks delivered: (1) Sonnet default across all 7 per-item reference-authoring stages; `--model` flag now wires through to all stages (LT gen, band statements, obs indicators, rubrics, supporting components), not just KUD. (2) Token logging: `TokenLedger` in `_anthropic.py` accumulates per-stage input/output token counts keyed by API call label prefix; both `haiku_stream_text` and `beta_messages_create` record to the ledger; quality_report.json gains a `token_usage` key; run prints summary line "Run complete. Total tokens: X input, Y output. Estimated cost: $Z." (3) Secondary RSHE 2025 ingested (47-page PDF, two-pass extraction pages 14-20 + 28-32) and full pipeline run; progression detector extended with `england_rshe_secondary` curated entry.

RSHE 2025 run: source renamed from "KS3 RSHE" to "Secondary RSHE" (document sets terminal outcomes for end of secondary, no KS3/KS4 split). 149 KUD items (higher than expected 30-55 — RSHE numbered bullets each contain multiple distinct knowledge items; classifier splits correctly but count is high). Type 3 only 3.4% (flagged, informational) — RSHE uses propositional framing for dispositional outcomes. Opus clustering used (149 items > 100 threshold). 66 LTs / 62 rubrics (36 pass / 26 gate-fail, 6 gen-fail) / 97 flags / 28 supporting components. Token cost: ~$7.19 (Sonnet + Opus).

## 2. Verified working

- **Phase 0 acquisition layer — complete.** Five source-type primitives at `curriculum_harness/phases/phase0_acquisition/sequences.py`; manifest schema 0.6.0 at `manifest.py:280`; ten ingestion artefacts under `docs/run-snapshots/` (nine prior + secondary-rshe-2025) covering all three domain types.
- **Welsh CfW Health & Wellbeing reference — complete.** `docs/reference-corpus/welsh-cfw-health-wellbeing/` — pre-4c-1 note applies (criteria.json predates halts-to-flags refactor).
- **Common Core 7.RP reference — complete.** `docs/reference-corpus/common-core-g7-rp/` — same pre-4c-1 note.
- **Ontario G7 History reference — complete (4b-5).** `docs/reference-corpus/ontario-g7-history/` — same pre-4c-1 note.
- **AP US Gov CED Unit 1 reference — complete (4c-1 re-run).** `docs/reference-corpus/ap-usgov-ced-unit1/` — 26 LTs / 26 rubrics (10 pass / 9 gate-fail / 7 gen-fail) / 50 flags / 5 CSVs.
- **Secondary RSHE 2025 reference — complete (4c-2a).** `docs/reference-corpus/secondary-rshe-2025/` — 149 KUD / 27 clusters / 66 LTs / 61 band sets / 4 obs indicator sets / 62 rubrics / 28 supporting components / 97 flags / 5 CSVs. `england_rshe_secondary` progression type (single-band "End of Secondary", ages 11-16). Known: high absolute KUD count (149) due to multi-item RSHE bullets; low Type 3% (3.4%, flagged) due to propositional framing of dispositional outcomes.
- **Reference-authoring pipeline — Sonnet default (4c-2a).** `DEFAULT_MODEL = SONNET_MODEL` in all 7 per-item stages. `--model` flag propagates through to all stages (LT gen, band statements, obs indicators, rubrics, supporting). `--cluster-model` Opus escalation unchanged.
- **Token logging — complete (4c-2a).** `curriculum_harness/_anthropic.py`: `TokenLedger`, `LEDGER`, cost constants (Haiku/Sonnet/Opus). `haiku_stream_text` captures usage from `stream.get_final_message()`. `beta_messages_create` captures `response.usage`. `run_pipeline.py` resets LEDGER at run start, appends `token_usage` to `quality_report.json` at completion, prints summary line.
- **`detect_progression.py` — `england_rshe_secondary` added (4c-2a).** Curated entry for DfE RSHE statutory guidance; URL match on `assets.publishing.service.gov.uk` + `relationships` path; slug match on `rshe`. Single-band "End of Secondary", ages 11-16, high confidence.
- **Reference-authoring pipeline v0.6 — halts-to-flags shipped (4c-1).** Unchanged from 4c-1.
- **Criterion bank schema v1.** `docs/schemas/criterion-bank-v1.md` — target schema for 4c-4.
- **VALIDITY.md populated.** Seven validator scripts plus `run_all.py` driver in `scripts/validity-gate/`.

## 3. Verified broken

- **English-only Phase 1 cue list.** `curriculum_harness/phases/phase1_ingestion.py:202-245`.
- **Hardcoded GCSE_AQA_EXAM_BLOCK in Phase 4.** `curriculum_harness/phases/phase4_lt_generation.py:132-138`.
- **Phase 5 strand routing.** `curriculum_harness/phases/phase5_formatting.py:70-86`.
- **Phase 3 flag-and-continue for `classification_unreliable`.** Phase 3 still emits items without a regeneration loop.
- **Welsh/Common Core/Ontario criteria.json predate 4c-1.** Rubric gen halts remain in `halted_lts`. Re-run not required but would update format.

## 4. Unverified

- **RSHE 2025 Type 3 rate (3.4%).** RSHE uses propositional framing ("pupils should know that...") for outcomes that are pedagogically dispositional. Whether 3.4% is a classification limitation or genuinely reflects the source's framing is unresolved. Teacher review needed to assess.
- **RSHE 2025 rubric gate-fail rate (42%: 26/62).** High for a new source. Sonnet on first run of a dispositional domain with propositional framing — some gate failures may be source-type artifacts. Gate recalibration in 4c-2b may reduce false positives.
- **Phase 3 consolidation collapse on felvételi.** Observable only in a Phase 3 run output.
- **Reference-authoring gate pass rates for Welsh CfW / Common Core under a fresh re-run.** Not re-verified since 4c-1.

## 5. Next session

**Session 4c-2b — Horizontal-domain gate recalibration** (see `docs/plans/curriculum-harness-remaining-build-plan-v5.md`). The `single_construct` and `observable_verb` gates flag on legitimate horizontal-domain output. Recalibrate both for horizontal domains without weakening them for hierarchical. Held-out test set: Common Core 7.RP (hierarchical), Ontario G7 History (horizontal). Tune against AP US Gov and Welsh CfW.

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
- **AP US Gov rubric flag rate (62%).** Haiku clustering in prior run; may improve on Sonnet re-run. Pick up in 4c-2b.

---

*Last updated 2026-04-19 at end of Session 4c-2a. Update at end of every session per `docs/process/state-md-discipline.md`.*
