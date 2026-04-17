#!/usr/bin/env python3
"""Foundation moment 3 — `GCSE_AQA_EXAM_BLOCK` scoped to AQA sources.

Assertion: the `GCSE_AQA_EXAM_BLOCK` prompt fragment (AQA command-word
and mark-tariff awareness) is only attached to runs whose source is
an AQA exam specification. It must not be applied to non-AQA exam
specifications (e.g. felvételi, IB, state-specific boards).

Status: pending — and it reflects a known bug. The block is currently
gated on `document_family == "exam_specification"`, which over-matches.
"""
from __future__ import annotations

from _stub import not_implemented


def main() -> None:
    not_implemented(
        script="validate_exam_block_scope.py",
        status="pending",
        foundation_moment=3,
        assertion=(
            "GCSE_AQA_EXAM_BLOCK is not applied to non-AQA sources"
        ),
        reads=(
            "the run config (source.jurisdiction, source.documentFamily, "
            "any awarding_body field) and outputs/<run>/<runId>_run_"
            "report_v1.md for the recorded prompt-fragment attachments"
        ),
        notes=(
            "KNOWN BUG — current gating is document_family == "
            "'exam_specification', which matches felvételi equally. Fix "
            "needs either (a) an explicit source.awardingBody field, or "
            "(b) a Phase 1 awarding-body inference, before this gate can "
            "meaningfully fire. Until then, the gate will fail on any "
            "non-AQA exam_specification run where the block attached."
        ),
    )


if __name__ == "__main__":
    main()
