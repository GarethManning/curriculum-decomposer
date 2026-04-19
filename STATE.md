# STATE.md — Curriculum Harness

Live state register. Updated at the end of every Claude Code session. Distinct from `docs/plans/curriculum-harness-remaining-build-plan-v3.md` (forward-looking) and `docs/project-log/harness-log.md` (historical). See `docs/process/state-md-discipline.md` for update protocol.

## 1. Last session

**Session 4b-5** — 2026-04-19 — head `2f18bf3 [gen] Ontario G7 History — re-cluster on Opus 4.6 + criteria + supporting (4b-5)`.

Closed out Session 4b-5 by completing the Ontario Grade 7 History reference corpus as the third anchor. Re-clustered Ontario's 188-item KUD on Opus 4.6 (prior run was Haiku; STATE.md prior claim of "Sonnet" was wrong) — membership drift dropped from 43.09% (Haiku 4b-3) to 0% (run2) / 9.57% (run3), both cleanly below the 20% DoD threshold. Added `--cluster-model` flag to the reference-authoring pipeline plus a standalone `run_cluster_only.py` probe runner. Regenerated downstream artefacts on Haiku (LTs / bands / indicators / criteria / supporting components). Exported 5 CSVs; regenerated `reference-review.md` and updated `_cross-source-summary.md`. Ontario directory now shape-parity with Welsh CfW and Common Core.

## 2. Verified working

- **Phase 0 acquisition layer — complete.** Five source-type primitives at `curriculum_harness/phases/phase0_acquisition/sequences.py`; manifest schema 0.6.0 at `manifest.py:280`; nine ingestion artefacts under `docs/run-snapshots/` covering all three domain types. Verified in audit section 1.
- **Welsh CfW Health & Wellbeing reference — complete.** `docs/reference-corpus/welsh-cfw-health-wellbeing/` carries KUD (33), clusters (9), LTs (20), band statements (11 sets), observation indicators (5 sets), criteria (12 rubrics, 11 gate pass), supporting components (9), progression structure, quality reports, reference review, **five CSVs** (criteria, kud, learning-targets, observation-indicators, supporting-components), and the preserved `_generated-in-error-a-d-version/` subdirectory.
- **Common Core 7.RP reference — complete.** `docs/reference-corpus/common-core-g7-rp/` carries KUD (22), clusters (4), LTs (8), band statements (6 sets), observation indicators (0 — no Type 3 content), criteria (7 rubrics, 6 gate pass), supporting components (4), progression structure, quality reports, reference review, **five CSVs** (the observation-indicators CSV is metadata-only, 8 lines, zero rows).
- **Ontario G7 History reference — complete (4b-5).** `docs/reference-corpus/ontario-g7-history/` carries KUD (188), clusters (8 canonical, Opus 4.6), LTs (13; 3 halted clusters), band statements (11 sets), observation indicators (2 sets), criteria (7 rubrics, 6 gate pass, 4 halted), supporting components (6, 0 halts), progression structure, quality reports, reference review, **five CSVs**. Cluster membership drift: 0% (run2) / 9.57% (run3), below the 20% DoD threshold. `overall_stability_flag = cluster_unstable` driven by `cluster_count_differs [8, 8, 7]` and one unmatched canonical cluster in run3 — not membership drift.
- **Reference-authoring pipeline v0.5 — shipped.** `curriculum_harness/reference_authoring/` carries inventory, KUD classifier/gates, competency clustering, LT generator, band statements, observation indicators, Type 1/2 criterion generator, criterion gates, supporting-components generator, progression detection with jurisdiction lookup, and a `pipeline/run_pipeline.py` orchestration entry point (4b-5: `--cluster-model` flag lets callers escalate clustering to Opus without touching downstream stages). Scripts at `scripts/reference_authoring/`, including `run_cluster_only.py` probe runner (4b-5).
- **Phase 4 hard-fail regeneration loop — in place since Session 3c.** `curriculum_harness/phases/phase4_lt_generation.py:1-58` defines `FAIL_SET` and `MAX_REGENERATION_RETRIES = 3`; budget-exhausted LTs route to `state["human_review_required"]`, not shipped silently.
- **VALIDITY.md populated.** Seven validator scripts plus `run_all.py` driver in `scripts/validity-gate/`: `validate_source_coverage.py`, `validate_source_faithfulness.py`, `validate_architecture_diagnosis.py`, `validate_exam_block_scope.py`, `validate_lt_surface_form.py`, `validate_regenerate_loop.py`, `validate_lt_criterion_coverage.py`, `validate_prerequisite_dag.py`.
- **Sessions 3a-3d Phase 1/3/4 work landed.** Phase 3 profile-conditional branch (`2e7c5da`), Phase 1 scope stabilisation (`43f4f4a`), Phase 4 regeneration loop (`cfc13f5`), bullet-type tagging (`80bab1b`).

## 3. Verified broken

- **English-only Phase 1 cue list.** `curriculum_harness/phases/phase1_ingestion.py:202-245` — `cues: dict[str, tuple[str, ...]]` is English-only across all five `document_family` branches; `_window_history_grade7` at line 171-188 uses English-only anchors. Hungarian / Welsh-language sources miss every needle.
- **Hardcoded GCSE_AQA_EXAM_BLOCK in Phase 4.** Defined at `curriculum_harness/phases/phase4_lt_generation.py:132-138` and attached unconditionally on any `document_family == "exam_specification"` at line 871. Tracked by `scripts/validity-gate/validate_exam_block_scope.py`.
- **Phase 5 strand routing.** `curriculum_harness/phases/phase5_formatting.py:70-86` implements `_competency_relevance_score` as a pure token-set intersection; `map_lt_to_strand_label` at line 127-149 collapses to zero when LT vocabulary does not share tokens with source strand labels, and falls back on arbitrary ordering among zero-scored candidates.
- **Phase 3 flag-and-continue for `classification_unreliable`.** Unlike Phase 4, Phase 3 still emits items tagged `classification_unreliable` without a regeneration loop. Phase 3's hard-fail equivalent is not yet built.
- **Ontario LT generation halts on large clusters (4b-5).** `lts.json` shows 3 of 8 Opus clusters halted LT generation with `lt_set_unreliable` (0/3, 1/3, 0/3 parseable runs) — all three clusters are large (23, 31, 34 items). Haiku's parse-reliability ceiling for LT generation on large clusters may warrant a per-stage model override analogous to the 4b-5 `--cluster-model` flag; tracked as a rebuild candidate.

## 4. Unverified

These are claimed in prior planning / run outputs but not verifiable from code alone under a read-only audit.

- **Phase 3 consolidation collapse on felvételi (32 source bullets → 14 Do-Skills).** Observable only in a Phase 3 run output (`outputs/palya-...`), not in phase source. The per_bullet vs strand_aggregated branching introduced in Session 3b/c was designed to mitigate this pattern; whether the mitigation is fully load-bearing on a fresh felvételi run is unconfirmed.
- **Factorial-notation injection from model priors on felvételi.** Pattern is acknowledged indirectly by the `source_faithfulness.py` module and the `SOURCE_FAITHFULNESS_FAIL_FLAG` wired into Phase 4's `FAIL_SET`; the specific injection is visible only in produced output.
- **Reference-authoring gate pass rates under a fresh run.** On-disk `criteria_quality_report.json` shows 12/11 for Welsh CfW and 7/6 for Common Core; these match the last generation run but are not re-verified.
- **v3 projections may be systematically too high for Opus-clustered sources.** v3's Session 4b-5 DoD projected 15–20 rubrics for Ontario; Opus-clustered Ontario produced 13 LTs and 7 rubrics, below that projection. The projection was calibrated against the prior Haiku-clustered Ontario run (23 LTs). Verify in 4b-5b whether comparator sources show the same gap at the Sonnet default, and revise v3 projections if the pattern holds across both domain types.

## 5. Next session

**Session 4b-5b — Comparator source references** (see `docs/plans/curriculum-harness-remaining-build-plan-v3.md`). Produces reference corpora for the two second-instance sources (DfE KS3 Maths as second hierarchical; AP US Gov Unit 1 as second horizontal). Each directory should match the shape of `common-core-g7-rp/`: inventory / kud / clusters / lts / band_statements / observation_indicators / criteria / supporting_components / quality_report / reference-review / five CSVs. Cross-source summary extended to five sources. Sonnet by default; Opus if either source exceeds ~100 items at any classification stage (use the new `--cluster-model` flag for clustering escalation).

Invocation:

```
cd ~/Github/curriculum-harness && claude --dangerously-skip-permissions --model sonnet
```

## 6. Open questions

- **Ontario LT halts on large Opus clusters (4b-5).** Opus clustering consolidated Ontario into fewer, larger clusters (23/31/34 items on the halted three); Haiku LT generation failed parse-reliability on all three. Options: (a) add `--lt-model` to pipeline and escalate LT gen to Opus for large-cluster inputs; (b) raise LT generator `DEFAULT_MAX_TOKENS` (currently 3072); (c) split large clusters before LT gen. Triage in 4b-5b if a second horizontal/hierarchical source exposes the same pattern; otherwise pick up in the Phase 1 rebuild priorities session (4b-7).
- **`overall_stability_flag == cluster_unstable` is normal, not a DoD failure.** All three anchors ship `cluster_unstable` for reasons other than membership drift (Welsh CfW: cluster_count_differs on small corpus; Common Core: dominant_type_drift on one cluster; Ontario: cluster_count_differs + one unmatched cluster in run3). The v3 DoD targets *membership drift* specifically. Worth a future gate-revision pass to decide whether to also relax the `overall_stability_flag` threshold or keep the current diagnostic-per-category split.

---

*Last updated 2026-04-19 at end of Session 4b-5. Update at end of every session per `docs/process/state-md-discipline.md`.*
