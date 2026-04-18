"""Whitespace normalisation primitive.

Collapses runs of horizontal whitespace, normalises line endings to
``\\n``, collapses runs of >2 consecutive newlines to exactly 2, strips
leading/trailing whitespace on each line, and strips the document.
UTF-8 output is enforced at the caller (encoding-detection primitive
upstream).
"""

from __future__ import annotations

import re

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
)


_HORIZONTAL_WS = re.compile(r"[ \t\f\v]+")
_CR_LF = re.compile(r"\r\n?")
_TRIPLE_NL = re.compile(r"\n{3,}")


def normalise_text(text: str) -> str:
    if not text:
        return ""
    s = _CR_LF.sub("\n", text)
    lines = [_HORIZONTAL_WS.sub(" ", line).strip() for line in s.split("\n")]
    s = "\n".join(lines)
    s = _TRIPLE_NL.sub("\n\n", s)
    return s.strip()


class NormaliseWhitespacePrimitive:
    name = "normalise_whitespace"
    required_scope_fields: tuple[str, ...] = ()
    optional_scope_fields: tuple[str, ...] = ()
    side_effects: frozenset[str] = frozenset()

    def validate_scope(self, scope) -> None:
        return None

    def run(self, scope, previous: PrimitiveResult | None) -> PrimitiveResult:
        text_in = "" if previous is None else str(previous.output or "")
        text_out = normalise_text(text_in)
        return PrimitiveResult(
            output=text_out,
            summary={
                "chars_in": len(text_in),
                "chars_out": len(text_out),
            },
        )
