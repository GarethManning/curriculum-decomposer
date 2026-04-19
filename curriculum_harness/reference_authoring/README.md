# Reference-authoring pipeline

Produces neutral reference KUDs, LTs, and criteria for anchor curriculum
sources. Compared against harness output in the separate comparison
pipeline (Session 4b-6).

## Distinct from the harness

This subsystem is **not** called by the harness (Phase 0–5 in
`curriculum_harness/phases/`). It runs separately, reads an extracted
source (a run-snapshot `content.txt`), and writes a reference corpus
to `docs/reference-corpus/<source-slug>/`.

## Discipline

The pipeline **must not** read, import, or reference any harness output
(no Palya run, no `outputs/...` JSONs, no prior KUDs). References are
neutral targets. Any cross-contamination invalidates their role as
comparators.

## Architecture

- `inventory/build_inventory.py` — verbatim source-content extraction into
  structured content blocks with source-position and heading hierarchy.
- `kud/classify_kud.py` — applies the LT authoring skill's Step 0
  knowledge-type decision tree mechanically. 3x self-consistency at
  temperature 0.3. Welsh CfW placement rule: sustained orientations
  route to Do-Disposition/Type 3; propositional content to Know/Understand/Type 1;
  occasion-triggered skills to Do-Skill/Type 2.
- `gates/kud_gates.py` — structural quality gates (source coverage,
  traceability, artefact-count ratio with **domain-aware thresholds**
  per vision v4.1 + the 4b-2 PROVISIONAL dispositional revision, Type 3
  distribution, no compound unsplit). Failures halt output with
  specific diagnostics.
- `lt/cluster_competencies.py` — clusters KUD items into competencies
  (2-3 LTs per competency, LT skill). 3x self-consistency with a
  deterministic stability check (cluster count, membership drift via
  Jaccard alignment, dominant-knowledge-type drift, unmatched-cluster
  existence).
- `lt/generate_lts.py` — LT generator. 2-3 LTs per competency;
  single-construct rule; knowledge-type split when a competency mixes
  Type 3 with Type 1/2; "I can" / "The student" definition-format
  check.
- `lt/generate_band_statements.py` — Type 1/2 band-statement
  generator. Bands A-D, progression levers (not topic escalation).
  Quality gate: "I can" prefix, 10-25 word count, observable-verb
  presence, banned substrings. Gate failures halt.
- `lt/generate_observation_indicators.py` — Type 3 observation-
  indicator generator. LT-specific observable behaviours per band,
  LT-specific parent prompts, prerequisite pointers, developmental
  conversation protocol reference. Generic developmental
  self-reflection prompts inserted from
  `types.MODE3_SELF_REFLECTION_PROMPTS` (calibrated by band, not LT-
  specific — correct Mode 3 behaviour per the skill). Mode 3 gate
  rejects rubric descriptors. Gate failures halt.
- `pipeline/run_pipeline.py` — orchestration. Full sequence: inventory
  → classify → KUD gates → cluster → LTs → bands + indicators →
  extended report. `--resume-from-kud` skips inventory + classify.
- `criterion/` (stub) — Type 1/2 criterion generator (five-level
  rubrics per the rubric logic skill) for session 4b-3.

## Implementation status

After session 4b-2:

- inventory: **implemented** (4b-1)
- KUD classifier: **implemented** (4b-1)
- KUD quality gates: **implemented** (4b-1); domain-aware
  `artefact_count_ratio` **revised** (4b-2, dispositional PROVISIONAL)
- pipeline orchestration: **implemented**, full sequence including
  LT + band + indicator stages, `--resume-from-kud` supported (4b-2)
- competency clustering: **implemented** with operationalised
  stability check (4b-2)
- LT generator: **implemented** (4b-2)
- Type 1/2 band-statement generator: **implemented** (4b-2)
- Type 3 observation-indicator generator: **implemented** (4b-2)
- Type 1/2 criterion generator (five-level rubrics): **stubbed** —
  session 4b-3 (Common Core / Ontario)
- comparison pipeline: **not here** — session 4b-6

## Running

Full pipeline from a Phase 0 snapshot:

```bash
python -m curriculum_harness.reference_authoring.pipeline.run_pipeline \
    --snapshot docs/run-snapshots/<session>-<source-slug>/ \
    --out docs/reference-corpus/<source-slug>/ \
    --domain dispositional   # or hierarchical / horizontal
```

Resume from an existing KUD (4b-2 Welsh CfW path):

```bash
python -m curriculum_harness.reference_authoring.pipeline.run_pipeline \
    --resume-from-kud \
    --out docs/reference-corpus/<source-slug>/ \
    --dispositional \
    --domain dispositional
```

Render the full reference for human review:

```bash
python -m scripts.reference_authoring.render_reference_for_review \
    --corpus docs/reference-corpus/<source-slug>/
```
