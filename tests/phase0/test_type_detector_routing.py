"""Type-detector routing tests (Session 4a-2b Step 9).

Live-PDF tests against the fixtures already under outputs/. Pins the
routing so future changes to the heuristic can't silently re-route a
known good artefact.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from curriculum_harness.phases.phase0_acquisition.type_detector import (
    detect_source_type,
)


ROOT = Path(__file__).resolve().parents[2]

ONTARIO_PDF = (
    ROOT / "outputs" / "phase0-test-ontario-g7-history-2026-04-18" / "_source.pdf"
)
AP_CED_PDF = (
    ROOT / "outputs" / "phase0-test-ap-usgov-unit1-requeued-2026-04-18" / "_source.pdf"
)


def test_ontario_routes_to_multi_section_pdf() -> None:
    if not ONTARIO_PDF.exists():
        pytest.skip(f"Ontario fixture not present at {ONTARIO_PDF}")
    d = detect_source_type(str(ONTARIO_PDF))
    assert d.source_type == "multi_section_pdf"
    assert d.confidence == "high"
    assert d.signals.get("outline_top_level_entries", 0) >= 2
    assert d.signals.get("n_pages", 0) >= 50


def test_ap_ced_stays_flat_pdf_linear() -> None:
    if not AP_CED_PDF.exists():
        pytest.skip(f"AP CED fixture not present at {AP_CED_PDF}")
    d = detect_source_type(str(AP_CED_PDF))
    assert d.source_type == "flat_pdf_linear", (
        "AP CED has a thin embedded outline (one top-level entry) and "
        "few TOC dot-leader lines — must stay flat under the 4a-2b "
        "heuristic, because its existing scoped-page-range pipeline "
        "produces the known-good artefact"
    )
