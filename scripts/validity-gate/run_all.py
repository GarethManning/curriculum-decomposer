#!/usr/bin/env python3
"""Validity-gate orchestrator.

Runs each `validate_*.py` script in this directory against a run's
output directory, collects exit codes, and prints a status table.

Exit codes from child scripts:
  0 — PASS
  1 — FAIL
  2 — NOT_IMPLEMENTED (stub — pending or deferred)

This scaffold always exits 0: at present every script is a stub. When
scripts are promoted to real checks, change the final exit logic to
return non-zero on any FAIL.

Usage:
    python scripts/validity-gate/run_all.py outputs/<run>/
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GATE_SCRIPTS = sorted(
    p.name
    for p in SCRIPT_DIR.glob("validate_*.py")
)


def main(run_path: str) -> int:
    results: list[tuple[str, int]] = []
    for script in GATE_SCRIPTS:
        proc = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / script), run_path],
            capture_output=True,
            text=True,
        )
        if proc.stdout:
            print(proc.stdout.rstrip())
        if proc.stderr:
            print(proc.stderr.rstrip(), file=sys.stderr)
        results.append((script, proc.returncode))

    print()
    print("=" * 72)
    print(f"Validity gate summary — run: {run_path}")
    print("=" * 72)
    passed = sum(1 for _, rc in results if rc == 0)
    failed = sum(1 for _, rc in results if rc == 1)
    stubbed = sum(1 for _, rc in results if rc == 2)
    other = sum(1 for _, rc in results if rc not in (0, 1, 2))
    for script, rc in results:
        label = {0: "PASS", 1: "FAIL", 2: "NOT_IMPL"}.get(rc, f"rc={rc}")
        print(f"  [{label:>8}] {script}")
    print()
    print(
        f"  {passed} pass, {failed} fail, {stubbed} not-implemented"
        + (f", {other} other" if other else "")
    )

    if failed > 0:
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "usage: python scripts/validity-gate/run_all.py <run_output_dir>",
            file=sys.stderr,
        )
        sys.exit(64)
    sys.exit(main(sys.argv[1]))
