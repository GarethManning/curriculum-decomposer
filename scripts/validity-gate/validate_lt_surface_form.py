#!/usr/bin/env python3
"""Foundation moment 2 — learning-target surface form.

Assertion: every emitted learning target satisfies the surface-form
contract in `ltConstraints` — max word count, single-construct only,
no embedded examples, stem matching the active `lt_statement_format`
(resolved via `resolve_lt_statement_format`).

Status: pending.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_lt_surface_form.py",
        status="pending",
        foundation_moment=2,
        assertion=(
            "all LTs pass surface-form validation (word count, format, "
            "compound-check)"
        ),
        reads=(
            "outputs/<run>/<runId>_learning_targets_v1.json plus the run "
            "config's ltConstraints and curriculumProfile"
        ),
        notes=(
            "the surface-form rules already live in curriculum_harness/phases/"
            "phase4_lt_generation.py and phase5_formatting.py — lift them "
            "into a shared validator both Phase 4 and this gate can call. "
            "Compound-check should go beyond naive 'and'-splitting "
            "(handle 'analyse and evaluate' style verb pairs that "
            "genuinely name two constructs)."
        ),
    )


if __name__ == "__main__":
    main()
