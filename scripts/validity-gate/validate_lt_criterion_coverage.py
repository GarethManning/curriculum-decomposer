#!/usr/bin/env python3
"""Foundation moment 4 — LT decomposes to >=1 criterion.

Assertion: every learning target decomposes to at least one criterion
in the criterion bank.

Status: deferred. The criterion-bank phase does not yet exist in the
pipeline. Do not implement this gate until that phase lands. When it
does, promote this script to `pending`, update the status table in
`README.md`, and update foundation moment 4 in `VALIDITY.md`.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_lt_criterion_coverage.py",
        status="deferred",
        foundation_moment=4,
        assertion=(
            "every LT decomposes to >=1 criterion in the bank"
        ),
        reads=(
            "outputs/<run>/<runId>_learning_targets_v1.json and a future "
            "..._criteria_v1.json (path TBD when criterion-bank phase "
            "is designed)"
        ),
        notes=(
            "blocked on criterion-bank phase. Do not implement speculative "
            "schema — wait for the phase to land."
        ),
    )


if __name__ == "__main__":
    main()
