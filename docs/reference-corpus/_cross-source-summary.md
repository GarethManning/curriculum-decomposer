# Cross-source reference corpus summary
*Updated: 2026-04-19 — session 4b-5b.*

**Four sources** have passed through the full reference-authoring pipeline
including rubrics and supporting components. A fifth candidate source
(DfE KS3 Maths) was attempted in session 4b-5b and **halted at the KUD
quality gate** — see DfE KS3 section below for diagnosis.

Completed sources: Welsh CfW HWB (dispositional), Common Core G7 RP
(hierarchical), Ontario G7 History (horizontal), AP US Gov CED Unit 1
(horizontal — second horizontal, new in 4b-5b).

---

## Source inventory

| Source | Slug | Domain | Jurisdiction | Bands | Source type |
|---|---|---|---|---|---|
| Welsh CfW Health and Well-being | `welsh-cfw-health-wellbeing` | dispositional | Wales | 5 (PS 1–5) | `welsh_cfw_aole` |
| Common Core G7 Ratios & Proportional Relationships | `common-core-g7-rp` | hierarchical | USA (CCSS) | 1 (Grade 7) | `us_common_core_grade` |
| Ontario Grade 7 History | `ontario-g7-history` | horizontal | Ontario, Canada | 1 (Grade 7) | `ontario_grade` |
| AP US Gov & Politics CED Unit 1 | `ap-usgov-ced-unit1` | horizontal | USA (College Board) | 1 (Unit 1) | `us_ap_course_unit` |
| ~~DfE KS3 Maths~~ | ~~`dfe-ks3-maths`~~ | ~~hierarchical~~ | ~~England (DfE)~~ | — | — |

**DfE KS3 status:** Halted at `artefact_count_ratio` gate (71/17 = 4.18, outside
[0.8, 2.5] hierarchical band). See diagnosis section below. The DfE KS3 Maths
source as ingested (full KS3 curriculum, all strands, 9 pages) does not produce
reference-quality output. The second hierarchical source gap remains open.

---

## Pipeline counts

| Metric | Welsh CfW HWB | Common Core G7 RP | Ontario G7 History | AP US Gov CED U1 |
|---|---|---|---|---|
| Inventory blocks | 26 | 18 | 259 | 365 |
| KUD items | 33 | 22 | 188 | 67 |
| Halted blocks | 6 | 8 | 129 | 221 |
| — severe underspecification | 4 | 8 | 118 | 215 |
| — classification unreliable | 2 | 0 | 11 | 6 |
| Expected-yield blocks | 20 | 10 | 141 | 49 |
| Artefact-count ratio | 1.650 | 2.200 | 1.333 | 1.367 |
| Ratio domain band | [0.8, 2.2] (disp.) | [0.8, 2.5] (hier.) | [0.8, 1.5] (horiz.) | [0.8, 1.5] (horiz.) |
| KUD gate result | PASSED | PASSED | PASSED | PASSED |
| Competency clusters | 9 | 4 | 8 | 13 |
| Cluster model | Haiku | Haiku | Opus 4.6 | Haiku |
| Cluster stability | cluster_unstable | cluster_unstable | cluster_unstable | cluster_unstable |
| LTs | 20 | 8 | 13 | 26 |
| Halted LT clusters | 0 | 0 | 3 | 1 |
| Band-statement sets | 11 | 6 | 11 | 26 |
| Observation indicator sets | 5 | 0 | 2 | 0 |
| Criterion rubrics (Type 1/2) | 12 | 7 | 7 | 15 |
| Criterion gate pass | 11 | 6 | 6 | 10 |
| Criterion halted | 2 | 1 | 4 | 11 |
| Supporting components | 9 | 4 | 6 | 8 |
| Supporting halted | 2 | 2 | 0 | 2 |

---

## Knowledge-type distribution

| Type | Welsh CfW HWB | Common Core G7 RP | Ontario G7 History | AP US Gov CED U1 |
|---|---|---|---|---|
| Type 1 (know/understand) | 21 (64%) | 21 (95%) | 62 (33%) | 48 (72%) |
| Type 2 (do_skill) | 5 (15%) | 1 (5%) | 110 (59%) | 19 (28%) |
| Type 3 (do_disposition) | 7 (21%) | 0 (0%) | 16 (9%) | 0 (0%) |

**Observations:**

- **Welsh CfW** has the highest Type 3 share (21%), consistent with a
  dispositional curriculum domain that explicitly describes sustained
  orientations.
- **Common Core** is almost purely Type 1 (95%) — the standard text
  states specific procedural and declarative content; there is one
  analytical item (Type 2) embedded in a reasoning standard.
- **Ontario G7 History** is predominantly Type 2 (59%) — inquiry and
  analytical skills tied to specific historical contexts — consistent
  with the horizontal domain. Type 3 items (9%) correspond to FOCUS ON
  historical-thinking concepts (Continuity and Change, Historical
  Perspective, etc.) that are described in the source as sustained
  orientations.
- **AP US Gov CED Unit 1** is predominantly Type 1 (72%) — the AP CED
  describes constitutional structures, historical context, and political
  science concepts with high declarative density. Type 2 items (28%)
  are analytical and application skills (argument construction, source
  analysis, scenario application). Zero Type 3: Unit 1 covers
  "Foundations of American Democracy" — institutional knowledge and
  analytical skills, not dispositional orientations. This is expected
  for a college-board exam-prep source scoped to constitutional content.

---

## Artefact-count ratios

| Source | Items | Expected-yield blocks | Ratio | Band | Status |
|---|---|---|---|---|---|
| Welsh CfW | 33 | 20 | 1.650 | [0.8, 2.2] dispositional | PASS |
| Common Core G7 RP | 22 | 10 | 2.200 | [0.8, 2.5] hierarchical | PASS |
| Ontario G7 History | 188 | 141 | 1.333 | [0.8, 1.5] horizontal | PASS |
| AP US Gov CED U1 | 67 | 49 | 1.367 | [0.8, 1.5] horizontal | PASS |
| DfE KS3 Maths | 71 | 17 | 4.176 | [0.8, 2.5] hierarchical | **FAIL** |

**Observations:**

- Welsh CfW's 1.65 ratio drove the 4b-2 provisional ceiling revision for
  dispositional sources (raised to 2.2). Its ratio sits comfortably below
  the revised ceiling.
- Common Core's 2.2 ratio drove the 4b-3 ceiling revision for hierarchical
  sources (raised to 2.5). Small denominator (10 blocks) means high
  sensitivity to LLM non-determinism: each item adds 0.1 to the ratio.
- Ontario's 1.333 ratio is the lowest of the three and fits comfortably
  within the horizontal band [0.8, 1.5] without triggering any gate
  revision.
- AP US Gov CED Unit 1's 1.367 ratio is the second horizontal source; it
  closely matches Ontario's 1.333. Two horizontal sources at 1.3–1.4
  confirms the horizontal band [0.8, 1.5] is well-calibrated. Note: high
  halt rate (77% of classified blocks) is expected — the CED format is
  dense with administrative/organisational text that classifies as severe
  underspecification.
- **DfE KS3 Maths FAIL (4.18):** The full KS3 Mathematics programme of
  study (all strands, 9 pages) is fundamentally denser than Common Core
  G7 RP (a single domain within one grade). 71 items from 17
  expected-yield blocks = 4.18, nearly double the hierarchical ceiling.
  Additionally, 64/71 items (90%) are classification_unstable — the
  classifier cannot reliably distinguish Know/Understand/Do-Skill on dense
  multi-concept curriculum paragraphs. This is an honest halt, not a
  threshold calibration problem. See DfE KS3 diagnosis below.

---

## Cluster stability

All four completed sources produced `cluster_unstable` overall — no source achieved
`stable` at the cluster level. The specific drivers differ by source:

- Welsh CfW (9 clusters, 33 items, Haiku): small items-per-cluster
  denominator amplifies Jaccard sensitivity. Cluster content is correct on
  manual review.
- Common Core (4 clusters, 22 items, Haiku): 4b-3 run; cluster_unstable
  driven by dominant-type drift on one cluster, not membership drift. Small
  source.
- Ontario (8 clusters, 188 items, **Opus 4.6**, 4b-5 re-run): membership
  drift **0% (vs run-2) / 9.57% (vs run-3)**, both below the 20% threshold.
  Residual instability is `cluster_count_differs [8, 8, 7]` and
  `cluster_missing_in_run3` (one canonical cluster has no Jaccard≥0.30 match
  in run 3). Prior Haiku run (4b-3) had 43.09% membership drift on 11
  clusters — escalation to Opus was load-bearing for the DoD target.
- AP US Gov (13 clusters, 67 items, Haiku, 4b-5b): `cluster_unstable`
  driven by `cluster_count_differs [13, 12, 13]` and one cluster missing in
  runs 2 and 3 (`cluster_07: Federalism`). Not membership drift — the
  cluster content is substantively stable; the instability is a count and
  match-threshold artefact. 67 items well below the Opus threshold (100);
  Haiku clustering was appropriate.

`cluster_unstable` is flagged for human review but is not a halting
condition. Across all four sources, the cluster boundaries on visual
inspection follow the source's organising structure correctly.

### Ontario downstream honest halts (4b-5)

The Opus re-clustering consolidated Ontario's prior 11 clusters into 8
larger, thematically coherent clusters (e.g. splitting by era 1713–1800
vs 1800–1850, each with Continuity/Change, Perspectives, and Causes
/Consequences/Significance dimensions). Three of the eight clusters
halted LT generation under Haiku (0/3, 1/3, 0/3 parseable runs) — all
three clusters are large (23, 34, 31 items). This produced 13 LTs from
5 productive clusters, below the prior 23-LT Haiku output (which itself
came from unstable 11-cluster output). Downstream: 4 of 11 Type 1/2
LTs halted at the rubric stage (`rubric_unreliable`), producing 7
rubrics of which 6 pass criterion gates. Pattern of halt reasons is
consistent with prior anchors (parse-reliability ceiling on Haiku); the
reduced absolute counts reflect Opus's cleaner consolidation, not a
regression.

---

## Observation indicators (Type 3)

| Source | Indicator sets |
|---|---|
| Welsh CfW | 5 |
| Common Core | 0 (no Type 3 items) |
| Ontario | 2 |
| AP US Gov CED U1 | 0 (no Type 3 items) |

Welsh CfW has the richest observation-indicator output, matching its
dispositional domain. Ontario's 2 indicator sets in the 4b-5 re-run
come from the two Type 3 LTs that survived clustering + LT generation
under Opus clusters. The FOCUS ON disposition KUD items are
distributed across multiple clusters; most were placed into Type 2-
dominated clusters during Opus clustering, so their corresponding LTs
(if any survived LT generation) are Type 2. The FOCUS ON verification
stage records classifier disagreement with the Seixas/Morton placement
rule rather than silently over-routing to Type 3 (see below).

AP US Gov CED Unit 1 has zero Type 3 items — the CED describes
constitutional knowledge and analytical skills without sustained
dispositional language. This is consistent with the exam-prep genre:
Unit 1 specifies essential knowledge and analytical tasks, not
character orientations. Zero observation indicators is the correct
result for this source.

---

## Criterion rubrics (Type 1/2)

*Updated 2026-04-19, session 4b-5b: AP US Gov row added.*

| Source | Rubrics | Gate pass | Halted | Stable | Unstable | Thin-flag | Supporting components | Supporting halted |
|---|---|---|---|---|---|---|---|---|
| Welsh CfW HWB | 12 | 11 | 2 | 5 | 7 | 2 | 9 | 2 |
| Common Core G7 RP | 7 | 6 | 1 | 4 | 3 | 2 | 4 | 2 |
| Ontario G7 History | 7 | 6 | 4 | 4 | 3 | 2 | 6 | 0 |
| AP US Gov CED U1 | 15 | 10 | 11 | 5 | 10 | 4 | 8 | 2 |

**Observations:**

- On both corpora the criterion gate passes on the vast majority of
  rubrics that converged under 3x self-consistency: 11/12 (Welsh CfW)
  and 6/7 (Common Core). The single gate fail on each is a
  `single_construct` halt on a Type 2 LT that bundles multiple
  skills — expected structural behaviour, not rubric-quality
  noise.
- Halts are predominantly `rubric_unreliable` driven by signature
  disagreement across self-consistency runs; after the 4b-4 Step 5
  signature relaxation (within-limit word counts collapsed to a
  single class; scope reduced to binary scoped/unscoped) convergence
  stabilised at ~85–90% on both corpora. Remaining halts are
  parse-reliability failures on a small number of LTs where Haiku
  failed to emit strict JSON on 2+ of 3 runs (documented per-corpus).
- The propositional-thin flag surfaces on both corpora (2 and 2),
  always on factual Type 1 LTs where the rubric necessarily compresses
  at Emerging/Developing because there is no intermediate performance
  to describe between "has the fact" and "does not". The flag is
  informational, not a gate failure.
- Supporting-components stage lags the rubric stage by exactly the
  number of halted rubrics plus a small number of additional halts on
  LTs that passed the rubric gate but produced unstable co-construction
  prompts. The gap is small and consistent across both corpora.
- Ontario G7 History (4b-5 re-run): 7 rubrics from 11 Type 1/2 LTs;
  4 halts all `rubric_unreliable` driven by parse-reliability (0/3
  or 1/3 runs producing valid output). 6 pass criterion gates; 0
  supporting-components halts. Outputs are below the 15–20 rubric
  projection in the v3 plan's DoD — that projection assumed the prior
  Haiku clustering's 23 LTs; Opus's consolidated 8 clusters with 3
  large-cluster LT halts produced a lower LT pool, and therefore a
  lower rubric count. Honest halt, not a regression.
- **AP US Gov CED Unit 1 (4b-5b):** 15 rubrics from 26 Type 1/2 LTs;
  11 LTs halted — all `rubric_unreliable` (signature disagreement or
  0/3 parseable runs). This is a higher halt rate than previous sources
  (42% vs ~15–27%). The AP CED's constitutional vocabulary is highly
  technical and propositional; Haiku's rubric generator shows more
  instability on political-science terminology than on general
  curriculum language. Gate passes: 10/15 (67%); 5 fail on
  `single_construct`. Propositional-thin flag on 4 rubrics — highest
  thin-flag count yet, consistent with the high declarative density of
  constitutional knowledge LTs. 8 supporting components from 10
  passing rubrics (2 additional halts).

  The higher rubric halt rate (42%) vs prior anchors raises a signal
  to carry into 4b-7: Haiku may need LT-gen-model escalation (analogous
  to the Ontario `--cluster-model` escalation) for rubric generation on
  Type 1 LTs from politically/constitutionally technical domains. This
  is an open question, not a blocking defect.

---

## FOCUS ON verification (Ontario)

Ontario content includes `FOCUS ON` tags for four historical-thinking
concepts (Continuity and Change, Cause and Consequence, Historical
Perspective, Historical Significance) that are described in the source
as sustained orientations. The pipeline was run with `--focus-on-priming`
(Seixas/Morton Big Six descriptions injected as `source_context`).

**Outcome: `unstable`.**

- 7 FOCUS ON items identified in the KUD.
- 0 items agree (Type 3 Do-Disposition per priming rule).
- 1 item disagrees: `blk_0102_item_02` (Historical Significance) was
  classified Type 2 Do-Skill by the classifier with this rationale:
  *"occasion-triggered analytical skill deployed when asked to assess
  significance of a specific event ... not a sustained orientation."*
- 6 items are `classification_unstable` — the placement could not be
  resolved consistently across the three self-consistency runs.

**Interpretation.** The FOCUS ON priming injected the Type 3 placement
instruction but the classifier disagreed on most items — either reading
the source text as describing a specific occasion-triggered task (Type 2)
rather than a sustained default orientation (Type 3), or producing unstable
output. The pipeline records this as disagreement, not a silent override.
This is working as designed (verification-flag-disagreement discipline).

The substantive question — whether Ontario FOCUS ON concepts are Type 3
or Type 2 — requires curriculum-expert review. The disagreement data is
preserved in `quality_report.md`.

---

## DfE KS3 Maths — honest halt diagnosis (4b-5b)

**Status:** Halted at `artefact_count_ratio` KUD gate. Not a reference corpus.

**Findings:**

- 46 inventory blocks, 29 severely underspecified → 17 expected-yield blocks.
- 71 KUD items from 17 blocks = ratio 4.18, outside hierarchical [0.8, 2.5].
- 64/71 items (90%) classified as `classification_unstable` — the highest
  instability rate seen on any source.
- Progression detection: before the fix in 4b-5b, the source-text fallback
  produced a 3-band KS1/KS2/KS3 structure (because the KS3 Maths document
  references KS2 as prior work). After adding a `dfe-ks3` curated entry to
  `detect_progression.py`, the structure is correctly `england_nc_ks3_only |
  1 band(s) | confidence=high`. This does NOT unblock the ratio gate.

**Root cause:** The source is mismatched to the reference-authoring scope
expectation. Common Core G7 RP covers a single domain within a single grade
(~22 items, single strand). DfE KS3 Maths covers the **entire** KS3
Mathematics programme of study — Number, Algebra, Ratio, Geometry,
Probability, Statistics — across all of Years 7-9 (~9 pages, all strands).
The ratio gate correctly flags this mismatch. The 90% classification
instability corroborates the diagnosis: dense multi-strand curriculum
paragraphs produce ambiguous boundaries between Know/Understand/Do-Skill.

**Not a threshold calibration problem.** The gate threshold is not wrong.
A hierarchical maths source scoped to a single strand (e.g., DfE KS3 Maths
— Number strand only) would plausibly pass. The full-programme document is
too broad.

**Action required (for a future session):** Re-ingest a scoped DfE KS3 Maths
source — one strand only (e.g., Number, or Algebra) — analogous to Common
Core G7 RP's single-domain scoping. The Phase 0 artefact at
`docs/run-snapshots/2026-04-18-session-4a-4-5-dfe-ks3-maths-pdf` can be
retained as documentation; a new ingestion is needed for the scoped source.
The second hierarchical source gap remains open.

**Files preserved:** `docs/reference-corpus/dfe-ks3-maths/` contains
`inventory.json`, `kud.json`, `quality_report.json`, `quality_report.md`,
and `progression_structure.json` (diagnosis artefacts only; no clusters,
LTs, or rubrics).

---

## Gate revision history driven by this corpus

| Revision | Session | Trigger | Change |
|---|---|---|---|
| 4b-2: dispositional ceiling | 4b-1/4b-2 | Welsh CfW ratio=1.65 | hierarchical/horizontal ceiling stays 1.5; dispositional raised to 2.2 (PROVISIONAL) |
| 4b-3: hierarchical ceiling | 4b-3 | Common Core G7 RP ratio=2.2 | hierarchical ceiling raised to 2.5 |

Horizontal confirmed at [0.8, 1.5] by two independent sources (Ontario
ratio=1.333, AP US Gov ratio=1.367 — 4b-5b). No revision triggered.

The DfE KS3 Maths ratio=4.18 FAIL does **not** indicate the hierarchical
ceiling needs further revision. The source scope (full-programme vs.
single-domain) is the mismatch; the gate is performing correctly.

---

## Code fixes driven by this corpus

| Fix | Commit | Trigger |
|---|---|---|
| Clustering max_tokens 4096→8192, drop source_blocks for >80 items | `dbcb857` | Ontario 188-item KUD exceeded output budget; 0/3 clustering runs valid |
| Clustering validator: recover duplicates and ≤3 missing items | `cee3aae` | Ontario clustering: 1 item duplicated, 1 item dropped; strict validator rejected valid runs |
| Progression detection: AP US Gov CED + DfE KS3-only curated entries | 4b-5b | AP US Gov halted at progression detection (no prior entry); DfE text-inspection produced wrong multi-KS structure |

---

*Cross-source summary last updated: 2026-04-19, session 4b-5b.*
