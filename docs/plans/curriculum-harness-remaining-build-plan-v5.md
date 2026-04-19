# Curriculum Harness — Remaining Build Plan v5

**Status:** Active plan. Supersedes v3 (archived).
**Date:** 19 April 2026.
**Scope:** Harness cleanup only. After v5 closes, next project phase is the curriculum assistant (separate product, separate plan).

## 1. Purpose

Finish the reference-authoring pipeline ("the harness") so it produces teacher-usable output on any reasonable curriculum document with no silent halts. When v5 closes, the harness becomes the engine behind the curriculum assistant.

## 2. What this plan is not

Not a forward-looking product roadmap. Not a specification for the curriculum assistant, the teaching assistant, or Kaku. Those are captured in Second Brain and will have their own plans.

Not a rebuild of Phases 1-5 of the original harness. Those phases are deprecated. The reference-authoring pipeline built during the 4b arc is what "the harness" now means in practice.

## 3. Excellence criteria

The harness passes v5 when all four hold on an unseen curriculum document of any reasonable type:

1. Four artefacts produced — architecture diagnosis, KUD, learning targets, criterion bank with prerequisite structure.
2. No silent halts. Every uncertainty surfaces as flagged output with a confidence tier and plain-language explanation.
3. Broad multi-strand sources processed via auto-scoping rather than gate-halt.
4. Output readable by a teacher without pipeline-engineer mediation.

## 4. Architectural decisions carried forward

Source-native progression bands preserved in output. Translation to school-specific bands is downstream.

Three-artefact-serves-three-audiences consensus (17 April 2026 panel): architecture diagnosis drives behaviour, KUD and LTs serve teachers, criterion bank serves tutoring systems.

Contested domains use curated libraries, not knowledge graphs (15 April 2026 decision).

Type 3 content uses observation indicators and single-point rubrics, never five-level.

Criterion bank is the shared substrate; rubric rendering (five-level / four-level / single-point / mastery-binary / alternative vocabulary) is configurable downstream, not hardcoded in the harness.

## 5. Sessions

### Session 4c-1 — Halts become flags

Every pipeline halt becomes a flagged output with a confidence tier and a plain-language explanation.

**Pre-work.** Before the halts-to-flags refactor, sketch the criterion bank schema in `docs/schemas/criterion-bank-v1.md`. Fields: criterion ID, associated LT, competency-level descriptors (using default No Evidence / Emerging / Developing / Competent / Extending), prerequisite edges (criterion IDs), source provenance. This schema informs what flags need to carry so downstream sessions can consume them.

**Confidence tier taxonomy.** High: single gate failure, output stable across re-runs. Medium: multiple gate failures OR output unstable across re-runs. Low: multiple gate failures AND output unstable. Surfaced per artefact in the quality report.

**Flag explanations.** Two mandatory layers, one conditional. First layer: what the gate was checking (technical). Second layer: why a teacher might care (pedagogical). Third layer (horizontal domains only): whether the gate failure might reflect legitimate conceptual deepening rather than drift, with a prompt for the teacher to review.

**Definition of done.** AP US Gov re-run produces output for all 26 LTs (previously 11 halted) and all 15 rubrics plus the 4 previously gate-failed rubrics now present with flags. Quality report lists every flag with confidence tier and two-to-three-layer explanation. No silent halts anywhere in the run.

**Model.** Sonnet. No architectural judgement, well-specified refactor.

**Depends on.** Nothing.

### Session 4c-2a — Sonnet default, token logging, KS3 RSHE 2025 ingestion and run

**2026-04-19. Replaces original 4c-2 scope for this session. Original 4c-2 scope deferred to 4c-2b.**

Three tasks in this session:

1. **Sonnet default across per-item stages.** Change DEFAULT_MODEL from Haiku to Sonnet in all seven per-item reference-authoring pipeline stages (kud/classify_kud, lt/generate_lts, lt/generate_band_statements, lt/generate_observation_indicators, lt/cluster_competencies, criterion/generate_criteria, criterion/generate_supporting_components). Haiku remains selectable via --model flag. Opus escalation via --cluster-model unchanged.

2. **Token logging.** Update _anthropic.py to capture usage fields from API responses; accumulate per-stage and total input/output token counts in run-level state; write to quality_report.json under token_usage key; print summary line at run end with estimated cost. Cost constants for Haiku/Sonnet/Opus in _anthropic.py.

3. **KS3 RSHE 2025 ingestion and run.** Ingest 2025 statutory RSHE guidance (KS3 section only). Run full reference-authoring pipeline. Expect dispositional domain classification; moderate Type 3 proportion; ~30–55 KUD items.

**Model.** Sonnet.

**Depends on.** 4c-1.

### Session 4c-2b — Horizontal-domain gate recalibration

*(Originally Session 4c-2. Deferred from 4c-2a.)*

The `single_construct` and `observable_verb` gates halt on legitimate horizontal-domain output. Recalibrate both for horizontal domains without weakening them for hierarchical.

**Held-out test set.** Before tuning, designate one hierarchical source (Common Core 7.RP) and one horizontal source (Ontario G7 History) as held-out. Tune gate parameters against AP US Gov and Welsh CfW. Test on the held-out pair. If the held-out results regress, tune is rejected.

**Definition of done.** AP US Gov re-run shows zero false-positive halts on previously-halted rubrics that a teacher would accept (teacher-review step required). Held-out hierarchical source shows no regression (same or better gate-pass rate). Held-out horizontal source shows improvement or no change.

**Model.** Sonnet.

**Depends on.** 4c-2a.

### Session 4c-3a — Strand detection

Multi-strand sources (DfE KS3 Maths, NZ Curriculum Social Sciences) currently halt at the `artefact_count_ratio` gate. Build strand detection: identify top-level divisions in a source (strands, units, domains) so the pipeline can sub-run each strand separately.

**Definition of done.** Strand detection runs on DfE KS3 Maths and correctly identifies the six strands (Number, Algebra, Geometry, Statistics, Ratio and Proportion, Probability). Runs on NZ Curriculum Social Sciences and correctly identifies its top-level divisions. False-detection rate documented; a flag is raised if the detector is uncertain rather than silently splitting.

**Model.** Opus if >100 items across strands; Sonnet otherwise.

**Depends on.** 4c-1.

### Session 4c-3b — Sub-run orchestration and stitching

With strands detected, run the full pipeline on each strand as a sub-run. Stitch sub-run outputs into a unified reference corpus with strand-level provenance preserved.

**Definition of done.** DfE KS3 Maths produces a complete reference corpus across all strands. Output shape matches single-strand corpora (Welsh CfW, AP US Gov) with an added `strand` field on each artefact. A second multi-strand source runs end-to-end without human intervention. No artefact-count-ratio halts on either source.

**Model.** Sonnet.

**Depends on.** 4c-3a.

### Session 4c-4 — Criterion bank with prerequisite structure

Generate the fourth artefact: individual criteria with competency-level descriptors and prerequisite edges between criteria.

**Using the schema from 4c-1.** Criterion bank is produced per source following the `docs/schemas/criterion-bank-v1.md` schema sketched in 4c-1. Each criterion has a unique ID, the associated LT(s), five competency-level descriptors (default schema), and prerequisite edges pointing to other criterion IDs in the bank.

**DAG validity.** Prerequisite edges form a directed acyclic graph (no cycles). A hand-curated validation set of 10-15 prerequisite relationships per anchor source (Welsh CfW, Common Core 7.RP, Ontario G7 History) is used to check the generated DAG. Agreement rate reported; disagreement means the DAG is flagged for review, not that the session fails.

**Definition of done.** Criterion bank produced on all five reference sources (Welsh CfW, Common Core 7.RP, Ontario G7 History, AP US Gov, DfE KS3 Maths). DAG validity check run on the three anchors; agreement rate reported per source. No cycles in any DAG.

**Model.** Opus. Architectural work, prerequisite reasoning load-bearing.

**Depends on.** 4c-1, 4c-2b, 4c-3b.

## 6. Close criterion for v5

All five sessions complete. The harness runs end-to-end on any of the five reference sources and a previously-unseen sixth source, producing all four artefacts with flagged output and no silent halts. STATE.md updated to reflect harness completion.

## 7. Next after v5

Curriculum assistant. Separate product, separate plan. General tool for any curriculum in the world, Claude Design UI, library with project-style organisational system, MCP for Claude integration, default rubric schema and band mapping with user-overrides, calendar ingestion, full-year planning with constraint solver. See Second Brain entry dated 19 April 2026 for scope detail.

## 8. Operating discipline

Standard project rules apply — no overwriting planning docs, STATE.md updated at session end, Claude Code invocation named with model, no aspirational reporting, honest halts and flagged instability are features.

## 9. Panel review

Five-persona review run on v4 draft produced panel average 83 (below 88 threshold). v5 revisions folded in: confidence tier taxonomy specified, flag explanations layered, criterion bank schema sketched pre-4c-1, held-out test set for gate recalibration, strand detection split from sub-run orchestration, DAG validity check added. Panel re-score on v5: Wiliam 89, Claxton 88, Christodoulou 89, Koedinger 87, Wineburg 88. Average 88.2 — clears threshold.

---

*Build plan v5 generated 2026-04-19 after Session 4b-5b close. Supersedes v3. Next update expected after Session 4c-1 close or earlier if close criteria change.*
