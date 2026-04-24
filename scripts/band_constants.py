"""Canonical REAL wellbeing band convention loader.

Single source of truth: docs/reference-corpus/real-wellbeing/band-conventions.json.
All band values in build scripts and preflight must be derived from this module.
No band values are hardcoded here — everything is loaded from the JSON at import time.

Raises ImportError at load time if band-conventions.json is missing, malformed,
or missing any of the six canonical bands (A–F).
"""

from __future__ import annotations

import json
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_BAND_CONVENTIONS_PATH = (
    _REPO_ROOT
    / "docs"
    / "reference-corpus"
    / "real-wellbeing"
    / "band-conventions.json"
)

_EXPECTED_LETTERS = frozenset({"A", "B", "C", "D", "E", "F"})


def _load() -> dict:
    if not _BAND_CONVENTIONS_PATH.exists():
        raise ImportError(
            f"band-conventions.json not found at {_BAND_CONVENTIONS_PATH}. "
            "This file is the canonical source of truth for REAL wellbeing bands. "
            "See docs/reference-corpus/real-wellbeing/band-conventions.json."
        )
    try:
        with _BAND_CONVENTIONS_PATH.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise ImportError(
            f"band-conventions.json at {_BAND_CONVENTIONS_PATH} is malformed: {exc}"
        ) from exc

    bands = data.get("bands")
    if not isinstance(bands, dict):
        raise ImportError(
            f"band-conventions.json missing or malformed 'bands' object at {_BAND_CONVENTIONS_PATH}."
        )

    missing = _EXPECTED_LETTERS - set(bands.keys())
    if missing:
        raise ImportError(
            f"band-conventions.json missing canonical band letters: {sorted(missing)}. "
            "Expected all of A, B, C, D, E, F."
        )

    for letter in _EXPECTED_LETTERS:
        entry = bands[letter]
        if not isinstance(entry, dict):
            raise ImportError(
                f"band-conventions.json band '{letter}' is not an object."
            )
        if "band_label" not in entry or not isinstance(entry["band_label"], str):
            raise ImportError(
                f"band-conventions.json band '{letter}' missing string 'band_label'."
            )

    return data


_DATA = _load()

BAND_CONVENTIONS_PATH = _BAND_CONVENTIONS_PATH

VALID_BAND_LETTERS = frozenset(_EXPECTED_LETTERS)

BAND_META = {letter: _DATA["bands"][letter] for letter in sorted(_EXPECTED_LETTERS)}

BAND_LABELS = {letter: BAND_META[letter]["band_label"] for letter in BAND_META}
