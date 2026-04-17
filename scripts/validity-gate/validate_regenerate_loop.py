#!/usr/bin/env python3
"""Foundation moment 2 — regenerate loop ran on initial failure.

Assertion: if any learning target initially failed surface-form
validation during Phase 4, the regenerate loop ran and the final LT
set passes surface-form.

Status: pending — and the underlying regenerate-on-failure loop is a
known gap. The gate cannot pass until the loop is guaranteed to run
in Phase 4. Until then, this script exists to make the gap visible.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_regenerate_loop.py",
        status="pending",
        foundation_moment=2,
        assertion=(
            "LT regeneration has run if any LT initially failed surface "
            "validation"
        ),
        reads=(
            "outputs/<run>/<runId>_learning_targets_v1.json, "
            "..._run_report_v1.md, and whatever Phase 4 emits to record "
            "regeneration events (not yet designed)"
        ),
        notes=(
            "KNOWN GAP — Phase 4 does not yet emit a regeneration-event "
            "log, and regeneration-on-failure is not guaranteed to run. "
            "Implementing this gate requires (1) Phase 4 to record "
            "initial failures and regeneration attempts in the run "
            "report, and (2) this script to read that record and "
            "re-validate the final LT set. Track as a pipeline dev item."
        ),
    )


if __name__ == "__main__":
    main()
