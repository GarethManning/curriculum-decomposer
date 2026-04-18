"""Tests for the ``detect_toc`` primitive.

Live-PDF tests against the Ontario K-8 Social Studies / History /
Geography PDF (downloaded in Session 4a-2b Step 3). Structural
assertions only — no semantic judgement about which titles exist, just
that the detection tiers work and return well-formed entries.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
)
from curriculum_harness.phases.phase0_acquisition.primitives.detect_toc import (
    DetectTocPrimitive,
)


ONTARIO_PDF = (
    Path(__file__).resolve().parents[2]
    / "outputs"
    / "phase0-test-ontario-g7-history-2026-04-18"
    / "_source.pdf"
)


class _Scope:
    source_reference = "test"


@pytest.fixture(scope="module")
def ontario_pdf_bytes() -> bytes:
    if not ONTARIO_PDF.exists():
        pytest.skip(f"Ontario fixture not present at {ONTARIO_PDF}")
    return ONTARIO_PDF.read_bytes()


def test_detect_toc_embedded_outline_on_ontario(ontario_pdf_bytes) -> None:
    prim = DetectTocPrimitive()
    result = prim.run(_Scope(), PrimitiveResult(output=ontario_pdf_bytes))
    toc = result.meta["toc"]

    assert toc["detection_method"] == "embedded_outline"
    assert len(toc["entries"]) >= 10

    titles = [e["title"] for e in toc["entries"]]
    assert any("Grade 7" in t and "History" in t for t in titles)
    assert any("Grade 8" in t and "History" in t for t in titles)

    for e in toc["entries"]:
        assert isinstance(e["page_number"], int) and e["page_number"] >= 1
        assert isinstance(e["depth"], int) and e["depth"] >= 0
        assert e["source"] == "embedded_outline"


def test_detect_toc_reports_struct_tree_on_aoda_pdf(ontario_pdf_bytes) -> None:
    # Ontario is AODA-tagged; the /StructTreeRoot probe must fire
    # regardless of whether the primitive actually consumes it.
    prim = DetectTocPrimitive()
    result = prim.run(_Scope(), PrimitiveResult(output=ontario_pdf_bytes))
    assert result.meta["toc"]["struct_tree_present"] is True


def test_detect_toc_grade_7_history_page_number_matches_ground_truth(
    ontario_pdf_bytes,
) -> None:
    # Step 3 manually determined G7 History starts at 1-indexed page 245.
    # The primitive's automated resolution must agree.
    prim = DetectTocPrimitive()
    result = prim.run(_Scope(), PrimitiveResult(output=ontario_pdf_bytes))
    match = [
        e for e in result.meta["toc"]["entries"]
        if e["title"].strip() == "History, Grade 7"
    ]
    assert len(match) == 1, (
        f"expected exactly one 'History, Grade 7' outline entry, got {len(match)}"
    )
    assert match[0]["page_number"] == 245


def test_detect_toc_handles_empty_input() -> None:
    # Primitive must return structured "none" rather than crashing on
    # non-PDF bytes.
    prim = DetectTocPrimitive()
    result = prim.run(_Scope(), PrimitiveResult(output=b"not a pdf"))
    toc = result.meta["toc"]
    assert toc["detection_method"] == "none"
    assert toc["entries"] == []
    assert "detection_reason" in toc
