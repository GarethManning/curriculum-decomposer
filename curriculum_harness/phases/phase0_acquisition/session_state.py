"""User-in-the-loop session state.

When a primitive cannot proceed without user input (e.g. unsupported
source type, missing scope field, encoding failure, or a scope spec
that does not match the document), Phase 0 pauses and writes:

- A ``request.md`` file — human-readable description of what Phase 0
  needs from the user, in what format, and how to resume.
- A ``state.json`` file — machine-readable pause state so resumption
  re-enters the sequence at exactly the pause point, not from scratch.

The user writes a corresponding ``provided.txt`` (or ``provided.json``
for structured fields). ``resume_session_state`` reads the state,
validates the provided file, and returns the content so the caller can
continue the sequence.

State is hand-editable plain text / JSON by design — a user should be
able to look at the state directory and understand what happened.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass
class PauseState:
    """Serialisable pause-state record.

    Attributes:
        primitive: The primitive that paused.
        reason: Short machine-readable reason tag.
        needed: Free-form prose — what we need from the user.
        expected_format: Tag for the expected provided-file format —
            ``"plain_text"``, ``"json"``, or ``"scope_fields"``.
        resume_hint: Short instructions on how to resume.
        state_dir: Absolute path to the pause directory.
        source_reference: Original source (URL or path) being acquired.
        created_at: ISO 8601 UTC timestamp.
        extra: Primitive-specific structured context (e.g. detected
            source_type, missing scope fields).
    """

    primitive: str
    reason: str
    needed: str
    expected_format: str
    resume_hint: str
    state_dir: str
    source_reference: str
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
    )
    extra: dict[str, Any] = field(default_factory=dict)


def _render_request_md(state: PauseState) -> str:
    lines = [
        f"# Phase 0 paused — {state.primitive}",
        "",
        f"- **Source:** {state.source_reference}",
        f"- **Reason tag:** `{state.reason}`",
        f"- **Created:** {state.created_at}",
        "",
        "## What Phase 0 needs from you",
        "",
        state.needed.strip(),
        "",
        "## Expected format",
        "",
        f"- `{state.expected_format}`",
        "",
        "## How to resume",
        "",
        state.resume_hint.strip(),
        "",
    ]
    if state.extra:
        lines.append("## Context")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(state.extra, indent=2, sort_keys=True))
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def write_pause_state(
    base_dir: str | os.PathLike[str],
    state: PauseState,
) -> dict[str, str]:
    """Write ``state.json`` and ``request.md`` under ``base_dir``.

    Returns a dict with the paths written, for the manifest trace.
    """

    path = Path(base_dir)
    path.mkdir(parents=True, exist_ok=True)

    state_file = path / "state.json"
    request_file = path / "request.md"

    state_file.write_text(
        json.dumps(asdict(state), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    request_file.write_text(_render_request_md(state), encoding="utf-8")

    return {
        "state_file": str(state_file),
        "request_file": str(request_file),
    }


def read_pause_state(base_dir: str | os.PathLike[str]) -> PauseState:
    path = Path(base_dir) / "state.json"
    if not path.exists():
        raise FileNotFoundError(f"No state.json at {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    return PauseState(**data)


def resume_from_provided(
    base_dir: str | os.PathLike[str],
) -> tuple[PauseState, str | dict[str, Any]]:
    """Read pause state + user-provided content.

    Looks for ``provided.txt`` (plain text) or ``provided.json``
    (structured) in the pause directory, depending on
    ``state.expected_format``. Returns ``(state, provided_content)``.
    Raises ``FileNotFoundError`` if neither is present.
    """

    state = read_pause_state(base_dir)
    path = Path(base_dir)

    if state.expected_format == "plain_text":
        p = path / "provided.txt"
        if not p.exists():
            raise FileNotFoundError(
                f"Expected provided.txt at {p} to resume {state.primitive}"
            )
        return state, p.read_text(encoding="utf-8")

    if state.expected_format in ("json", "scope_fields"):
        p = path / "provided.json"
        if not p.exists():
            raise FileNotFoundError(
                f"Expected provided.json at {p} to resume {state.primitive}"
            )
        return state, json.loads(p.read_text(encoding="utf-8"))

    raise ValueError(f"Unknown expected_format: {state.expected_format}")
