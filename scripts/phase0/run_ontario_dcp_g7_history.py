"""Phase 0 extraction — Ontario DCP Grade 7 History via the
js_rendered_progressive_disclosure sequence (Session 4a-3 Step 6).

Writes into docs/run-snapshots/2026-04-18-session-4a-3-ontario-dcp-g7-history/.
Uses a detection_override because the page classifies as
js_rendered_progressive_disclosure under the updated Angular markers in
the type detector; the override keeps the run deterministic against
source-type drift (e.g. if marker heuristics change in later sessions).
"""

from __future__ import annotations

from pathlib import Path

from curriculum_harness.phases.phase0_acquisition.acquire import acquire
from curriculum_harness.phases.phase0_acquisition.manifest import ScopeSpec
from curriculum_harness.phases.phase0_acquisition.type_detector import (
    DetectionResult,
)


URL = (
    "https://www.dcp.edu.gov.on.ca/en/curriculum/elementary-sshg/"
    "grades/g7-history/strands"
)
OUT = Path(
    "docs/run-snapshots/2026-04-18-session-4a-3-ontario-dcp-g7-history"
)


def main() -> None:
    scope = ScopeSpec(
        source_reference=URL,
        url=URL,
        wait_for_selector="main",
        css_selector="main",
        browser_timeout_ms=60000,
        notes=(
            "Ontario DCP Grade 7 History, Expectations by strand. "
            "Session 4a-3 Step 6 — first test of js_rendered_progressive_disclosure "
            "primitive sequence. Extracts overall-expectation content "
            "including FOCUS ON tags; specific-expectations text lives "
            "on SPA-routed sub-pages (see investigation memo)."
        ),
    )
    override = DetectionResult(
        source_type="js_rendered_progressive_disclosure",
        confidence="high",
        rationale=(
            "Session 4a-3 Step 6 deterministic override — Ontario DCP "
            "is an Angular Material SPA (ng-version + mat-* markers)."
        ),
        signals={"override_source": "session_4a_3_step_6_runner"},
        is_supported_now=True,
    )
    if OUT.exists():
        import shutil

        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    m = acquire(scope=scope, output_dir=OUT, detection_override=override)

    print("Run complete.")
    print("  source_type :", m.source_type)
    print("  content_hash:", m.content_hash)
    print("  dom_hash    :", m.dom_hash)
    print("  chars       :", m.scope_acquired.get("chars"))
    print("  content_files:")
    for p in m.content_files:
        print(f"    - {p}")


if __name__ == "__main__":
    main()
