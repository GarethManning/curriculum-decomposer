"""Helpers for validity-gate scripts that read a curriculum-decomposer
run directory.

A "run directory" is `outputs/<run>/` and contains some subset of:
  - `<runId>_curriculum_profile_v1.json` or `curriculum_profile_v1.json`
  - `<runId>_architecture_v1.json`          or `architecture_v1.json`
  - `<runId>_kud_v1.json`                   or `kud_v1.json`
  - `<runId>_learning_targets_v1.json`      or `learning_targets_v1.json`

This module hides the runId-prefixed-vs-plain naming convention and
builds a best-available English source-proxy corpus for matching. The
raw source text lives in a LangGraph checkpoint DB and may be
non-English (e.g. Hungarian for the felvételi run); the matcher is
English-only, so the proxy is the pipeline's English rendering of the
source: `curriculum_profile.rationale`, strand labels, values_basis,
and the hierarchical/horizontal/dispositional element lists.

### What this proxy does NOT give you

- **True source fidelity.** If the pipeline's Phase 1 already dropped
  a strand, the proxy has no memory of it. Coverage against the proxy
  is coverage against the pipeline's own reading, not against the
  original document.
- **Bullet-level granularity.** The proxy items are strand-level, not
  per-bullet. Orphan detection is coarser than the gate's ultimate
  intent; a proxy item "covers" any LT that shares strand vocabulary.

Upgrade path: once a per-run `_source_bullets_v1.json` artefact is
written by the harness (not yet implemented), `load_source_corpus`
should prefer that file and only fall back to the proxy when absent.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SourceItem:
    """One item in the source-proxy corpus.

    `provenance` — where this item came from in the run dir, so reports
    can cite it. Examples: "architecture.strands[2].label",
    "curriculum_profile.rationale".
    """

    text: str
    provenance: str


@dataclass
class RunArtefacts:
    run_dir: Path
    curriculum_profile: dict | None
    architecture: dict | None
    learning_targets: list[dict]
    source_corpus: list[SourceItem]


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


def load_run(run_dir: str | Path) -> RunArtefacts:
    """Load a run's Phase 1/2/4 JSON and build the source-proxy corpus.

    Raises FileNotFoundError if `learning_targets` JSON is missing —
    gates cannot run without it. A missing profile or architecture is
    tolerated; the source-proxy corpus will be smaller.
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

    source_corpus = _build_source_corpus(profile, architecture)

    return RunArtefacts(
        run_dir=run_dir,
        curriculum_profile=profile,
        architecture=architecture,
        learning_targets=lts,
        source_corpus=source_corpus,
    )


__all__ = ["RunArtefacts", "SourceItem", "load_run"]
