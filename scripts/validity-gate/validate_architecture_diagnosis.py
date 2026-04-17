#!/usr/bin/env python3
"""Foundation moment 1 — architecture diagnosis verifiable from source.

Assertion: the Phase 2 architecture diagnosis (strand labels, level
model, scoping strategy, any ArchitectureStrand entries) is
justifiable by pointing at passages of the source document.

Status: pending.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_architecture_diagnosis.py",
        status="pending",
        foundation_moment=1,
        assertion=(
            "architecture diagnosis is verifiable from the source"
        ),
        reads=(
            "outputs/<run>/<runId>_architecture_v1.json, "
            "..._curriculum_profile_v1.json, and the source text cached "
            "by Phase 1"
        ),
        notes=(
            "likely a two-tier check: (1) every strand label appears "
            "verbatim or near-verbatim in the source; (2) the level_model "
            "and scoping_strategy match structural cues in the source "
            "(multi-level headings => multi_level_progression, etc). "
            "Second tier may need a rubric rather than a hard assertion."
        ),
    )


if __name__ == "__main__":
    main()
