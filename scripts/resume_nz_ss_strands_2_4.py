"""Resume NZ Social Sciences run from session 4c-3b.

History strand is complete in OUT_DIR/per_strand/history/. This script runs
only Civics and Society, Geography, and Economic Activity, then re-stitches
all four strands into a unified corpus.

Usage:
    python scripts/resume_nz_ss_strands_2_4.py
"""
from __future__ import annotations

import json
import os
import sys

SNAPSHOT = "docs/run-snapshots/2026-04-18-session-4a-3-nz-curriculum"
OUT_DIR = "/tmp/nz-social-sciences-4c3b"
DOMAIN = "horizontal"

STRANDS_TO_RUN = ["civics-and-society", "geography", "economic-activity"]

BASE_ARGS = {
    "model": "claude-sonnet-4-20250514",
    "runs": None,
    "temperature": None,
    "cluster_model": None,
    "domain": DOMAIN,
    "dispositional": False,
    "skip_criteria": False,
    "skip_lts": False,
}


def main() -> int:
    from curriculum_harness.reference_authoring.strand.detect_strands import detect_strands
    from curriculum_harness.reference_authoring.strand.orchestrate import (
        create_strand_snapshot,
        run_strand_sub_run,
        _strand_slug,
    )
    from curriculum_harness.reference_authoring.strand.stitch import stitch_corpora
    import tempfile

    with open(os.path.join(SNAPSHOT, "content.txt"), encoding="utf-8") as fh:
        raw = fh.read()

    strand_result = detect_strands(raw)
    if not strand_result.is_multi_strand:
        print("ERROR: source detected as single-strand; expected multi-strand", file=sys.stderr)
        return 1

    all_lines = raw.splitlines()
    per_strand_out_root = os.path.join(OUT_DIR, "per_strand")
    tmp_snapshot_root = tempfile.mkdtemp(prefix="strand_snapshots_resume_")

    per_strand_dirs: dict[str, str] = {}
    ledger_by_strand: dict[str, dict] = {}
    failed_strands: list[str] = []

    for strand in strand_result.strands:
        slug = _strand_slug(strand.name)
        strand_out_dir = os.path.join(per_strand_out_root, slug)

        if slug not in STRANDS_TO_RUN:
            # Use existing output from prior run
            print(f"[resume] strand '{strand.name}' — reusing existing output at {strand_out_dir}")
            per_strand_dirs[slug] = strand_out_dir
            # Load ledger from existing quality_report.json
            qr_path = os.path.join(strand_out_dir, "quality_report.json")
            try:
                with open(qr_path) as fh:
                    qr = json.load(fh)
                ledger_by_strand[slug] = qr.get("token_usage", {})
            except FileNotFoundError:
                ledger_by_strand[slug] = {}
            continue

        print(
            f"[resume] strand '{strand.name}' (slug={slug}, "
            f"lines {strand.line_start}–{strand.line_end}) — running sub-run...",
            flush=True,
        )

        strand_snapshot_dir = create_strand_snapshot(
            original_snapshot_path=SNAPSHOT,
            strand=strand,
            all_lines=all_lines,
            strand_slug=slug,
            parent_dir=tmp_snapshot_root,
        )

        os.makedirs(strand_out_dir, exist_ok=True)
        exit_code, strand_ledger = run_strand_sub_run(
            strand_snapshot_dir=strand_snapshot_dir,
            strand_output_dir=strand_out_dir,
            base_args=BASE_ARGS,
        )

        per_strand_dirs[slug] = strand_out_dir
        ledger_by_strand[slug] = strand_ledger

        if exit_code != 0:
            print(f"[resume] WARNING: strand '{strand.name}' exited {exit_code}", flush=True)
            failed_strands.append(slug)
        else:
            in_t = strand_ledger.get("total_input_tokens", 0)
            out_t = strand_ledger.get("total_output_tokens", 0)
            cost = (in_t * 3 + out_t * 15) / 1_000_000
            print(
                f"[resume] strand '{strand.name}' complete. "
                f"tokens={in_t}in+{out_t}out  cost=${cost:.4f}",
                flush=True,
            )

    strand_slugs = [_strand_slug(s.name) for s in strand_result.strands]
    strand_names = {_strand_slug(s.name): s.name for s in strand_result.strands}

    print("[resume] stitching all 4 strand corpora...", flush=True)
    stitch_ok, stitch_failures = stitch_corpora(
        per_strand_dirs=per_strand_dirs,
        unified_out_dir=OUT_DIR,
        strand_result=strand_result,
        strand_slugs=strand_slugs,
        strand_names=strand_names,
        ledger_by_strand=ledger_by_strand,
    )

    if stitch_failures:
        print("[resume] SANITY CHECK FAILURES:", flush=True)
        for f in stitch_failures:
            print(f"  {f}", flush=True)
        return 2

    print("[resume] all sanity checks passed.", flush=True)

    if failed_strands:
        print(f"[resume] WARNING: {len(failed_strands)} strand(s) failed: {failed_strands}", flush=True)
        return 2

    print("[resume] NZ Social Sciences resume complete.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
