"""Session 4a-4.5 Step 5 — regenerate all current Phase 0 artefacts
under schema 0.6.0 with raw-content caching active.

Writes each regeneration into a fresh run-snapshot directory:
``docs/run-snapshots/2026-04-18-session-4a-4-5-<slug>/``. The
canonical 4a-1/4a-2/4a-3/4a-4 snapshots are left untouched as
historical records under their earlier schemas.

Re-fetch outcomes per source:

- Common Core 7.RP — Cloudflare block (observed 4a-3). If re-fetch
  fails and no preserved raw HTML is available, mark
  ``raw_content_unavailable`` with a first_observed_at timestamp.
- NZ Curriculum — bot detection (observed 4a-4). Same treatment.
- AP CED — College Board robots.txt disallow; local file already
  archived. Reference via ``source_reference`` with hash, no copy.
- Everything else — live re-fetch with raw cache.

Pre-flight verification is performed before any regeneration:
- AP CED local PDF path
- Preserved Common Core 7.RP raw HTML (grep-scan, two minutes budget)

Outputs a structured summary dict so the caller (or the
regression-from-cache utility in Step 6) can tell at a glance which
artefacts cached successfully and which are gapped.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from curriculum_harness.phases.phase0_acquisition.acquire import acquire
from curriculum_harness.phases.phase0_acquisition.executor import (
    Phase0Paused,
)
from curriculum_harness.phases.phase0_acquisition.manifest import (
    AcquisitionManifest,
    RawContentUnavailable,
    ScopeSpec,
)
from curriculum_harness.phases.phase0_acquisition.type_detector import (
    DetectionResult,
)


REPO = Path(__file__).resolve().parents[2]
SNAP_ROOT = REPO / "docs/run-snapshots"
UNAVAILABLE_TIMESTAMP = "2026-04-18"


CASES: list[dict[str, Any]] = [
    {
        "slug": "common-core-7rp",
        "label": "Common Core 7.RP",
        "scope_kwargs": dict(
            source_reference="https://www.thecorestandards.org/Math/Content/7/RP/",
            url="https://www.thecorestandards.org/Math/Content/7/RP/",
            css_selector="article section.content",
        ),
        "detection_override": None,
        "known_gap_on_refetch": (
            "Cloudflare challenge blocks programmatic re-fetch; no "
            "preserved raw HTML available."
        ),
    },
    {
        "slug": "dfe-ks3-maths-pdf",
        "label": "DfE KS3 Maths (PDF URL)",
        "scope_kwargs": dict(
            source_reference=(
                "https://assets.publishing.service.gov.uk/media/"
                "5a7c1408e5274a1f5cc75a68/SECONDARY_national_curriculum_"
                "-_Mathematics.pdf"
            ),
        ),
        "detection_override": None,
        "known_gap_on_refetch": None,
    },
    {
        "slug": "ap-usgov-ced-unit1",
        "label": "AP US Gov CED Unit 1 (local PDF)",
        "scope_kwargs": dict(
            source_reference=str(
                REPO
                / "outputs/phase0-test-ap-usgov-unit1-requeued-2026-04-18/_source.pdf"
            ),
            page_range=[40, 55],
            section_heading="Foundations of American Democracy",
            pdf_dedup_coords=True,
            pdf_dedup_coord_tolerance=1,
        ),
        "detection_override": None,
        "known_gap_on_refetch": None,
    },
    {
        "slug": "ontario-k8-g7-history-pdf",
        "label": "Ontario K-8 Grade 7 History (local PDF)",
        "scope_kwargs": dict(
            source_reference=str(
                REPO
                / "outputs/phase0-test-ontario-g7-history-2026-04-18/_source.pdf"
            ),
            section_identifier="History, Grade 7",
        ),
        "detection_override": None,
        "known_gap_on_refetch": None,
    },
    {
        "slug": "ontario-dcp-g7-history",
        "label": "Ontario DCP Grade 7 History (JS)",
        "scope_kwargs": dict(
            source_reference=(
                "https://www.dcp.edu.gov.on.ca/en/curriculum/elementary-sshg/"
                "grades/g7-history/strands"
            ),
            url=(
                "https://www.dcp.edu.gov.on.ca/en/curriculum/elementary-sshg/"
                "grades/g7-history/strands"
            ),
            wait_for_selector="main",
            css_selector="main",
            browser_timeout_ms=60000,
        ),
        "detection_override": DetectionResult(
            source_type="js_rendered_progressive_disclosure",
            confidence="high",
            rationale="Session 4a-4.5 Step 5 deterministic override.",
            signals={"override_source": "session_4a_4_5_regen"},
            is_supported_now=True,
        ),
        "known_gap_on_refetch": None,
    },
    {
        "slug": "nz-curriculum-social-sciences",
        "label": "NZ Curriculum Social Sciences Phase 2 (JS)",
        "scope_kwargs": dict(
            source_reference=(
                "https://newzealandcurriculum.tahurangi.education.govt.nz/"
                "new-zealand-curriculum-online/nzc---social-sciences-years-4---6/"
                "5637290852.p"
            ),
            url=(
                "https://newzealandcurriculum.tahurangi.education.govt.nz/"
                "new-zealand-curriculum-online/nzc---social-sciences-years-4---6/"
                "5637290852.p"
            ),
            wait_for_selector="main",
            css_selector="main",
            dismiss_modal_selector="button[aria-label*='cookie' i]",
            browser_timeout_ms=60000,
        ),
        "detection_override": DetectionResult(
            source_type="js_rendered_progressive_disclosure",
            confidence="high",
            rationale="Session 4a-4.5 Step 5 deterministic override.",
            signals={"override_source": "session_4a_4_5_regen"},
            is_supported_now=True,
        ),
        "known_gap_on_refetch": (
            "Bot detection on live fetch (observed 4a-4); no preserved "
            "rendered DOM HTML available."
        ),
    },
    {
        "slug": "gov-uk-nc-maths-ks3",
        "label": "gov.uk NC Maths KS3",
        "scope_kwargs": dict(
            url=(
                "https://www.gov.uk/government/publications/"
                "national-curriculum-in-england-mathematics-programmes-of-study/"
                "national-curriculum-in-england-mathematics-programmes-of-study"
            ),
            content_root_selector=".govspeak",
            section_anchor_selector="#key-stage-3",
            include_details_content=True,
            preserve_headings=True,
        ),
        "detection_override": DetectionResult(
            source_type="html_nested_dom",
            confidence="high",
            rationale="Session 4a-4.5 Step 5 deterministic override.",
            signals={"override_source": "session_4a_4_5_regen"},
            is_supported_now=True,
        ),
        "known_gap_on_refetch": None,
    },
    {
        "slug": "wales-cfw-maths-sow",
        "label": "Wales CfW Maths Statements of what matters",
        "scope_kwargs": dict(
            url=(
                "https://hwb.gov.wales/curriculum-for-wales/"
                "mathematics-and-numeracy/statements-of-what-matters/"
            ),
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
        ),
        "detection_override": DetectionResult(
            source_type="html_nested_dom",
            confidence="high",
            rationale="Session 4a-4.5 Step 5 deterministic override.",
            signals={"override_source": "session_4a_4_5_regen"},
            is_supported_now=True,
        ),
        "known_gap_on_refetch": None,
    },
]


def _preflight() -> dict[str, Any]:
    """Run Step 5's specific pre-flight path checks and log results."""

    result: dict[str, Any] = {
        "ap_ced_local_pdf": {"expected_path": None, "found": False, "bytes": 0},
        "common_core_raw_html_search": {"ran": False, "found": False, "notes": ""},
        "ontario_k8_pdf": {"expected_path": None, "found": False, "bytes": 0},
    }

    ap_ced_path = (
        REPO
        / "outputs/phase0-test-ap-usgov-unit1-requeued-2026-04-18/_source.pdf"
    )
    result["ap_ced_local_pdf"]["expected_path"] = str(ap_ced_path)
    if ap_ced_path.exists():
        result["ap_ced_local_pdf"]["found"] = True
        result["ap_ced_local_pdf"]["bytes"] = ap_ced_path.stat().st_size

    ontario_pdf = (
        REPO / "outputs/phase0-test-ontario-g7-history-2026-04-18/_source.pdf"
    )
    result["ontario_k8_pdf"]["expected_path"] = str(ontario_pdf)
    if ontario_pdf.exists():
        result["ontario_k8_pdf"]["found"] = True
        result["ontario_k8_pdf"]["bytes"] = ontario_pdf.stat().st_size

    try:
        proc = subprocess.run(
            [
                "grep",
                "-rli",
                "-e",
                "7.RP",
                "-e",
                "thecorestandards",
                "--include=*.html",
                "--include=*.txt",
                "docs/",
                "outputs/",
                "scripts/",
            ],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=120,
        )
        hits = [
            line.strip()
            for line in proc.stdout.splitlines()
            if line.strip()
            and "run-snapshots" not in line  # skip already-extracted content
        ]
        result["common_core_raw_html_search"]["ran"] = True
        result["common_core_raw_html_search"]["found"] = bool(hits)
        result["common_core_raw_html_search"]["notes"] = (
            "\n".join(hits[:5]) if hits else "no preserved raw HTML found"
        )
    except Exception as exc:  # noqa: BLE001
        result["common_core_raw_html_search"]["notes"] = (
            f"grep_failed: {exc}"
        )

    return result


def _write_unavailable_manifest(
    *,
    slug: str,
    label: str,
    scope: Any,
    source_type_hint: str,
    reason: str,
    out_dir: Path,
) -> dict[str, Any]:
    """Write a 0.6.0 manifest capturing raw_content_unavailable only.

    Used when a known-gapped source (Cloudflare, bot detection) cannot
    be re-fetched and no preserved raw content exists. Leaves
    ``content_files`` / ``content_hash`` empty: the *extracted* content
    for these sources already lives under the original 4a-N snapshot
    and is consulted by the regression-from-cache utility.
    """

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = AcquisitionManifest(
        source_reference=(
            scope.source_reference
            if hasattr(scope, "source_reference") and scope.source_reference
            else getattr(scope, "url", "")
        ),
        source_type=source_type_hint,
        scope_requested=scope,
    )
    manifest.raw_content_unavailable = RawContentUnavailable(
        value=True,
        reason=reason,
        first_observed_at=UNAVAILABLE_TIMESTAMP,
    )
    manifest.notes = (
        f"Session 4a-4.5 Step 5 regeneration for `{label}` attempted "
        "but source is unavailable for programmatic re-fetch. "
        "Extracted content persists under the canonical 4a-N snapshot."
    )
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest.model_dump(mode="json"), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return {
        "slug": slug,
        "outcome": "unavailable",
        "reason": reason,
        "manifest": str(out_dir / "manifest.json"),
        "raw_content_files": [],
    }


def _run_one(case: dict[str, Any]) -> dict[str, Any]:
    slug = case["slug"]
    label = case["label"]
    out_dir = SNAP_ROOT / f"2026-04-18-session-4a-4-5-{slug}"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    scope = ScopeSpec(**case["scope_kwargs"])
    detection_override = case.get("detection_override")
    known_gap_reason = case.get("known_gap_on_refetch")

    try:
        m = acquire(
            scope=scope,
            output_dir=out_dir,
            detection_override=detection_override,
        )
    except Phase0Paused as exc:
        msg = str(exc)
        if known_gap_reason is not None:
            shutil.rmtree(out_dir)
            return _write_unavailable_manifest(
                slug=slug,
                label=label,
                scope=scope,
                source_type_hint=exc.manifest.source_type
                or "static_html_linear",
                reason=known_gap_reason + f" [pause: {msg[:140]}]",
                out_dir=out_dir,
            )
        return {
            "slug": slug,
            "outcome": "paused",
            "reason": msg[:200],
            "manifest": str(out_dir / "manifest.json"),
        }
    except Exception as exc:  # noqa: BLE001
        msg = f"{type(exc).__name__}: {exc}"
        # URL-based static HTML may return an HTTP error on Cloudflare
        # challenge before a pause fires; accept that as a known gap
        # when documented.
        if known_gap_reason is not None:
            shutil.rmtree(out_dir)
            source_type_hint = "static_html_linear"
            if "js_rendered" in (detection_override.source_type if detection_override else ""):
                source_type_hint = "js_rendered_progressive_disclosure"
            return _write_unavailable_manifest(
                slug=slug,
                label=label,
                scope=scope,
                source_type_hint=source_type_hint,
                reason=known_gap_reason + f" [error: {msg[:140]}]",
                out_dir=out_dir,
            )
        return {"slug": slug, "outcome": "error", "reason": msg[:200]}

    # Extraction may return empty content when a JS source silently
    # degrades to a bot-detection shell (NZ Curriculum, 2026-04-18) or
    # when a Cloudflare challenge page renders but does not match the
    # challenge-marker taxonomy. Treat empty content on a known-gapped
    # source as raw-content-unavailable and rewrite the manifest.
    empty_content_hash = (
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
    if m.content_hash == empty_content_hash and known_gap_reason is not None:
        shutil.rmtree(out_dir)
        return _write_unavailable_manifest(
            slug=slug,
            label=label,
            scope=scope,
            source_type_hint=m.source_type,
            reason=(
                known_gap_reason
                + " [extraction returned empty content — source appears "
                "to be serving a bot-detection shell rather than real "
                "curriculum content]"
            ),
            out_dir=out_dir,
        )

    raw_files = [rcf.model_dump() for rcf in m.raw_content_files]
    return {
        "slug": slug,
        "outcome": "ok",
        "content_hash": m.content_hash,
        "source_type": m.source_type,
        "raw_content_files": raw_files,
        "manifest": str(out_dir / "manifest.json"),
    }


def main() -> int:
    preflight = _preflight()
    summary = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "preflight": preflight,
        "artefacts": [],
    }
    for case in CASES:
        entry = _run_one(case)
        summary["artefacts"].append(entry)
        print(
            f"[{entry['outcome']}] {case['label']}"
            + (f"  content_hash={entry.get('content_hash')}" if entry.get("content_hash") else "")
        )
        if entry.get("outcome") == "unavailable":
            print(f"    reason: {entry['reason']}")

    summary_path = REPO / "docs/project-log/phase0-4a4-5-regeneration-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nSummary written to {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
