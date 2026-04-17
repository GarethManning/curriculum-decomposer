# curriculum-decomposer harness log

In-repo session log. Every substantive Claude Code session on this
project appends an entry here at session close covering: what was
built, what commits were made (hashes), what was measured, and what
the next session should pick up.

Sessions are numbered; entries are dated. Baseline measurement
snapshots live alongside this file in `docs/project-log/`.

---

## Session 2 — 2026-04-17 — Source-evidence matcher + gates a/b/c

Judge-side session. No harness code changes. Built the source-
evidence matcher primitive and wrapped it into the three foundation-
moment-1 VALIDITY gates (source coverage, no-invention,
architecture verifiability).

### Commits

- `02917c3` [docs] create project log file
- `a04aa0e` [judge] add source-evidence matcher and fixture tests
- `b8be9cb` [judge] implement VALIDITY gates a/b/c using source-
  evidence matcher
- `a9a047e` [docs] record Session 2 baseline measurements for gates
  a/b/c
- `<this commit>` [docs] Session 2 log entry

### What was built

1. `eval/source_evidence_matcher.py` — pure-Python lexical matcher.
   Lemma Jaccard + char-4gram Jaccard hybrid. No new dependencies
   (PyTorch / spaCy / sentence-transformers flagged as a decision
   point at session start; Gareth chose pure-Python for v1).
2. `eval/test_cases/{known_good,known_bad}/` + `eval/test_matcher.py`
   — fixture tests that gate trust in the matcher before it runs on
   real data. 18/18 assertions passing; threshold 0.20 cleanly
   separates 0.43–1.0 known-good from 0.03–0.08 known-bad.
3. `scripts/validity-gate/_run_loader.py` — helper that hides
   runId-prefixed vs legacy plain filenames and builds the source-
   proxy corpus from Phase 1 `curriculum_profile` + Phase 2
   `architecture`.
4. Three gate scripts, replacing their stubs:
   - `validate_source_coverage.py`
   - `validate_source_faithfulness.py`
   - `validate_architecture_diagnosis.py`
5. `VALIDITY.md` and `scripts/validity-gate/README.md` updated to
   mark assertions a/b/c as **implemented** (were pending).

### Baseline measurements

See `docs/project-log/baseline-measurements-2026-04-17.md`.

Felvételi (`outputs/palya-felveteli-2026-04-17/`):
- coverage 18.8 % (13/16 source-proxy items orphaned)
- faithfulness 9.7 % (28/31 LTs flagged as potentially invented)
- architecture verifiability 100 % (6/6 strands)

Ontario (`outputs/ontario_grade7_history/`):
- coverage 0 %, faithfulness 0 %, verifiability 100 %
- Pre-v1.2 run without `strands[]` / `values_basis` — proxy corpus
  is just 13 short element labels + structural_flaw. Baseline is
  unreliable for this run; re-running under current harness would
  help.

**Session-brief checkpoint met.** The factorial LT (index 0 of the
felvételi run, REVIEW.md §2) is correctly flagged as potentially
invented at score 0.136.

**Known precision issue** documented in the baseline file: the gate
is high-sensitivity / lower-precision in proxy mode because the
Phase 1/2 English rendering of a Hungarian source is too thin for
fine-grained faithfulness matching. Session 3+ upgrade path: harness
emits a `_source_bullets_v1.json` artefact per run.

### What Session 3 should pick up

Session 1 diagnosis identified Shape C (Phase 3 profile-conditional
branching) as the next change to address the consolidation issue.
Session 3's natural scope:

1. Implement a Phase 3 entry branch that reads
   `curriculum_profile.scoping_strategy == "full_document"` +
   `document_family == "exam_specification"` +
   `has_mark_scheme == false` + `has_command_words == false` and
   selects a per-bullet-mode prompt/tool invocation instead of the
   current strand-aggregated call.
2. Re-run the felvételi config under the new Phase 3 and compare
   against Session 2's baseline. The gate's faithfulness percentage
   should move; the factorial LT should either disappear (if the
   per-bullet mode doesn't produce it) or remain (informative failure
   mode).
3. Populate `docs/run-snapshots/` with the new run (not created this
   session; will be first populated in Session 3).

Adjacent improvements Session 3 could fold in if scope allows:
- Emit `_source_bullets_v1.json` from Phase 1 so the gates can run
  against structured bullets rather than the proxy.
- Promote gate (d) LT surface form from stub — pure-Python syntactic
  check, no matcher needed.

### Open questions / concerns

- The 0.20 threshold is fixture-calibrated, not baseline-calibrated.
  Real proxy corpora produce a narrower distribution. Once Session 3
  produces a richer source artefact, re-calibrate.
- Gate (c) architecture verifiability passes at 100 % on both
  runs but the check is really "strands are internally coherent",
  not "strands match the source". Adjacent-mechanism declaration in
  the gate's docstring is explicit about this; revisit when the
  upgrade to per-bullet source is in.

---

<!-- next session entry goes here -->

