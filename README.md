# Curriculum Harness

Standalone **LangGraph** pipeline that ingests a curriculum document (URL — PDF or plain text), diagnoses its knowledge architecture, derives a **KUD** (Know / Understand / Do) map with assessment routes, and generates **learning targets** aligned to Claude Education Skills MCP tools.

Downstream half of a two-tool architecture; the upstream Constitution Tool (not in this repo) ingests narrative prose and produces the structured curriculum document or exam specification that this harness consumes.

> **Repository rename pending.** The project was renamed from `curriculum-decomposer` → `Curriculum Harness` (package: `curriculum_harness`). The GitHub repo URL still reads `curriculum-decomposer` — a manual rename via GitHub settings is outstanding.

## Setup

```bash
cd curriculum-decomposer
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
# set ANTHROPIC_API_KEY in .env
```

## Usage

```bash
python -m curriculum_harness.run --config configs/ontario_grade7_history_v1_0.json --dry-run
python -m curriculum_harness.run --config configs/ontario_grade7_history_v1_0.json
python -m curriculum_harness.run --config configs/ontario_grade7_history_v1_0.json --resume
```

Outputs are written under the configured `outputPath` (versioned `*_v1.*` files). Checkpoints use Sqlite (`checkpointDb`).

## Curriculum profile (v1.1)

Phase 1 classifies the document into a **`curriculum_profile`** (JSON + run report section). The model infers `document_family`, `level_model`, `scoping_strategy`, and `assessment_signals`; **`output_conventions`** includes `lt_statement_format` and **`recommended_adjacent_radius`** (product default **±1** when using adjacent bands).

### v1.3 — profile-driven learning-target wording

- **Resolved format:** `resolve_lt_statement_format(profile)` picks the active format after merge: if `output_conventions.lt_statement_format` is set to `i_can`, `outcome_statement`, or `competency_descriptor`, it wins; otherwise **`higher_ed_syllabus` → `outcome_statement`**, and **all other families (including `exam_specification`) default to `i_can`**.
- **Phase 4** branches MCP + Sonnet prompts and validation on that format. Each emitted **`LearningTarget`** carries **`lt_statement_format`** for downstream storage (e.g. Supabase).
- **Exam specifications (`exam_specification`):** an **AQA-style command-word / mark-tariff awareness** block is appended to Phase 4 instructions. Output format remains **`i_can`** unless you override `lt_statement_format` in config.
- **Higher education (`higher_ed_syllabus`):** after the KUD loop, a supplementary Sonnet pass adds up to **three** inferred Type 3 dispositions (`assessment_route: observation_protocol`, flag **`HE_DISPOSITION_INFERRED`**). Near-duplicates vs existing targets are skipped using **cosine similarity** on token-frequency vectors (threshold **0.92** in code).
- **Phase 5** uses the profile default and **per-LT** `lt_statement_format` when generating structured rows and anchor-level fallbacks.
- **Run report** lists the count (and truncated statements) of **`HE_DISPOSITION_INFERRED`** learning targets.

`ltConstraints.iCanFormat` in a run config does not override the profile resolver; use **`curriculumProfile.output_conventions.lt_statement_format`** to force a format.

**Overrides**

- `source.documentFamily` — if set, overrides the inferred family. Values: `exam_specification`, `national_framework`, `school_scoped_programme`, `higher_ed_syllabus`, `other`.
- `curriculumProfile` — optional object merged into the profile (e.g. `output_conventions`, `scoping_strategy`, `assessment_signals`).

**REAL School** — use `document_family: "school_scoped_programme"` (or leave inference) and set **`source.jurisdiction`** (e.g. REAL School / location).

**Adjacent levels** — prefer `outputStructure.adjacent_count: 1` for ±1 bands; you can still set `2` for wider spreads.

## Models

- **Haiku**: Phase 1 ingestion / parsing volume.
- **Sonnet** (`claude-sonnet-4-20250514`): Phases 2–4, including MCP tool calls against the configured remote MCP server.
