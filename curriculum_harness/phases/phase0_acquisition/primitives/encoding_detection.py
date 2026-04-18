"""Encoding-detection primitive.

Takes raw ``bytes`` (or a ``(bytes, declared_encoding)`` tuple carried
in ``previous.meta``) and returns a UTF-8 string. Detection failures
are flagged in ``meta["encoding_failure"]`` rather than silently
producing corrupt text — the caller records the flag in the manifest.

Uses ``charset_normalizer`` (a dependency of ``requests``, already in
the environment). Falls back to the declared encoding from the HTTP
response when detection confidence is low.
"""

from __future__ import annotations

import charset_normalizer

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
)


class EncodingDetectionPrimitive:
    name = "encoding_detection"
    required_scope_fields: tuple[str, ...] = ()
    optional_scope_fields: tuple[str, ...] = ()
    side_effects: frozenset[str] = frozenset()

    def validate_scope(self, scope) -> None:
        return None

    def run(self, scope, previous: PrimitiveResult | None) -> PrimitiveResult:
        if previous is None or previous.output is None:
            return PrimitiveResult(
                output="",
                summary={"status": "no_input"},
                meta={"encoding_detected": None, "encoding_failure": "no_input"},
            )

        raw = previous.output
        declared = (previous.meta or {}).get("declared_encoding")

        if isinstance(raw, str):
            return PrimitiveResult(
                output=raw,
                summary={"status": "already_str", "declared_encoding": declared},
                meta={"encoding_detected": declared or "utf-8"},
            )

        if not isinstance(raw, (bytes, bytearray)):
            return PrimitiveResult(
                output=str(raw),
                summary={"status": "coerced_to_str"},
                meta={
                    "encoding_detected": None,
                    "encoding_failure": "input_not_bytes_or_str",
                },
            )

        results = charset_normalizer.from_bytes(bytes(raw))
        best = results.best()

        if best is None:
            fallback_enc = declared or "utf-8"
            try:
                text = bytes(raw).decode(fallback_enc, errors="replace")
                return PrimitiveResult(
                    output=text,
                    summary={
                        "status": "fallback_decode",
                        "fallback_encoding": fallback_enc,
                    },
                    meta={
                        "encoding_detected": fallback_enc,
                        "encoding_failure": "charset_normalizer_returned_none",
                    },
                )
            except (LookupError, UnicodeDecodeError) as exc:
                text = bytes(raw).decode("utf-8", errors="replace")
                return PrimitiveResult(
                    output=text,
                    summary={"status": "utf8_replace", "error": str(exc)},
                    meta={
                        "encoding_detected": "utf-8",
                        "encoding_failure": f"fallback_failed: {exc}",
                    },
                )

        detected = best.encoding
        text = str(best)
        return PrimitiveResult(
            output=text,
            summary={
                "status": "detected",
                "encoding_detected": detected,
                "declared_encoding": declared,
                "chaos": round(best.chaos, 4),
            },
            meta={"encoding_detected": detected},
        )
