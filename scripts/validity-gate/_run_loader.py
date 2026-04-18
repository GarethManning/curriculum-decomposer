"""Helpers for validity-gate scripts that read a curriculum-harness
run directory.

A "run directory" is `outputs/<run>/` and contains some subset of:
  - `<runId>_curriculum_profile_v1.json` or `curriculum_profile_v1.json`
  - `<runId>_architecture_v1.json`          or `architecture_v1.json`
  - `<runId>_kud_v1.json`                   or `kud_v1.json`
  - `<runId>_learning_targets_v1.json`      or `learning_targets_v1.json`
  - `<runId>_source_bullets_v1.json`        or `source_bullets_v1.json`  (v3a+)

This module hides the runId-prefixed-vs-plain naming convention and
builds the source corpus that the three foundation-moment-1 gates
match against.

### Corpus selection — bullets preferred, proxy fallback

Since Session 3a (2026-04-18) Phase 1 emits a discrete
`_source_bullets_v1.json` artefact (topic statements / numbered
outcomes / marker bullets extracted from the Phase 1 scoped text).
Bullet-level granularity raises the matcher's precision sharply over
the Session-2 proxy corpus, which inflated orphan counts because it
only had strand-label-coarse items.

`load_run()` prefers the bullet artefact when present; falls back to
the proxy and sets `corpus_mode = "proxy"` with a warning when absent.

### Session 3d — bullet_type weighting

The 937-bullet Ontario run (Session 3c) produced a coverage denominator
dominated by front-matter, sample questions, and cross-grade content.
Session 3d adds a semantic `bullet_type` field on every bullet (see
`curriculum_harness/source_bullets.py`) and this loader now filters by
bullet_type when building the coverage corpus:

- `coverage_relevant` (used by all three gates): `specific_expectation`,
  `overall_expectation`. Source items that a Grade-N KUD should trace
  to.
- `illustrative` (reported but excluded from coverage): `sample_question`,
  `teacher_prompt`. Surfaced as a separate bucket so gate reports can
  cite them for teacher reference.
- `excluded` (reported but excluded): `front_matter`, `other`. Large
  counts here (>20 by default) are flagged as a review signal, since
  it means Phase 1 scoping let in a lot of non-content.
- `extraction_errors`: `cross_grade`. These are extraction mistakes,
  not content — reported as a diagnostic.

Backwards compatibility: when a bullet has no `bullet_type` field, or
its `bullet_type` value is one of the pre-Session-3d detector names
(``marker_bullet``, ``numbered_outcome``, ``topic_statement``), this
loader reclassifies the bullet via
`curriculum_harness.source_bullets.classify_bullet_type` so old
artefacts (e.g. the Session 3c Ontario snapshot) can be rebaselined
against the Session 3d rules without re-running the harness.

### When the proxy fallback kicks in — and why its baseline is unreliable

The proxy mode exists for backwards compatibility with runs predating
Session 3a that never emitted bullets. Its corpus is the pipeline's
own *English rendering* of the source:
`curriculum_profile.rationale`, strand labels + `values_basis`,
hierarchical / horizontal / dispositional element lists,
`structural_flaw`. For a Hungarian source (felvételi), this means
matching English LTs against the English re-rendering of a Hungarian
bullet list — an accidental dependency that systematically
under-scores. Any baseline taken in proxy mode is high-sensitivity /
low-precision and should not be compared against a baseline taken in
bullets mode.

### Adjacent mechanisms — what this module does NOT do

1. **Bullet importance weighting within a type.** All
   `specific_expectation` bullets count equally in the coverage
   denominator; a broad A2.1 ("formulate questions to guide
   investigations") and a narrow A3.5 ("treat others with respect")
   are indistinguishable.
2. **Grade verification.** A bullet tagged `specific_expectation`
   structurally might still be at the wrong grade — the classifier
   in `source_bullets.py` is structural, not grade-aware beyond the
   `(Grade N)` in-text tag heuristic.
3. **Curriculum-specific mis-tagging.** The Session-3d heuristics are
   Ontario-calibrated. AP CED / IB / UK NC bullets may mis-tag until
   separately calibrated.
4. **Threshold on "excluded-by-default" bucket.** The 20-bullet review
   threshold is a working default; operators should override per
   source when the structural noise floor is known.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Make the harness package importable when this loader runs as a script
# (e.g. `python scripts/validity-gate/validate_source_coverage.py ...`).
ROOT = Path(__file__).parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from curriculum_harness.source_bullets import (  # noqa: E402
    BULLET_TYPES,
    classify_bullet_type,
)

# Session 3d bucket membership.
_COVERAGE_RELEVANT = {"specific_expectation", "overall_expectation"}
_ILLUSTRATIVE = {"sample_question", "teacher_prompt"}
_EXTRACTION_ERRORS = {"cross_grade"}
_EXCLUDED = {"front_matter", "other"}

# Pre-Session-3d bullet_type values (detector names). Treated as
# "needs reclassification" by `_normalise_bullet`.
_LEGACY_DETECTOR_NAMES = {
    "marker_bullet",
    "numbered_outcome",
    "topic_statement",
}

# Threshold above which a large `excluded` bucket is flagged in the
# loader's diagnostic warning. See adjacent mechanism #4.
_EXCLUDED_REVIEW_THRESHOLD = 20


@dataclass(frozen=True)
class SourceItem:
    """One item in the source-proxy or source-bullets corpus.

    `provenance` — where this item came from in the run dir, so reports
    can cite it. Examples: "architecture.strands[2].label",
    "source_bullets.sb_037 (specific_expectation)".

    `bullet_type` — semantic category when the corpus is built from
    bullets (Session 3d). Empty string in proxy mode.
    """

    text: str
    provenance: str
    bullet_type: str = ""


@dataclass
class RunArtefacts:
    run_dir: Path
    curriculum_profile: dict | None
    architecture: dict | None
    learning_targets: list[dict]
    # Coverage-relevant corpus (for all three foundation-moment-1
    # gates). In `corpus_mode="bullets"` this is
    # specific_expectation + overall_expectation. In `corpus_mode="proxy"`
    # it is the full proxy corpus (unfiltered — proxy mode has no
    # bullet_type metadata).
    source_corpus: list[SourceItem]
    # "bullets" when built from `_source_bullets_v1.json`, "proxy" when
    # falling back to Phase 1/2 artefacts. Proxy-mode baselines are
    # unreliable (see module docstring).
    corpus_mode: str
    # Human-readable warning when corpus_mode is "proxy", the bullet
    # artefact was found but empty, or the `excluded` bucket exceeds
    # the review threshold. Empty string on happy path.
    corpus_warning: str
    # Session 3d — diagnostic buckets. Empty in proxy mode.
    illustrative_bullets: list[SourceItem] = field(default_factory=list)
    excluded_bullets: list[SourceItem] = field(default_factory=list)
    extraction_error_bullets: list[SourceItem] = field(default_factory=list)
    # Counts by semantic bullet_type, useful for reports. Keys are the
    # enum values from `curriculum_harness.source_bullets.BULLET_TYPES`
    # plus ``total``. Empty in proxy mode.
    bullet_type_counts: dict[str, int] = field(default_factory=dict)


def _find_json(run_dir: Path, suffix: str) -> Path | None:
    """Find `<runId>_<suffix>` or plain `<suffix>` inside run_dir."""
    # Preferred: runId-prefixed filename.
    hits = sorted(run_dir.glob(f"*_{suffix}"))
    if hits:
        return hits[0]
    # Legacy: plain filename.
    plain = run_dir / suffix
    if plain.exists():
        return plain
    return None


def _load_json(path: Path | None) -> dict | None:
    if path is None:
        return None
    return json.loads(path.read_text())


def _build_source_corpus(
    profile: dict | None, architecture: dict | None
) -> list[SourceItem]:
    items: list[SourceItem] = []

    if profile:
        if rationale := profile.get("rationale"):
            items.append(
                SourceItem(rationale, "curriculum_profile.rationale")
            )
        hints = profile.get("source_hints") or {}
        if pages_note := hints.get("pages_note"):
            items.append(
                SourceItem(pages_note, "curriculum_profile.source_hints.pages_note")
            )
        assess = profile.get("assessment_signals") or {}
        if fmt := assess.get("format"):
            items.append(
                SourceItem(fmt, "curriculum_profile.assessment_signals.format")
            )

    if architecture:
        strands = architecture.get("strands") or []
        # v1.2+ shape: architecture.strands[] with label + values_basis.
        for i, strand in enumerate(strands):
            label = strand.get("label") or ""
            basis = strand.get("values_basis") or ""
            combined = (label + ". " + basis).strip(". ").strip()
            if combined:
                items.append(
                    SourceItem(combined, f"architecture.strands[{i}].label+values_basis")
                )
            # Strand IDs carry hyphen-separated content tokens
            # ("procedural-fluency-habits") that expand the lexical
            # coverage of the corpus without restating the label.
            sid = strand.get("id") or ""
            if sid:
                expanded = sid.replace("-", " ").replace("_", " ")
                items.append(
                    SourceItem(expanded, f"architecture.strands[{i}].id")
                )
        # Legacy element lists are only used when strands[] is absent
        # (pre-v1.2 runs). When strands[] exists, the element lists are
        # just the strand labels in another shape; adding them back
        # creates short label-only items that inflate false positives
        # on LTs sharing generic subject vocabulary.
        if not strands:
            for key in (
                "hierarchical_elements",
                "horizontal_elements",
                "dispositional_elements",
            ):
                for j, el in enumerate(architecture.get(key) or []):
                    if el:
                        items.append(SourceItem(el, f"architecture.{key}[{j}]"))
        # Structural flaw commentary carries subject-specific vocabulary
        # useful for faithfulness matching.
        if flaw := architecture.get("structural_flaw"):
            items.append(SourceItem(flaw, "architecture.structural_flaw"))

    return items


def _normalise_bullet_type(b: dict) -> str:
    """Return the Session-3d semantic bullet_type for a bullet dict.

    Handles three shapes:
    - Session 3d artefact: ``bullet_type`` is already a semantic enum
      value — returned as-is.
    - Pre-Session-3d artefact: ``bullet_type`` holds a detector name
      (``marker_bullet``/``numbered_outcome``/``topic_statement``) and
      no ``detector`` field exists. Reclassified via
      ``classify_bullet_type`` using the detector name recovered from
      the old ``bullet_type`` field.
    - Missing field: reclassified with an empty detector, which still
      lets the heuristic apply the text-level rules (``?`` terminator,
      ``e.g.``, ``(Grade N)``).
    """
    btype = (b.get("bullet_type") or "").strip()
    if btype in BULLET_TYPES:
        return btype
    # Legacy shape: bullet_type is the detector name.
    if btype in _LEGACY_DETECTOR_NAMES:
        detector = btype
    else:
        detector = (b.get("detector") or "").strip()
    return classify_bullet_type(
        str(b.get("text") or ""),
        str(b.get("source_location") or ""),
        detector,
    )


def _build_bullet_buckets(
    bullets_doc: dict,
) -> tuple[
    list[SourceItem],        # coverage_relevant
    list[SourceItem],        # illustrative
    list[SourceItem],        # excluded
    list[SourceItem],        # extraction_errors
    dict[str, int],          # counts by bullet_type
]:
    """Bucket a bullets artefact by semantic bullet_type."""
    coverage: list[SourceItem] = []
    illustrative: list[SourceItem] = []
    excluded: list[SourceItem] = []
    errors: list[SourceItem] = []
    counts: dict[str, int] = {t: 0 for t in BULLET_TYPES}

    for b in bullets_doc.get("source_bullets") or []:
        text = (b.get("text") or "").strip()
        bid = (b.get("id") or "").strip()
        if not text or not bid:
            continue

        btype = _normalise_bullet_type(b)
        counts[btype] = counts.get(btype, 0) + 1
        prov = f"source_bullets.{bid} ({btype})"
        item = SourceItem(text, prov, btype)

        if btype in _COVERAGE_RELEVANT:
            coverage.append(item)
        elif btype in _ILLUSTRATIVE:
            illustrative.append(item)
        elif btype in _EXTRACTION_ERRORS:
            errors.append(item)
        else:
            excluded.append(item)

    counts["total"] = sum(counts.get(t, 0) for t in BULLET_TYPES)
    return coverage, illustrative, excluded, errors, counts


def load_run(run_dir: str | Path) -> RunArtefacts:
    """Load a run's Phase 1/2/4 JSON and build the source corpus.

    Corpus selection:
    - If `_source_bullets_v1.json` is present and non-empty, the corpus
      is built from its bullets (`corpus_mode = "bullets"`). Session 3d
      filters that corpus to coverage-relevant bullet_types only;
      illustrative / excluded / extraction-error buckets are exposed
      separately for diagnostic reporting.
    - Otherwise the Phase 1/2 proxy is used with a warning
      (`corpus_mode = "proxy"`) — see module docstring.

    Raises FileNotFoundError if `learning_targets` JSON is missing —
    gates cannot run without it.
    """
    run_dir = Path(run_dir)
    if not run_dir.is_dir():
        raise FileNotFoundError(f"run directory does not exist: {run_dir}")

    profile = _load_json(_find_json(run_dir, "curriculum_profile_v1.json"))
    architecture = _load_json(_find_json(run_dir, "architecture_v1.json"))
    lts_path = _find_json(run_dir, "learning_targets_v1.json")
    if lts_path is None:
        raise FileNotFoundError(
            f"no learning_targets_v1.json in {run_dir} — gate cannot run"
        )
    lts_doc = _load_json(lts_path) or {}
    lts = lts_doc.get("learning_targets") or []

    bullets_path = _find_json(run_dir, "source_bullets_v1.json")
    bullets_doc = _load_json(bullets_path) if bullets_path else None

    corpus_mode = "proxy"
    corpus_warning = ""
    illustrative: list[SourceItem] = []
    excluded: list[SourceItem] = []
    errors: list[SourceItem] = []
    counts: dict[str, int] = {}

    if bullets_doc is not None:
        coverage, illustrative, excluded, errors, counts = _build_bullet_buckets(
            bullets_doc
        )
        if coverage or illustrative or excluded or errors:
            source_corpus = coverage
            corpus_mode = "bullets"
            warnings: list[str] = []
            if not coverage:
                warnings.append(
                    "source_bullets artefact has no coverage-relevant bullets "
                    "(specific_expectation + overall_expectation = 0); "
                    "coverage denominator is empty — gate output is a "
                    "diagnostic signal, not a quality measurement."
                )
            if len(excluded) > _EXCLUDED_REVIEW_THRESHOLD:
                warnings.append(
                    f"excluded bucket has {len(excluded)} bullets "
                    f"(front_matter + other), above review threshold "
                    f"{_EXCLUDED_REVIEW_THRESHOLD} — Phase 1 scoping may be "
                    "letting in non-content."
                )
            if errors:
                warnings.append(
                    f"extraction-error bucket has {len(errors)} cross-grade "
                    "bullet(s); Phase 1 scoping captured content outside "
                    "the target grade."
                )
            corpus_warning = " | ".join(warnings)
        else:
            source_corpus = _build_source_corpus(profile, architecture)
            corpus_warning = (
                f"source_bullets artefact at {bullets_path} is empty; "
                "falling back to proxy corpus — baseline unreliable."
            )
    else:
        source_corpus = _build_source_corpus(profile, architecture)
        corpus_warning = (
            "no source_bullets_v1.json artefact in run dir; "
            "running on proxy corpus — baseline unreliable."
        )

    return RunArtefacts(
        run_dir=run_dir,
        curriculum_profile=profile,
        architecture=architecture,
        learning_targets=lts,
        source_corpus=source_corpus,
        corpus_mode=corpus_mode,
        corpus_warning=corpus_warning,
        illustrative_bullets=illustrative,
        excluded_bullets=excluded,
        extraction_error_bullets=errors,
        bullet_type_counts=counts,
    )


__all__ = ["RunArtefacts", "SourceItem", "load_run"]
