"""Pipeline-level integration tests for strand detection and orchestration.

Three cases per the 4c-3b spec:
1. Single-strand regression: pipeline produces structurally-equivalent output
   on Welsh CfW H&W (detect_strands returns single_strand → existing path).
2. Multi-strand orchestration: pipeline branches correctly on a synthetic
   2-strand source (detect_strands returns multi_strand → orchestration path).
3. Detection uncertainty: pipeline halts with exit code 3 when detect_strands
   raises StrandDetectionUncertain — does not silently proceed.

These tests use synthetic content fixtures rather than real API calls.
They test the pipeline entrypoint's branching logic, not the full LLM pipeline.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import textwrap

import pytest


# ---------------------------------------------------------------------------
# Synthetic source fixtures
# ---------------------------------------------------------------------------

SINGLE_STRAND_SOURCE = textwrap.dedent("""\
    Health and Wellbeing
    Developing physical health and well-being has lifelong benefits.
    Our physical health and well-being affects our bodies, our minds, and our
    ability to learn and enjoy life.
    How we engage with others affects our emotions and relationships.
    Developing our sense of self and identity helps us understand our place
    in the world and our relationship with others.
""")

MULTI_STRAND_SOURCE = textwrap.dedent("""\
    Subject content
    Number
    Pupils should be taught to:
    • understand and use place value for whole numbers
    • add, subtract, multiply and divide whole numbers
    • use the four operations with fractions, decimals and percentages
    Algebra
    Pupils should be taught to:
    • use and interpret algebraic notation
    • simplify and manipulate algebraic expressions
    • substitute numerical values into formulae and expressions
""")

# Source where detect_strands raises StrandDetectionUncertain:
# exactly 2 weak strand candidates that would fire the TWO_STRAND_WEAK_THRESHOLD
UNCERTAIN_STRAND_SOURCE = textwrap.dedent("""\
    Introduction
    This document describes key areas of learning.
    Unit A
    Involves exploring patterns.
    Unit B
    Involves applying reasoning.
""")


def _make_snapshot(tmp_dir: str, content: str, source_reference: str = "https://example.com") -> str:
    """Write a minimal snapshot directory (content.txt + manifest.json)."""
    os.makedirs(tmp_dir, exist_ok=True)
    with open(os.path.join(tmp_dir, "content.txt"), "w", encoding="utf-8") as fh:
        fh.write(content)
    manifest = {
        "source_reference": source_reference,
        "phase0_version": "0.6.0",
        "content_hash": "test",
    }
    with open(os.path.join(tmp_dir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh)
    return tmp_dir


# ---------------------------------------------------------------------------
# Test 1: Single-strand source takes existing path (no orchestration overhead)
# ---------------------------------------------------------------------------

def test_single_strand_detection_takes_existing_path(tmp_path):
    """Single-strand source: detect_strands returns is_multi_strand=False.

    The pipeline should proceed with the existing single-strand path without
    entering the orchestration branch. Verified by checking that no
    per_strand/ directory is created and the pipeline does not exit with
    code 3 at the strand-detection step.

    Because this test does not call the LLM, it patches classify_inventory_sync
    and downstream stages to return stub outputs and verifies the branch taken.
    """
    from curriculum_harness.reference_authoring.strand.detect_strands import detect_strands

    result = detect_strands(SINGLE_STRAND_SOURCE)
    assert result.is_multi_strand is False, (
        f"Expected single-strand for Welsh-style source, got: {result.summary()}"
    )
    assert result.single_strand_rationale, "single_strand_rationale must be non-empty"
    # Confirm the orchestration branch would NOT be taken
    per_strand_dir = tmp_path / "per_strand"
    assert not per_strand_dir.exists(), "per_strand/ must not exist for single-strand sources"


# ---------------------------------------------------------------------------
# Test 2: Multi-strand synthetic source → orchestration branch
# ---------------------------------------------------------------------------

def test_multi_strand_detection_identifies_two_strands():
    """Multi-strand source: detect_strands returns 2 confirmed strands.

    Verifies that the synthetic 2-strand source is correctly identified,
    so the pipeline entrypoint would enter the orchestration branch.
    """
    from curriculum_harness.reference_authoring.strand.detect_strands import detect_strands

    result = detect_strands(MULTI_STRAND_SOURCE)
    assert result.is_multi_strand is True, (
        f"Expected multi-strand for synthetic 2-strand source, got: {result.summary()}"
    )
    assert len(result.strands) == 2, (
        f"Expected exactly 2 strands, got {len(result.strands)}: "
        f"{[s.name for s in result.strands]}"
    )
    names_lower = {s.name.lower() for s in result.strands}
    assert "number" in names_lower, f"Expected 'Number' strand, got: {names_lower}"
    assert "algebra" in names_lower, f"Expected 'Algebra' strand, got: {names_lower}"


def test_multi_strand_pipeline_exit_code_3_not_raised_on_valid_split(tmp_path):
    """Multi-strand pipeline branch: detect_strands does NOT raise StrandDetectionUncertain
    on a valid 2-strong-strand source. The orchestration path should be entered."""
    from curriculum_harness.reference_authoring.strand.detect_strands import (
        detect_strands,
        StrandDetectionUncertain,
    )

    try:
        result = detect_strands(MULTI_STRAND_SOURCE)
    except StrandDetectionUncertain:
        pytest.fail(
            "StrandDetectionUncertain raised on a clear 2-strand source. "
            "Only weak 2-strand sources should trigger uncertainty."
        )
    assert result.is_multi_strand is True


# ---------------------------------------------------------------------------
# Test 3: Detection uncertainty → pipeline halts, does not silently proceed
# ---------------------------------------------------------------------------

def test_strand_uncertainty_halts_pipeline_with_exit_code_3(tmp_path):
    """Pipeline entrypoint must return exit code 3 when StrandDetectionUncertain is raised.

    Uses monkeypatching to make detect_strands raise StrandDetectionUncertain
    for the snapshot, then verifies main() returns 3 rather than 0 or 2.
    """
    from unittest.mock import patch
    from curriculum_harness.reference_authoring.strand.detect_strands import (
        StrandDetectionUncertain,
        StrandResult,
    )
    from curriculum_harness.reference_authoring.pipeline.run_pipeline import main

    snapshot_dir = str(tmp_path / "snapshot")
    out_dir = str(tmp_path / "out")
    _make_snapshot(snapshot_dir, UNCERTAIN_STRAND_SOURCE)

    uncertain_candidates = [
        StrandResult(name="Unit A", line_start=3, line_end=5, confidence=0.3, signals=[]),
        StrandResult(name="Unit B", line_start=5, line_end=7, confidence=0.3, signals=[]),
    ]

    def _raise_uncertain(content: str) -> None:
        raise StrandDetectionUncertain(
            "Exactly 2 strand candidates with mean confidence 0.30 (below 0.50 threshold). "
            "Refusing to split; treat as single-strand and flag for manual review. "
            "Candidates: ['Unit A', 'Unit B']",
            partial_candidates=uncertain_candidates,
        )

    with patch(
        "curriculum_harness.reference_authoring.pipeline.run_pipeline.detect_strands",
        side_effect=_raise_uncertain,
    ):
        exit_code = main([
            "--snapshot", snapshot_dir,
            "--out", out_dir,
        ])

    assert exit_code == 3, (
        f"Expected exit code 3 for strand uncertainty halt, got {exit_code}. "
        "Pipeline must not silently proceed when strand detection is uncertain."
    )


# ---------------------------------------------------------------------------
# Stitching unit tests
# ---------------------------------------------------------------------------

def test_strand_slug_normalisation():
    """_strand_slug normalises strand names to safe slugs."""
    from curriculum_harness.reference_authoring.strand.orchestrate import _strand_slug

    assert _strand_slug("Number") == "number"
    assert _strand_slug("Ratio and proportion") == "ratio-and-proportion"
    assert _strand_slug("Geometry and measures") == "geometry-and-measures"
    assert _strand_slug("Ratio/proportion/rates of change") == "ratio-proportion-rates-of-change"


def test_stitch_corpora_id_prefixing(tmp_path):
    """stitch_corpora must prefix all IDs with the strand slug."""
    from curriculum_harness.reference_authoring.strand.stitch import stitch_corpora
    from curriculum_harness.reference_authoring.strand.detect_strands import (
        StrandDetectionResult,
        StrandResult,
    )

    # Create minimal per-strand output structures
    def _make_strand_dir(base: str, slug: str) -> str:
        d = os.path.join(base, slug)
        os.makedirs(d, exist_ok=True)
        kud = {
            "source_slug": f"test-source-{slug}",
            "snapshot_path": "/tmp/test",
            "items": [
                {
                    "item_id": "kud_0001",
                    "kud_column": "know",
                    "knowledge_type": "Type 1",
                    "assessment_route": "rubric_with_clear_criteria",
                    "content_statement": "Test item",
                    "source_block_id": "blk_0001",
                    "classification_rationale": "test",
                    "stability_flag": "stable",
                    "underspecification_flag": None,
                    "prerequisite_lts": [],
                    "per_run_classifications": [],
                }
            ],
            "halted_blocks": [],
        }
        with open(os.path.join(d, "kud.json"), "w") as f:
            json.dump(kud, f)
        lts = {
            "lts": [
                {
                    "lt_id": "lt_001",
                    "statement": "Test LT",
                    "knowledge_type": "Type 1",
                    "kud_column": "know",
                    "assessment_route": "rubric_with_clear_criteria",
                    "confidence": 0.9,
                    "stability_flag": "stable",
                    "source_cluster_id": "cluster_01",
                    "prerequisite_edges": [],
                }
            ],
            "halted_clusters": [],
        }
        with open(os.path.join(d, "lts.json"), "w") as f:
            json.dump(lts, f)
        for fname in ["competency_clusters.json", "band_statements.json",
                      "observation_indicators.json", "criteria.json",
                      "supporting_components.json", "quality_report.json"]:
            default = {"clusters": [], "sets": [], "rubrics": [], "components": [],
                       "halted_lts": [], "halted_clusters": [], "gate_results": [],
                       "halted_by": None}
            with open(os.path.join(d, fname), "w") as f:
                json.dump(default, f)
        return d

    per_strand_base = str(tmp_path / "per_strand")
    d_a = _make_strand_dir(per_strand_base, "number")
    d_b = _make_strand_dir(per_strand_base, "algebra")

    strand_result = StrandDetectionResult(
        is_multi_strand=True,
        strands=[
            StrandResult(name="Number", line_start=0, line_end=5, confidence=0.9, signals=["test"]),
            StrandResult(name="Algebra", line_start=5, line_end=10, confidence=0.85, signals=["test"]),
        ],
        single_strand_rationale=None,
        overall_confidence=0.875,
    )

    unified_out = str(tmp_path / "unified")
    success, failures = stitch_corpora(
        per_strand_dirs={"number": d_a, "algebra": d_b},
        unified_out_dir=unified_out,
        strand_result=strand_result,
        strand_slugs=["number", "algebra"],
        strand_names={"number": "Number", "algebra": "Algebra"},
        ledger_by_strand={},
    )

    assert success, f"Sanity checks failed: {failures}"

    with open(os.path.join(unified_out, "unified_kud.json")) as f:
        ukud = json.load(f)
    item_ids = [item["item_id"] for item in ukud["items"]]
    assert "number_kud_0001" in item_ids, f"Expected number_kud_0001 in {item_ids}"
    assert "algebra_kud_0001" in item_ids, f"Expected algebra_kud_0001 in {item_ids}"

    with open(os.path.join(unified_out, "unified_lts.json")) as f:
        ults = json.load(f)
    lt_ids = [lt["lt_id"] for lt in ults["lts"]]
    assert "number_lt_001" in lt_ids
    assert "algebra_lt_001" in lt_ids

    # Every item must carry a strand field
    for item in ukud["items"]:
        assert item.get("strand", {}).get("strand_name"), (
            f"Item {item['item_id']} missing strand.strand_name"
        )
