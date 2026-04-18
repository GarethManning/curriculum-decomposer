"""Session 4a-3 Step 8 regression — replay each prior Phase 0 extraction
in-place under the updated schema (0.4.0 + dom_hash field) and assert
the content hash is byte-identical to the stored value.

A drift in hash is a regression to investigate, not a blank re-accept.
The updated schema added the dom_hash field (null for non-JS types) but
did not alter any extraction primitive, so hashes must hold.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from curriculum_harness.phases.phase0_acquisition.acquire import acquire
from curriculum_harness.phases.phase0_acquisition.manifest import ScopeSpec


CASES = [
    {
        "label": "Common Core 7.RP",
        "expected_hash": (
            "c48297f2cd0daecc97afc2a861deb036"
            "940f1799919b90e3ed3b7a60ec0162d3"
        ),
        "out_dir": Path("outputs/_regression_4a3/common-core-7rp"),
        "scope": ScopeSpec(
            source_reference="https://www.thecorestandards.org/Math/Content/7/RP/",
            url="https://www.thecorestandards.org/Math/Content/7/RP/",
            css_selector="article section.content",
            notes="Regression replay Session 4a-3 Step 8.",
        ),
    },
    {
        "label": "DfE KS3 Maths",
        "expected_hash": (
            "260154d50a6016f499e866d6e6e71c4f"
            "90dae7ac1c8f7800eeb552fa8336bafa"
        ),
        "out_dir": Path("outputs/_regression_4a3/dfe-ks3"),
        "scope": ScopeSpec(
            source_reference=(
                "https://assets.publishing.service.gov.uk/media/"
                "5a7c1408e5274a1f5cc75a68/SECONDARY_national_curriculum_"
                "-_Mathematics.pdf"
            ),
            notes="Regression replay Session 4a-3 Step 8.",
        ),
    },
    {
        "label": "AP US Gov CED, Unit 1 (requeued)",
        "expected_hash": (
            "e6eea33806b8ab5ef1b17955d3417032"
            "ec549e602262c45f48d20b40c06f396d"
        ),
        "out_dir": Path("outputs/_regression_4a3/ap-usgov-requeued"),
        "scope": ScopeSpec(
            source_reference=(
                "/Users/garethmanning/Github/curriculum-harness/outputs/"
                "phase0-test-ap-usgov-unit1-requeued-2026-04-18/_source.pdf"
            ),
            page_range=[40, 55],
            section_heading="Foundations of American Democracy",
            pdf_dedup_coords=True,
            pdf_dedup_coord_tolerance=1,
            notes="Regression replay Session 4a-3 Step 8.",
        ),
    },
    {
        "label": "Ontario K-8 Grade 7 History (PDF)",
        "expected_hash": (
            "bc7ef9d3b36f9da9a7ffa3182e50aa79"
            "77d555c1ea37c2ad2a4d641ccf1d8b93"
        ),
        "out_dir": Path("outputs/_regression_4a3/ontario-g7-pdf"),
        "scope": ScopeSpec(
            source_reference=(
                "outputs/phase0-test-ontario-g7-history-2026-04-18/_source.pdf"
            ),
            section_identifier="History, Grade 7",
            notes="Regression replay Session 4a-3 Step 8.",
        ),
    },
]


def main() -> int:
    exit_code = 0
    for case in CASES:
        label = case["label"]
        expected = case["expected_hash"]
        out_dir = case["out_dir"]
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        try:
            m = acquire(scope=case["scope"], output_dir=out_dir)
            actual = m.content_hash or ""
            ok = actual == expected
            status = "OK" if ok else "DRIFT"
            print(f"[{status}] {label}")
            print(f"    expected: {expected}")
            print(f"    actual  : {actual}")
            if not ok:
                exit_code = 1
        except Exception as exc:  # noqa: BLE001
            print(f"[ERROR] {label}: {exc}")
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
