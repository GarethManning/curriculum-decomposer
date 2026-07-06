# Curriculum-Harness Audit — Minnesota SEL Fitness Review

**Date:** 2026-07-06 · **Version:** v1 · **Model:** Opus (plan-mode audit) · **Scope:** read-only; no pipeline files modified
**Question:** Is `~/Github/curriculum-harness` fit to transform Minnesota's SEL benchmarks into LearnOS learning-target structure, and what is the minimal change list to make it so?

> Verification note: every finding cites `file:line`. Each citation was re-read against the working tree during this session; none are reported from memory of an earlier read.

---

## 0. Repository & pipeline map (read before judging)

The repo contains **two distinct generation pipelines** that share the model helpers, schema, and token ledger. Distinguishing them is essential to the audit — they have different clean-room and rubric exposure.

### Pipeline A — Main graph (`python -m curriculum_harness.run --config …`)
LangGraph state machine wired in `curriculum_harness/graph.py:503-516`:

```
phase1_ingestion → phase2_architecture → phase3_kud → phase4_lt_generation → phase5_formatting → output_node
```

- **Phase 0/1 (acquire + scope):** `phases/phase0_acquisition/*`, `phases/phase1_ingestion.py`. Fetches a source URL (or `provided_text_file`), extracts and scopes text. Uses **Haiku** (`phase1_ingestion.py:460,494,743`).
- **Phase 2–5 (architecture → KUD → LT → format):** all use **Sonnet** (`phase2_architecture.py:75,143`; `phase3_kud.py:250,276,392`; `phase4_lt_generation.py:409,476,573`; `phase5_formatting.py:332`).
- Output object: `LearningTarget` (`types.py:469-508`).

### Pipeline B — Reference-authoring (`python -m curriculum_harness.reference_authoring.pipeline.run_pipeline …`)
Per-block authoring path used to build the REAL reference corpus:

```
inventory → KUD classify → cluster competencies → generate LTs → band statements
          → observation indicators → [criterion rubrics] → [supporting components]
```

- Stage order: `run_pipeline.py:1289-1592`. Every per-item stage defaults to **Sonnet** via `DEFAULT_MODEL = SONNET_MODEL` in each module (`kud/classify_kud.py:45`, `lt/generate_lts.py:49`, `lt/cluster_competencies.py:53`, `lt/generate_band_statements.py:63`, `lt/generate_observation_indicators.py:73`, `criterion/generate_criteria.py:77`, `criterion/generate_supporting_components.py:52`).
- **This is the pipeline that owns the decomposition gate and the five-level rubric generator.**

### Model constants (single source)
- `SONNET_MODEL = "claude-sonnet-4-20250514"` — `types.py:173`
- `HAIKU_MODEL  = "claude-haiku-4-5-20251001"` — `types.py:10`
- Cost table (advisory only) — `_anthropic.py:18-22`.

### Configs & seed data
`configs/*.json` (16 run configs) drive Pipeline A by URL. They are **clean** of REAL/level-name signatures (grep below). The REAL wellbeing artefacts live under `docs/reference-corpus/real-wellbeing/` and are read **only** by review/export scripts (`scripts/reference_authoring/render_*.py`, `export_reference_to_csv.py`), **never** by either generation pipeline.

---

## 1. Findings, ranked by severity

### 🔴 HIGH-1 — Output schema does not carry the LearnOS provenance/tag/modality spine
**Audit Q4.** The `LearningTarget` object (`types.py:469-508`) carries:
`statement, type, knowledge_type, assessment_route, kud_source, word_count, flags, lt_statement_format, source_provenance, kud_provenance`.

It does **not** carry, as first-class fields, any of the LearnOS spine the crosswalk requires (Brief C):

| LearnOS field needed | Present? | Evidence |
|---|---|---|
| Source benchmark ID (as published) | ❌ | no `source_id`/`benchmark_id` field in `types.py:469-508` |
| Verbatim source text (authoritative) | ⚠️ only as fuzzy match span | `source_provenance[].matched_text` is a *matched bullet*, not the parent benchmark — `source_faithfulness.py:8-24` |
| CASEL competency tag | ❌ | absent |
| Developmental band (explicit field) | ❌ | band lives in `level_statements`/band-statement stage, not on the target — `types.py:193-201, 469-508` |
| Social Thinking strategy-link field | ❌ | absent |
| Modality marker (decided/proposed/open) | ❌ | absent |

**Provenance is advisory, not authoritative.** `source_provenance` is a top-k **token-overlap** match with a `SOURCE_FAITHFULNESS_FAIL` flag (`source_faithfulness.py:1-24`). Its own docstring lists the failure modes: coarse items match trivially (#1), vocabulary injection can clear threshold (#2), empty corpus auto-passes (#5), no multi-bullet corroboration (#7), English-only matcher (#4). Real-run evidence: the England NC English v2 run flagged **19/26 LTs (73%)** as faithfulness-fail because "LTs are generated from `raw_curriculum` … which uses slightly different vocabulary" (`outputs/england-nc-english-2026-05-11/england_nc_english_ks1_to_ks3_2026_05_11_v2_analysis_v1.md:60,124`).

**Why it matters:** Brief B Step 3 and Fable checklist #2 require *every* target to trace to **verbatim** source text via a stable ID. The harness paraphrases the LT from scoped text and then tries to *re-discover* the link by lexical similarity. That is the wrong direction for LearnOS and will not survive the verification sample.

**Minimal change:** extend `LearningTarget` (and `KUDItem`) with explicit carried fields — `source_benchmark_id`, `source_verbatim` (copied forward, not re-matched), `casel_competency` (+ optional secondary), `developmental_band`, `strategy_links: list[{name, modality}]`, `modality: "decided"|"proposed"|"open"`. Thread the benchmark ID and verbatim text from Phase 1 extraction forward through KUD and LT emission rather than reconstructing it downstream.

---

### 🔴 HIGH-2 — Decomposition splits by knowledge *type*, not by *construct*
**Audit Q2.** The harness does have a decomposition mechanism, but it is type-keyed, not construct-keyed:

- **The rule** (`kud/prompts.py:33,49-51,133`): "COMPOUND RULE — MANDATORY … If a content block contains BOTH a Type 3 element AND a Type 1/2 element, it MUST be split." Splitting is triggered by a **mix of knowledge types**, and column mapping is by type.
- **The gate** (`gates/kud_gates.py:280-300`, `_gate_no_compound_unsplit`): checks only that each item's `(kud_column, knowledge_type, assessment_route)` triple is internally consistent. It halts on type↔route↔column mismatch — **not** on two same-type constructs sharing one item.

**Consequence:** a composite benchmark like *"the student identifies their emotions **and** regulates their emotions"* — two constructs, both plausibly Type 2/3 — passes the gate as a single item. Atomicity (one construct per target, Fable checklist #1) is **not enforced** for same-type composites. This is exactly why Brief B Step 2 schedules a **dedicated Opus decomposition pass** — the harness alone does not deliver construct atomicity.

**Smallest change that adds a real decomposition pass:**
1. Add an explicit atomicity instruction to `kud/prompts.py` ("one construct per item — split coordinated verbs/objects even within the same knowledge type") **and**
2. Insert an Opus construct-splitter between KUD classification and LT generation (Brief B Step 2), each child carrying `parent_benchmark_id` + verbatim (feeds HIGH-1). A prompt-only tweak is cheap but unverified; the Opus pass is what the brief already commits to and is the reliable fix.

---

### 🔴 HIGH-3 — Criterion subsystem emits the wrong rubric shape and pre-authors criteria content
**Audit Q5.** Two problems, one subsystem (`reference_authoring/criterion/`):

1. **Wrong shape.** `criterion_prompts.py:37-90` generates a **single-channel five-level rubric** (`no_evidence → emerging → developing → competent → extending`). LearnOS/Brief C requires **two channels**: *understanding 1–4* and *behavior/performance 0–4, support-graded*, with understanding gating behavior. The harness rubric collapses support and quality onto one axis (e.g. "heavily-supported" is baked into the `emerging` descriptor, `criterion_prompts.py:44`). It does **not** separate support condition from performance quality, and does **not** separate understanding from performance. It cannot be coaxed into the Social Thinking model by config.
2. **Pre-authors content.** The stage writes full descriptor prose per level (`generate_criteria.py:493`) — a fixed criteria library. Brief C is explicit: the tool drafts **rubric shape only**, per-goal, as editable clinician-owned proposals — never a pre-authored criteria corpus.

**Mitigation already in-repo:** `run_pipeline.py:881` `--skip-criteria` disables the rubric + supporting-components stages (`run_pipeline.py:1488-1489`). For the Minnesota job this stage **must be skipped**, and the two-channel rubric *shape* generated by a separate LearnOS-specific step (not this generator).

---

### 🟠 MEDIUM-1 — Live REAL-School reference inside a Phase-1 prompt string
**Audit Q3 (quarantine).** `phases/phase1_ingestion.py:367` — the `school_scoped_programme` extraction prompt contains the literal example *"(e.g. REAL School, academy, or district programmes)"*. This text is sent to the model.

- **Blast radius is narrow:** it fires only when `document_family == "school_scoped_programme"`. Minnesota's SEL framework is a state/national framework (`national_framework` / SEL grade-band), so this branch should not fire — but the brief's rule is absolute: *anything found is quarantined*.
- **Quarantine action:** replace "REAL School" with a neutral example ("e.g. a school-, academy-, or district-scoped programme"). One-line edit, deferred to the transform pass (this audit does not modify pipeline files).

---

### 🟡 LOW-1 — REAL-School wording in comments/docstrings (non-output-bearing)
**Audit Q3 (informational).** These are code comments/docstrings; they do **not** travel into any model call or output artefact, but are listed for completeness:

- `reference_authoring/types.py:419-420` — comment describing the removed A–D global as "REAL School Budapest's calibration".
- `reference_authoring/developmental_scope/detect_scope.py:138` — comment "Internal school framework (REAL School Budapest)"; plus source-type key `internal_school_framework` (map value, not emitted text).
- `reference_authoring/progression/detect_progression.py:5-14` — a **design-principle docstring stating the pipeline does NOT impose REAL bands**. This is protective, not a leak; keep it.
- `reference_authoring/progression/detect_progression.py:1282` — comment "only 4 of 6 REAL bands are represented" (frames a Circle Solutions seed table).
- `phases/phase4_lt_generation.py:104` and `criterion/criterion_prompts.py` / `gates/criterion_gates.py:3` — "five-level rubric" language (prompt-bearing, but part of HIGH-3, which is resolved by skipping the criterion stage).

Recommendation: scrub the comments during the transform pass for hygiene; none is a blocker.

---

### 🟢 PASS-1 — Model configuration runs entirely on Sonnet; nothing hard-coded to Opus
**Audit Q1.** Confirmed. No generation step is hard-coded to Opus.

- Pipeline A: Haiku (Phase 1 scoping) + Sonnet (Phases 2–5). No Opus reference anywhere in `phases/`.
- Pipeline B: every per-item stage defaults to `SONNET_MODEL` (citations in §0). The single CLI `--model` flag (`run_pipeline.py:850-852`) overrides all per-item stages at once, defaulting to Sonnet.
- The **only** Opus mentions in the whole package are: the advisory cost table (`_anthropic.py:21`), the family classifier (`_anthropic.py:79-80`), and an **optional** `--cluster-model` override suggested for KUDs >100 items (`run_pipeline.py:867-873`).

**Two minor notes (LOW):**
- The `--cluster-model` help text says the clustering default is "Haiku" (`run_pipeline.py:871`), but the code default is Sonnet (`cluster_competencies.py:53`). Stale help string — cosmetic; the effective default is Sonnet, which is *safer* for the "runs on Sonnet" guarantee.
- Model IDs are 4-generation (`claude-sonnet-4-20250514`, `claude-haiku-4-5-20251001`). They run fine; if a newer Sonnet is desired it is a two-constant edit in `types.py:10,173`. Not required for GO.

---

## 2. Cost estimate (Audit Q6)

Sonnet-4 pricing from `_anthropic.py:20`: **$3.00 / M input, $15.00 / M output**. The LearnOS path runs KUD-classify + LT-generate + tag, with the criterion stage **skipped**. The dominant cost driver is **3× self-consistency** (`DEFAULT_RUNS = 3`, `cluster_competencies.py` and peers).

**Per benchmark (Sonnet, self-consistency = 3):**

| Stage | Input tok | Output tok | Runs | Notes |
|---|---|---|---|---|
| KUD classify | ~2.5k | ~0.5k | ×3 | `kud/prompts.py` system ~2k |
| LT generate | ~2.0k | ~0.5k | ×3 | |
| Band statement | ~2.0k | ~0.5k | ×3 | only if grade-banded |
| Tag (CASEL+ST+band) | ~1.5k | ~0.3k | ×1 | new light stage |
| **Subtotal** | **~20k** | **~4.8k** | | |

Per-benchmark ≈ (20k × $3 + 4.8k × $15) / 1e6 ≈ **$0.06 + $0.072 ≈ $0.13**.

**Plus Opus decomposition** (composites only) — Opus $15/$75 (`_anthropic.py:21`): ~2k in / ~1k out ≈ **$0.11 per composite benchmark**.

**Corpus of 50–150 benchmarks:**
- Sonnet targeting+tagging: **$6.50 – $19.50**
- Opus decomposition (assume ~40% composite): 20–60 calls × $0.11 ≈ **$2 – $7**
- Haiku scoping: one-time per source document, **< $0.50**

**Total ≈ $10 – $30 for the full Minnesota corpus.** Cutting tagging self-consistency to 1× (it is a deterministic mapping, not a generative judgement) removes ~1/3 of the Sonnet cost. Cost is not a constraint.

---

## 3. Recommendation

### ✅ GO — conditional on the minimal change list below.

**Rationale.** The harness's **ingestion → KUD → LT spine is directly reusable and already Sonnet-native** (PASS-1), configs are clean-room-safe, and the REAL corpus is firewalled from both generation pipelines. The gaps are additive, not architectural: the object schema needs LearnOS fields (HIGH-1), atomicity needs the Opus pass the brief already plans (HIGH-2), and the wrong-shape criterion generator simply needs to be switched off and replaced with a rubric-shape step (HIGH-3). None of these requires rebuilding the pipeline. There is **no critical clean-room leak** into LearnOS output on the intended path; the one live prompt reference (MEDIUM-1) is in a branch Minnesota won't trigger and is a one-line quarantine regardless.

This maps cleanly onto the intended sequence: Brief A changes applied → Brief B runs extraction/tag on Sonnet, decomposition on Opus.

### Minimal change list (apply in the Brief-A→B transform pass; do not modify in this audit)

1. **Schema (HIGH-1).** Add to `LearningTarget`/`KUDItem`: `source_benchmark_id`, `source_verbatim`, `casel_competency` (+secondary), `developmental_band`, `strategy_links[{name, modality}]`, `modality`. Thread benchmark ID + verbatim **forward** from Phase 1; stop relying on downstream lexical re-matching for provenance.
2. **Decomposition (HIGH-2).** Add a one-construct-per-item instruction to `kud/prompts.py`, and insert the Opus construct-splitter (Brief B Step 2) between KUD classify and LT generation, each child carrying parent ID + verbatim.
3. **Rubric (HIGH-3).** Run with `--skip-criteria`. Build the **two-channel** rubric *shape* (understanding 1–4 gating behavior 0–4 support-graded) as a separate LearnOS step that emits editable proposals — never fixed criteria content.
4. **Quarantine (MEDIUM-1 / LOW-1).** Neutralise the "REAL School" example in `phase1_ingestion.py:367`; scrub REAL comments in `types.py:419-420`, `detect_scope.py:138`, `detect_progression.py:1282`. Keep the protective docstring at `detect_progression.py:5-14`.
5. **Tagging stage (new).** Add the CASEL + Social-Thinking + band tagger (Brief B Step 3), Sonnet, self-consistency 1×, every strategy link emitted as `modality: "proposed"`.
6. **Cost hygiene (optional).** Drop tagging to a single run; confirm the `--cluster-model` help string (`run_pipeline.py:871`) before it misleads an operator.

**Do-not-touch for the Minnesota job:** the REAL reference corpus under `docs/reference-corpus/real-wellbeing/` (firewalled), the five-level criterion generator (disabled, not deleted — still valid for the REAL track).

---

*End of audit. No pipeline files were modified in this pass.*
