"""Adversarial tests for ``verify_extraction_quality``.

Empirical proof that the verifier fails correctly on broken extractions.
Each test feeds a constructed-bad input to the primitive and asserts the
expected verdict plus the specific failing check. If any of these
assertions regress, the verifier's thresholds are misconfigured.

Test corpus:

- ``test_ap_ced_original_content_fails_character_doubling`` — real
  failure from Session 4a-1: AP US Gov CED extracted without
  coordinate-level dedup. Systematic footer-only doubling that would
  fall below a document-wide ratio threshold but must still fail via
  the systematic-failure branch. Content hash is pinned so the test
  cannot drift onto the post-fix version.
- ``test_whitespace_runs_synthetic_failure`` — many 80+ character
  whitespace runs. Must fail on ``whitespace_runs``.
- ``test_empty_lines_synthetic_failure`` — mostly-empty document. Must
  fail on ``empty_line_ratio``.
- ``test_bigram_synthetic_failure`` — one word repeated many times.
  Must fail on ``repeated_bigram``.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
)
from curriculum_harness.phases.phase0_acquisition.primitives.verify_extraction_quality import (
    VerifyExtractionQualityPrimitive,
)


AP_4A1_SNAPSHOT = (
    Path(__file__).resolve().parents[2]
    / "docs"
    / "run-snapshots"
    / "2026-04-18-session-4a-1-phase0-test-ap-usgov"
    / "content.txt"
)

# Hash pinned from the Session 4a-1 snapshot (pre-fix, doubled content).
# If this hash does not match, the test has been pointed at the wrong
# file — stop and investigate before accepting the test as passing.
AP_4A1_CONTENT_HASH = (
    "47d41e8bc6031c9bc91decaa0be5b65f11357452022202d26d662ef0bea7215a"
)


def _run_verifier(
    text: str, **kwargs
) -> PrimitiveResult:
    prim = VerifyExtractionQualityPrimitive(**kwargs)

    class _Scope:
        source_reference = "test"

    return prim.run(_Scope(), PrimitiveResult(output=text))


def _check_by_name(checks: list[dict], name: str) -> dict:
    for c in checks:
        if c.get("name") == name:
            return c
    raise AssertionError(f"check {name!r} not present in verifier output")


def test_ap_ced_original_content_fails_character_doubling() -> None:
    assert AP_4A1_SNAPSHOT.exists(), (
        f"Session 4a-1 snapshot not found at {AP_4A1_SNAPSHOT}; "
        "this test depends on the pre-fix AP CED content being present."
    )
    data = AP_4A1_SNAPSHOT.read_bytes()
    actual_hash = hashlib.sha256(data).hexdigest()
    assert actual_hash == AP_4A1_CONTENT_HASH, (
        "AP 4a-1 content hash mismatch — expected "
        f"{AP_4A1_CONTENT_HASH}, got {actual_hash}. Do not proceed; the "
        "file may have been overwritten with post-fix content."
    )

    text = data.decode("utf-8")
    result = _run_verifier(text)

    assert result.summary["verdict"] == "failed", (
        "AP CED original content (doubled) must verdict 'failed'"
    )

    cd = _check_by_name(result.summary["checks"], "character_doubling")
    assert cd["passed"] is False, "character_doubling must fail on AP original"
    assert cd["systematic_failure"] is True, (
        "AP CED doubling is systematic (footer-only across pages); the "
        "systematic-failure branch is the gate that catches it"
    )


def test_whitespace_runs_synthetic_failure() -> None:
    # Current verifier thresholds: ws_failed when count of 80+ char
    # whitespace runs > whitespace_run_max * 10 = 50. Construct 60
    # separate 80-space runs to trip the failure branch.
    block = " " * 80
    real_line = "The quick brown fox jumps over the lazy dog. "
    parts = []
    for _ in range(60):
        parts.append(real_line)
        parts.append(block)
        parts.append("\n")
    text = "".join(parts)

    result = _run_verifier(text)

    assert result.summary["verdict"] == "failed"
    ws = _check_by_name(result.summary["checks"], "whitespace_runs")
    assert ws["passed"] is False, "whitespace_runs must fail on 60 runs"


def test_empty_lines_synthetic_failure() -> None:
    content_lines = [
        f"Content line {i}: The quick brown fox jumps over the lazy dog."
        for i in range(50)
    ]
    empty_lines = [""] * 500
    text = "\n".join(content_lines + empty_lines)

    result = _run_verifier(text)

    assert result.summary["verdict"] == "failed"
    el = _check_by_name(result.summary["checks"], "empty_line_ratio")
    assert el["passed"] is False, (
        "empty_line_ratio must fail when > 60 % of lines are empty"
    )


def test_bigram_synthetic_failure() -> None:
    # "the the the ..." 5000 times. The bigram check case-folds and
    # considers letter-only bigrams, so the repeated stream yields three
    # distinct bigrams (th, he, et) sharing ~100 % of the total — well
    # above top_bigram_failure_threshold (0.75).
    text = ("the " * 5000).strip()

    result = _run_verifier(text)

    assert result.summary["verdict"] == "failed"
    bg = _check_by_name(result.summary["checks"], "repeated_bigram")
    assert bg["passed"] is False, (
        "repeated_bigram must fail when a single word dominates the "
        "bigram distribution"
    )


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
