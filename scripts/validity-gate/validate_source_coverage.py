#!/usr/bin/env python3
"""Foundation moment 1 — source → LT coverage.

Assertion: every load-bearing content element present in the source
(as represented in Phase 1 `curriculum_profile` and Phase 2
`architecture` outputs) traces to at least one learning target in
`..._learning_targets_v1.json`.

Status: pending. The artefacts needed (source text, Phase 1 JSON,
Phase 2 JSON, learning-targets JSON) already land in
`outputs/<run>/`, so this is implementable without new pipeline work.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_source_coverage.py",
        status="pending",
        foundation_moment=1,
        assertion=(
            "every source content element traces to >=1 LT in the output"
        ),
        reads=(
            "outputs/<run>/<runId>_curriculum_profile_v1.json, "
            "..._architecture_v1.json, ..._learning_targets_v1.json, "
            "and the source text cached by Phase 1"
        ),
        notes=(
            "requires a stable notion of 'content element' — likely a "
            "union of Phase 2 strand items and any Phase 1 extracted "
            "topic/competency list. Define that before writing the check."
        ),
    )


if __name__ == "__main__":
    main()
