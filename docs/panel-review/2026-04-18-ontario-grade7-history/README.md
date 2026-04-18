# Ontario Grade 7 History — panel-review package (2026-04-18)

## What the Curriculum Harness is

A curriculum-to-artefact translation pipeline. Ingests a source curriculum
document, extracts source bullets, diagnoses the document's knowledge
architecture, and emits downstream artefacts for an AI tutoring system.

## What the four artefacts are

Per `docs/vision/binding-specifications.md`, the harness targets four
artefact families in curriculum mode:

- **Architecture diagnosis.** A classification of the source document's
  knowledge architecture — hierarchical / horizontal / dispositional
  proportions, strands, and auto-assessable fraction. Drives downstream
  grain and routing decisions.
- **KUD map.** Know / Understand / Do four-column decomposition of the
  curriculum, each item carrying a knowledge type (Sequential,
  Horizontal, Dispositional) and an assessment route.
- **Learning targets (LTs).** Teacher-assessment-grain statements
  aligned to the KUD items. In curriculum mode the ratio is ~1:1 with
  KUD items (±20%). Statement format resolves to `i_can` for Ontario
  under the v1.3 resolver.
- **Pedagogical criterion bank.** Per-LT success criteria. In this run
  Phase 5 (criterion-bank structuring) was skipped because the
  architecture diagnosis had no strands; see "Known incomplete state"
  below.

## Known incomplete state — please read before reviewing

The panel should review this output knowing the following observed
limitations. These are properties of the current harness at commit
`f023c8e`, not of the source document.

1. **Phase 1 scoping did not narrow to Grade 7.** The scoped slice
   pulled the whole K–8 document through Grade 1's specific
   expectations, stopping before Grade 7. `run-outputs/
   ontario_session3e_panel_pkg_source_bullets_v1.json` contains
   primarily front-matter and Grade 1 content. Every downstream
   artefact was generated against this incorrectly-scoped extraction.
2. **Phase 2 architecture diagnosis timed out** on this run (240 s
   API timeout). The architecture JSON is empty with
   `structural_flaw: timeout_phase2`.
3. **Phase 5 was skipped** because Phase 2's architecture had no
   strands to structure against. No `structured_lts` artefact was
   produced, and no criterion-bank artefact was produced.
4. **Phase 4 regeneration loop exhausted retries on every LT.** All
   22 LTs are flagged `SOURCE_FAITHFULNESS_FAIL` after regeneration
   against the mis-scoped source bullets; 20 exhausted retries and 2
   aborted on near-identical regeneration.
5. **MCP server instability.** Phase 3 and Phase 4 each fell back to
   Sonnet-direct on multiple calls due to intermittent MCP
   connection errors. This is known flaky infrastructure, not a
   model-quality signal.

The panel is being asked to evaluate what the harness produced against
an Ontario Grade 7 History reviewer's mental model — including whether
the output is at the right grade, the right grain, and captures the
disciplinary thinking the curriculum requires.

## Factorial-LT-equivalent concern for Ontario

Earlier sessions on Hungarian felvételi (exam-spec mode) surfaced a
class of defects the existing flags do not catch: LTs invented from
combinatorial expansion of source terms, at wrong grain, or missing
entirely. Existing faithfulness flags are lexical and will miss
semantic invention or topic omission.

**Ask of panel:** identify invented LTs (content not in the Grade 7
History curriculum), grain mismatches (e.g. specific-skill LTs against
strand-level KUD items, or vice versa), and missed content (Grade 7
History material not represented). Do not assume the existing flags
surface these.

## Architectural context

- `docs/vision/binding-specifications.md` — load-bearing v4.1 vision
  specifications. Two-tool architecture, curriculum vs exam-spec
  modes, numeric thresholds, provenance commitment.
- `VALIDITY.md` — validity gates a–d and their implementation status.
- `docs/project-log/harness-log.md` — session-by-session build log,
  including Session 3d's bullet-type recalibration that made the
  Phase 1 scoping failure visible.

## Package contents

- `source.md` — URL + metadata for the source PDF (not mirrored in
  repo).
- `run-outputs/` — the full Session 3e-run output directory, copied
  verbatim. Artefacts:
  - `*_source_bullets_v1.json` — Phase 1 extraction (937 bullets).
  - `*_curriculum_profile_v1.json` — Phase 1 profile.
  - `*_architecture_v1.json` — Phase 2 diagnosis (empty; see above).
  - `*_kud_v1.json` — Phase 3 KUD (22 items, strand-aggregated
    branch).
  - `*_learning_targets_v1.json` — Phase 4 LTs (22 items, all flagged).
  - `*_regeneration_events_v1.json` — Phase 4 regeneration loop log.
  - `*_human_review_queue_v1.json` — LTs routed to human review.
  - `*_run_report_v1.md` — human-readable run summary.
- `questions-for-panel.md` — the six questions each panelist is asked
  to address.

## Run metadata

- Commit: `f023c8e` (Session 3d completion).
- Run ID: `ontario_session3e_panel_pkg`.
- Config: `configs/ontario_session3e_panel_pkg.json` (Session 3d config
  with a new runId + output path).
- Date: 2026-04-18.
- Exit code: 0.
- Phase errors observed: Phase 2 timeout @ 240 s; Phase 5 skipped (no
  strands).
