"""Phase 0 extraction — Welsh Curriculum for Wales Health and Well-being
"Statements of what matters" (Session 4a-5 Step 3).

Dispositional-domain source: closes the domain-coverage gap in the
Phase 0 corpus. Reuses the Welsh Maths SoW extraction primitive sequence
(Session 4a-4 Step 9) unchanged — scope-only differences from that run:
the URL points at a different AoLE, the chrome list and content-root
selector are identical.

Writes into
docs/run-snapshots/2026-04-19-session-4a-5-wales-cfw-health-wellbeing-sow/.
If the primitive needs code changes to handle this source, the
architecture is wrong — halt and close with a deferred-primitive-work
finding instead.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from curriculum_harness.phases.phase0_acquisition.acquire import acquire
from curriculum_harness.phases.phase0_acquisition.scope import (
    HtmlNestedDomScope,
)
from curriculum_harness.phases.phase0_acquisition.type_detector import (
    DetectionResult,
)


URL = (
    "https://hwb.gov.wales/curriculum-for-wales/"
    "health-and-well-being/statements-of-what-matters/"
)
OUT = Path(
    "docs/run-snapshots/"
    "2026-04-19-session-4a-5-wales-cfw-health-wellbeing-sow"
)


def main() -> None:
    scope = HtmlNestedDomScope(
        url=URL,
        content_root_selector="article#aole-v2",
        exclude_selectors=[
            "nav",
            ".tab-next-prev",
            ".explore-links",
            ".contents",
            ".cookie-block",
            ".breadcrumb",
        ],
        include_details_content=True,
        preserve_headings=True,
        notes=(
            "Welsh Government / hwb.gov.wales — Curriculum for Wales, "
            "Health and Well-being Area of Learning and Experience, "
            "Statements of what matters. Session 4a-5 — dispositional-"
            "domain source extraction. Reuses the Session 4a-4 Step 9 "
            "(Welsh Maths SoW) primitive sequence unchanged; scope "
            "differs only by URL — content_root_selector and "
            "exclude_selectors are identical. See Step 2 investigation "
            "memo docs/diagnostics/"
            "2026-04-19-wales-cfw-health-wellbeing-sow-investigation.md "
            "and Step 1 pre-flight memo docs/diagnostics/"
            "2026-04-19-dispositional-source-preflight.md."
        ),
    )

    override = DetectionResult(
        source_type="html_nested_dom",
        confidence="high",
        rationale=(
            "Session 4a-5 deterministic override — identical site shape "
            "to Session 4a-4 Step 9 (article#aole-v2 single_main_container). "
            "Conservative auto-heuristic does not trip."
        ),
        signals={"override_source": "session_4a_5_runner"},
        is_supported_now=True,
    )

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    m = acquire(scope=scope, output_dir=OUT, detection_override=override)

    m.investigation_memo_refs = [
        "docs/diagnostics/2026-04-19-dispositional-source-preflight.md",
        "docs/diagnostics/"
        "2026-04-19-wales-cfw-health-wellbeing-sow-investigation.md",
    ]
    (OUT / "manifest.json").write_text(
        json.dumps(m.model_dump(mode="json"), indent=2, sort_keys=True),
        encoding="utf-8",
    )

    print("Run complete.")
    print("  source_type :", m.source_type)
    print("  content_hash:", m.content_hash)
    print("  chars       :", m.scope_acquired.get("chars"))
    print("  content_files:")
    for p in m.content_files:
        print(f"    - {p}")


if __name__ == "__main__":
    main()
