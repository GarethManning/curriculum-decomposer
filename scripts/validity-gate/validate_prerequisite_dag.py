#!/usr/bin/env python3
"""Foundation moment 4 — prerequisite edges form a DAG.

Assertion: the prerequisite edges between criteria form a directed
acyclic graph (no cycles, topological sort exists).

Status: deferred. Blocked on the same criterion-bank phase as
`validate_lt_criterion_coverage.py`. Promote to `pending` when that
phase lands.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_prerequisite_dag.py",
        status="deferred",
        foundation_moment=4,
        assertion=(
            "prerequisite edges between criteria form a DAG"
        ),
        reads=(
            "future outputs/<run>/<runId>_criteria_v1.json (or equivalent) "
            "— the edge set containing prerequisite relations"
        ),
        notes=(
            "blocked on criterion-bank phase. Implementation is a "
            "topological-sort or Tarjan SCC check over the edge set. "
            "Deferred, not pending — do not sketch the schema now."
        ),
    )


if __name__ == "__main__":
    main()
