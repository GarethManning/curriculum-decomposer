"""Run Phase 1 twice against the same config and compare outputs.

Phase-1-only runner: calls `phase1_ingestion` directly rather than the
full pipeline so variance comparison doesn't incur a full end-to-end cost.
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(REPO_ROOT / ".env", override=False)

from curriculum_harness.graph import build_initial_state  # noqa: E402
from curriculum_harness.phases.phase1_ingestion import phase1_ingestion  # noqa: E402


async def _run_once(config_path: str, label: str) -> dict:
    cfg = json.loads(Path(config_path).read_text())
    state = build_initial_state(config_path, cfg)
    result = await phase1_ingestion(state)
    return {
        "label": label,
        "raw_curriculum_chars": len(result.get("raw_curriculum", "") or ""),
        "source_bullets_count": len(result.get("source_bullets", []) or []),
        "curriculum_profile": result.get("curriculum_profile", {}) or {},
        "errors": result.get("errors", []) or [],
        "raw_curriculum": result.get("raw_curriculum", "") or "",
        "source_bullets": result.get("source_bullets", []) or [],
    }


async def _main() -> None:
    out_dir = REPO_ROOT / "docs" / "run-snapshots" / "2026-04-18-session-3b-phase1-stability"
    out_dir.mkdir(parents=True, exist_ok=True)

    runA = await _run_once("configs/ontario_session3b_runA.json", "runA")
    runB = await _run_once("configs/ontario_session3b_runB.json", "runB")

    def _bullets_char_count(bullets: list[dict]) -> int:
        return sum(len(b.get("text", "")) for b in bullets)

    for run in (runA, runB):
        payload = {
            "raw_curriculum_chars": run["raw_curriculum_chars"],
            "source_bullets_count": run["source_bullets_count"],
            "source_bullets_char_count": _bullets_char_count(run["source_bullets"]),
            "curriculum_profile": run["curriculum_profile"],
            "errors": run["errors"],
        }
        (out_dir / f"{run['label']}_summary.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False)
        )
        (out_dir / f"{run['label']}_raw_curriculum.txt").write_text(run["raw_curriculum"])
        (out_dir / f"{run['label']}_source_bullets.json").write_text(
            json.dumps({"source_bullets": run["source_bullets"]}, indent=2, ensure_ascii=False)
        )

    def pct(a: int, b: int) -> float:
        if max(a, b) == 0:
            return 0.0
        return abs(a - b) / max(a, b) * 100.0

    bullet_var = pct(runA["source_bullets_count"], runB["source_bullets_count"])
    bullet_char_var = pct(
        _bullets_char_count(runA["source_bullets"]),
        _bullets_char_count(runB["source_bullets"]),
    )
    raw_char_var = pct(runA["raw_curriculum_chars"], runB["raw_curriculum_chars"])

    report = [
        "# Phase 1 variance — runA vs runB (Shape A + Shape B)",
        "",
        f"- runA bullets: {runA['source_bullets_count']} "
        f"(bullet-text chars: {_bullets_char_count(runA['source_bullets'])}, "
        f"raw_curriculum chars: {runA['raw_curriculum_chars']})",
        f"- runB bullets: {runB['source_bullets_count']} "
        f"(bullet-text chars: {_bullets_char_count(runB['source_bullets'])}, "
        f"raw_curriculum chars: {runB['raw_curriculum_chars']})",
        f"- bullet-count variance: {bullet_var:.1f}%",
        f"- bullet-text char variance: {bullet_char_var:.1f}%",
        f"- raw_curriculum char variance (non-bullet, informational): {raw_char_var:.1f}%",
        f"- threshold (binding-specifications): 15%",
        "",
        f"**Result (bullets only — the gate-binding artefact):** "
        f"{'PASS (under 15%)' if (bullet_var < 15 and bullet_char_var < 15) else 'FAIL (>= 15%)'}",
        "",
        "Note: `raw_curriculum` is the Haiku-narrowed text used by downstream",
        "LLM phases. It still varies run-to-run because Anthropic's streaming",
        "inference at temperature 0 is not bit-for-bit deterministic (documented",
        "server-side batching effects). The downstream phases are LLM-based",
        "anyway and tolerate this informational variance. The load-bearing",
        "artefact for source-evidence gates is `source_bullets`, which is now",
        "deterministic because it is extracted rule-based from the Phase 1",
        "windowed slice rather than from the Haiku output.",
    ]
    (out_dir / "variance_report.md").write_text("\n".join(report) + "\n")
    print("\n".join(report))


if __name__ == "__main__":
    asyncio.run(_main())
