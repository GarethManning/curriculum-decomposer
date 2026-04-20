"""Adversarial test suite — developmental scope detection.

Tests detect_developmental_scope against known ground-truth sources and
edge cases. All 8 cases must pass.

Usage:
    python scripts/test_developmental_scope_adversarial.py

Exit code 0 = all pass. Non-zero = failures (details printed to stdout).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

# Allow running from repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from curriculum_harness.reference_authoring.developmental_scope.detect_scope import (
    detect_developmental_scope,
    make_developmental_scope_flag,
)
from curriculum_harness.reference_authoring.progression.detect_progression import (
    ProgressionStructure,
)
from curriculum_harness.reference_authoring.types import ContentBlock, SourceInventory


# ---------------------------------------------------------------------------
# Helpers: build mock objects
# ---------------------------------------------------------------------------


def _inv(slug: str, ref: str = "", blocks: list[ContentBlock] | None = None) -> SourceInventory:
    return SourceInventory(
        source_slug=slug,
        snapshot_path="",
        manifest_content_hash="",
        phase0_version="",
        source_reference=ref,
        content_blocks=blocks or [],
    )


def _blk(text: str, block_id: str = "blk_0001") -> ContentBlock:
    return ContentBlock(
        block_id=block_id,
        raw_text=text,
        block_type="paragraph",
        line_start=1,
        line_end=2,
    )


def _prog(source_type: str, band_count: int = 1) -> ProgressionStructure:
    return ProgressionStructure(
        band_labels=["Band"] * band_count,
        band_count=band_count,
        age_range_hint="",
        source_type=source_type,
        detection_confidence="high",
        detection_rationale="mock",
    )


# ---------------------------------------------------------------------------
# Test definitions
# ---------------------------------------------------------------------------


@dataclass
class TestCase:
    name: str
    inventory: SourceInventory
    progression_structure: ProgressionStructure
    expected_scope: str
    expected_confidence: str
    description: str


CASES: list[TestCase] = [
    # ------------------------------------------------------------------
    # Case 1 — Known single_band: Common Core 7.RP
    # Source type us_common_core_grade → single_band, high (curated map).
    # ------------------------------------------------------------------
    TestCase(
        name="Case 1 — Known single_band: Common Core 7.RP",
        inventory=_inv("2a-regression-common-core-7rp"),
        progression_structure=_prog("us_common_core_grade", band_count=1),
        expected_scope="single_band",
        expected_confidence="high",
        description=(
            "Common Core 7.RP: single-grade source. Curated map gives "
            "(single_band, high) for source_type=us_common_core_grade."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 2 — Known explicit_progression: Welsh CfW H&W
    # Source type welsh_cfw_aole → explicit_progression, high (curated map).
    # ------------------------------------------------------------------
    TestCase(
        name="Case 2 — Known explicit_progression: Welsh CfW H&W",
        inventory=_inv("wales-cfw-health-wellbeing-sow"),
        progression_structure=_prog("welsh_cfw_aole", band_count=5),
        expected_scope="explicit_progression",
        expected_confidence="high",
        description=(
            "Welsh CfW H&W: 5 Progression Steps. Curated map gives "
            "(explicit_progression, high) for source_type=welsh_cfw_aole."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 3 — Known range_without_bands: Secondary RSHE 2025
    # Source type england_rshe_secondary → range_without_bands, high.
    # ------------------------------------------------------------------
    TestCase(
        name="Case 3 — Known range_without_bands: Secondary RSHE 2025",
        inventory=_inv("2a-secondary-rshe-2025"),
        progression_structure=_prog("england_rshe_secondary", band_count=1),
        expected_scope="range_without_bands",
        expected_confidence="high",
        description=(
            "RSHE 2025: KS3+KS4 combined terminal outcomes. Curated map gives "
            "(range_without_bands, high) for source_type=england_rshe_secondary."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 4 — Edge: age range in content but no Level markers
    # Unknown source_type, content mentions age range text, no per-level markers.
    # Expected: range_without_bands, medium or high.
    # ------------------------------------------------------------------
    TestCase(
        name="Case 4 — Edge: age range in metadata, no progression markers",
        inventory=_inv(
            "hypothetical-multi-year-source",
            blocks=[
                _blk(
                    "By the end of the programme, students aged 11-14 will be able to "
                    "demonstrate understanding of core concepts in this domain.",
                    "blk_0001",
                ),
                _blk(
                    "Students will develop skills across the full secondary phase, "
                    "regardless of their specific year group.",
                    "blk_0002",
                ),
            ],
        ),
        progression_structure=_prog("unknown_custom_type", band_count=1),
        expected_scope="range_without_bands",
        expected_confidence="high",  # terminal-outcome language → high
        description=(
            "Unknown source type. Content has age range reference and terminal-outcome "
            "language ('by the end of the programme'). No per-level markers. "
            "Expected: range_without_bands. Confidence high because terminal-outcome "
            "language is present with no year/grade refs that would create ambiguity."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 5 — Edge: explicit "Year 7 only" content → single_band, high
    # Unknown source_type, content explicitly scopes to a single year.
    # ------------------------------------------------------------------
    TestCase(
        name="Case 5 — Edge: explicit single-year source",
        inventory=_inv(
            "hypothetical-year7-source",
            blocks=[
                _blk("This specification covers Year 7 only.", "blk_0001"),
                _blk(
                    "Grade 7 students will apply proportional reasoning to solve "
                    "multi-step ratio problems.",
                    "blk_0002",
                ),
            ],
        ),
        progression_structure=_prog("unknown_custom_type", band_count=1),
        expected_scope="single_band",
        expected_confidence="high",
        description=(
            "Unknown source type. Content has a single Grade reference and no "
            "terminal-outcome language. Expected: single_band, high."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 6 — Edge: source with explicit CfE Levels → explicit_progression
    # Source type scottish_cfe → curated map → explicit_progression, high.
    # (Also tests AP US Gov Unit 1 as single_band ground truth.)
    # ------------------------------------------------------------------
    TestCase(
        name="Case 6 — Edge: Scottish CfE source (explicit Levels)",
        inventory=_inv("scottish-cfe-health-wellbeing"),
        progression_structure=_prog("scottish_cfe", band_count=6),
        expected_scope="explicit_progression",
        expected_confidence="high",
        description=(
            "Scottish CfE: Early/First/Second/Third/Fourth/Senior levels. "
            "Curated map gives (explicit_progression, high)."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 7 — Edge: source with per-level guidance (NZ curriculum with
    # explicit Level markers in content) → explicit_progression, high.
    # Tests content inspection for nz_curriculum source type.
    # ------------------------------------------------------------------
    TestCase(
        name="Case 7 — Edge: NZ curriculum with per-level content",
        inventory=_inv(
            "nz-hypothetical-with-levels",
            ref="https://newzealandcurriculum.tahurangi.education.govt.nz/sample",
            blocks=[
                _blk("Level 3: Students will understand the concept of place.", "blk_0001"),
                _blk("Level 4: Students will apply geographical reasoning across contexts.", "blk_0002"),
                _blk("Level 5: Students will evaluate competing geographical perspectives.", "blk_0003"),
            ],
        ),
        progression_structure=_prog("nz_curriculum", band_count=8),
        expected_scope="explicit_progression",
        expected_confidence="high",
        description=(
            "NZ curriculum source with >= 2 distinct 'Level N' markers in content. "
            "Content inspection path for nz_curriculum → explicit_progression, high."
        ),
    ),
    # ------------------------------------------------------------------
    # Case 8 — Edge: ambiguous source → low confidence classification
    # Content has both per-level markers AND terminal-outcome language.
    # ------------------------------------------------------------------
    TestCase(
        name="Case 8 — Edge: ambiguous source (per-level + terminal-outcome language)",
        inventory=_inv(
            "ambiguous-multi-signal-source",
            blocks=[
                _blk("Level 3: Learners will begin to engage with primary sources.", "blk_0001"),
                _blk("Level 4: Learners will apply source analysis skills.", "blk_0002"),
                _blk(
                    "By the end of the programme, all students will be able to "
                    "evaluate historical arguments using multiple perspectives.",
                    "blk_0003",
                ),
            ],
        ),
        progression_structure=_prog("unknown_custom_type", band_count=1),
        expected_scope="explicit_progression",  # per-level wins, but low confidence
        expected_confidence="low",
        description=(
            "Unknown source type. Content has both Level markers (per-level) "
            "AND terminal-outcome language ('by the end of the programme'). "
            "Contradictory signals → explicit_progression with low confidence."
        ),
    ),
]


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def run_tests() -> int:
    failures = 0
    print(f"Running {len(CASES)} adversarial test cases...\n")

    for i, case in enumerate(CASES, 1):
        result = detect_developmental_scope(case.inventory, case.progression_structure)

        scope_ok = result.developmental_scope == case.expected_scope
        conf_ok = result.developmental_scope_confidence == case.expected_confidence

        if scope_ok and conf_ok:
            print(f"  PASS {i:2d}. {case.name}")
            print(f"         → ({result.developmental_scope}, {result.developmental_scope_confidence})")
        else:
            failures += 1
            print(f"  FAIL {i:2d}. {case.name}")
            print(f"         Expected: ({case.expected_scope}, {case.expected_confidence})")
            print(f"         Got:      ({result.developmental_scope}, {result.developmental_scope_confidence})")
            print(f"         Rationale: {result.detection_rationale}")
            if result.ambiguity_notes:
                print(f"         Ambiguity: {result.ambiguity_notes}")
        print()

    print("-" * 60)
    print(f"Results: {len(CASES) - failures}/{len(CASES)} passed.")

    if failures == 0:
        print("All tests passed.")
    else:
        print(f"{failures} test(s) FAILED.")

    # Smoke test flag emission.
    print("\n--- Flag emission smoke test ---")
    rshe_inv = _inv("2a-secondary-rshe-2025")
    rshe_prog = _prog("england_rshe_secondary", band_count=1)
    rshe_result = detect_developmental_scope(rshe_inv, rshe_prog)
    flag = make_developmental_scope_flag(rshe_result, domain_type="dispositional")
    assert flag is not None, "Flag should be emitted for range_without_bands"
    assert flag["flag_type"] == "developmental_scope_range_without_bands"
    assert "explanation_pedagogical_dispositional" in flag
    # domain_type=dispositional: cognitive explanation NOT included (dispositional sources only)
    assert "explanation_pedagogical_cognitive" not in flag
    print(f"  Flag type: {flag['flag_type']}")
    print(f"  Confidence tier: {flag['confidence_tier']}")
    print(f"  Domain type: {flag['domain_type']}")
    print(f"  Technical: {flag['explanation_technical'][:80]}...")
    print(f"  Dispositional: {flag['explanation_pedagogical_dispositional'][:80]}...")

    no_flag = make_developmental_scope_flag(
        detect_developmental_scope(_inv("wales-cfw-health-wellbeing-sow"), _prog("welsh_cfw_aole", 5)),
        domain_type="sequential",
    )
    assert no_flag is None, "explicit_progression should not emit a flag"
    print("  No-flag assertion for explicit_progression: PASS")

    return failures


if __name__ == "__main__":
    sys.exit(run_tests())
