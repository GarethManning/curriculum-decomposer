#!/usr/bin/env python3
"""Foundation moment 1 — no fabrication.

Assertion: no learning target introduces content (concept, skill,
assessment move, disciplinary convention) that the source does not
support.

Status: pending. Counterpart to `validate_source_coverage.py`.
Coverage catches drops; faithfulness catches additions.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_source_faithfulness.py",
        status="pending",
        foundation_moment=1,
        assertion=(
            "no LT introduces content not supported by the source"
        ),
        reads=(
            "outputs/<run>/<runId>_learning_targets_v1.json plus the "
            "source text cached by Phase 1"
        ),
        notes=(
            "hardest of the moment-1 gates — requires a retrieval or "
            "embedding check against source text, or a structured "
            "allow-list of source-derived concepts to match LTs against. "
            "Start with the lighter allow-list check; upgrade later."
        ),
    )


if __name__ == "__main__":
    main()
