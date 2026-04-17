"""Shared stub helpers for validity-gate scripts.

Every gate script in this directory is currently a stub. Each script
calls `not_implemented(...)` with its assertion text and status, which
prints a stable one-line banner and exits 2 (NOT_IMPLEMENTED). The
runner (`run_all.py`) distinguishes exit codes:

  0 — PASS
  1 — FAIL
  2 — NOT_IMPLEMENTED (stub, counted as pending or deferred)

Promoting a stub to a real check: replace its `main()` body with the
check logic and remove the `not_implemented(...)` call. See
`README.md` for the full promotion recipe.
"""

from __future__ import annotations

import sys
from typing import Literal

Status = Literal["pending", "deferred"]


def not_implemented(
    *,
    script: str,
    status: Status,
    foundation_moment: int,
    assertion: str,
    reads: str,
    notes: str = "",
) -> None:
    """Print a stable banner and exit 2."""
    lines = [
        f"[NOT_IMPLEMENTED] {script}",
        f"  status             : {status}",
        f"  foundation moment  : {foundation_moment}",
        f"  assertion          : {assertion}",
        f"  would read         : {reads}",
    ]
    if notes:
        lines.append(f"  notes              : {notes}")
    print("\n".join(lines))
    sys.exit(2)
