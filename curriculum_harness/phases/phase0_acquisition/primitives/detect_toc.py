"""Table-of-contents detection for PDFs (Session 4a-2b Step 7).

Three-tier fallback, deterministic, no model calls:

1. **Embedded outline.** Read the PDF's outline / bookmark tree via
   pypdf. Walk the tree, yielding ``{title, page_number, depth}`` per
   entry. AODA-compliant PDFs occasionally carry both a standard
   reader outline (`/Outlines`) and a semantic structure tree
   (`/StructTreeRoot`) used by screen readers; when both are present
   the primitive tags the primary outline as ``embedded_outline`` and
   records the presence of the structure tree in the detection trace
   (``struct_tree_present``). Downstream consumers can choose which
   to use.

2. **TOC-page heuristic.** When no embedded outline is present, scan
   the first ``toc_page_scan_limit`` pages for a page titled
   ``Contents`` / ``Table of Contents`` (case-insensitive). On
   candidate pages, parse lines matching the leader pattern
   ``title..........page_number``.

3. **Heading-structure inference.** Last-resort fallback. Extract
   every page, classify lines by font size from ``page.chars`` — a
   line whose predominant char-height is materially larger than the
   body median is tentatively a heading. Entries are flagged as
   ``inferred`` with lower confidence.

On total failure the primitive returns an empty entries list and a
structured ``detection_reason``. The primitive never raises on a
detection miss; extraction downstream handles the
absence via scope validation.

Output: passes through the input PDF bytes unchanged. ``meta`` carries
``toc_entries`` and ``toc_detection_method``. ``summary`` carries the
same plus a short sample for the acquisition trace.
"""

from __future__ import annotations

import io
import re
from collections import Counter
from typing import Any

from curriculum_harness.phases.phase0_acquisition.primitives.base import (
    PrimitiveResult,
    ScopeValidationError,
)


_TOC_HEADER_RX = re.compile(r"(?i)\b(table\s+of\s+contents|contents)\b")
_TOC_LEADER_RX = re.compile(
    r"^(?P<title>.+?)\s*\.{3,}\s*(?P<page>\d+)\s*$"
)
_TOC_TRAILING_PAGE_RX = re.compile(
    r"^(?P<title>.{3,}?)\s{2,}(?P<page>\d+)\s*$"
)


def _walk_outline(reader, items, depth: int = 0, out: list | None = None) -> list:
    if out is None:
        out = []
    for it in items:
        if isinstance(it, list):
            _walk_outline(reader, it, depth + 1, out)
            continue
        try:
            title = str(it.title).strip()
        except Exception:  # noqa: BLE001
            title = ""
        if not title:
            continue
        try:
            page_num = reader.get_destination_page_number(it)
        except Exception:  # noqa: BLE001
            continue
        out.append(
            {
                "title": title,
                "page_number": int(page_num) + 1,  # 1-indexed for consumers
                "depth": depth,
                "source": "embedded_outline",
            }
        )
    return out


def _parse_toc_pages(pdf, toc_page_scan_limit: int) -> tuple[list, int | None]:
    """Tier 2: find a TOC page and parse its leader lines."""

    n_pages = len(pdf.pages)
    scan_n = min(toc_page_scan_limit, n_pages)
    toc_page_index = None
    for i in range(scan_n):
        text = pdf.pages[i].extract_text() or ""
        head = "\n".join(text.splitlines()[:10]).lower()
        if _TOC_HEADER_RX.search(head):
            toc_page_index = i
            break
    if toc_page_index is None:
        return [], None

    entries: list[dict] = []
    # Treat contiguous pages starting at toc_page_index as candidate TOC pages
    for i in range(toc_page_index, min(toc_page_index + 6, n_pages)):
        text = pdf.pages[i].extract_text() or ""
        found_any = False
        for line in text.splitlines():
            line = line.strip()
            m = _TOC_LEADER_RX.match(line)
            if not m:
                m = _TOC_TRAILING_PAGE_RX.match(line)
            if not m:
                continue
            title = m.group("title").strip()
            page = int(m.group("page"))
            if not title:
                continue
            entries.append(
                {
                    "title": title,
                    "page_number": page,
                    "depth": 0,
                    "source": "toc_page_heuristic",
                }
            )
            found_any = True
        if not found_any and i > toc_page_index:
            break
    return entries, toc_page_index + 1


def _infer_from_headings(pdf, max_pages: int) -> list:
    """Tier 3: classify lines by font-height and declare likely headings."""
    # Sample per-char heights across the whole document (bounded).
    heights: list[float] = []
    page_cap = min(len(pdf.pages), max_pages)
    for i in range(page_cap):
        page = pdf.pages[i]
        for c in page.chars:
            h = c.get("size") or c.get("height")
            if isinstance(h, (int, float)):
                heights.append(float(h))
    if not heights:
        return []
    # Approx mode = body text height
    rounded = [round(h, 1) for h in heights]
    body_size, _ = Counter(rounded).most_common(1)[0]
    heading_threshold = body_size * 1.35

    entries: list[dict] = []
    for i in range(page_cap):
        page = pdf.pages[i]
        # Group chars by rounded top; compute max size per line.
        lines: dict[int, list[dict]] = {}
        for c in page.chars:
            t = int(round(c.get("top", 0)))
            lines.setdefault(t, []).append(c)
        for top_y in sorted(lines):
            chars = lines[top_y]
            text = "".join(
                c.get("text", "") for c in sorted(chars, key=lambda c: c.get("x0", 0))
            ).strip()
            if not text or len(text) > 120:
                continue
            max_size = max(
                float(c.get("size", 0) or c.get("height", 0) or 0) for c in chars
            )
            if max_size >= heading_threshold and text:
                entries.append(
                    {
                        "title": text,
                        "page_number": i + 1,
                        "depth": 0,
                        "source": "heading_inference",
                        "font_size": round(max_size, 2),
                    }
                )
    return entries


class DetectTocPrimitive:
    """Three-tier TOC detection primitive. Deterministic, no model calls.

    Pass-through: the PDF bytes flow unchanged to the next primitive.
    Emits ``meta['toc']`` with:

    - ``entries``: list of ``{title, page_number, depth, source}``.
    - ``detection_method``: ``embedded_outline`` / ``toc_page_heuristic``
      / ``heading_inference`` / ``none``.
    - ``detection_reason``: set when ``detection_method == 'none'``.
    - ``struct_tree_present``: AODA accessibility structure detected
      (informational only; not parsed).
    """

    name = "detect_toc"
    required_scope_fields: tuple[str, ...] = ()
    optional_scope_fields: tuple[str, ...] = ()
    side_effects: frozenset[str] = frozenset()

    def __init__(
        self,
        *,
        toc_page_scan_limit: int = 20,
        heading_inference_page_cap: int = 60,
    ) -> None:
        self.toc_page_scan_limit = toc_page_scan_limit
        self.heading_inference_page_cap = heading_inference_page_cap

    def validate_scope(self, scope) -> None:
        return None

    def run(self, scope, previous: PrimitiveResult | None) -> PrimitiveResult:
        if previous is None or previous.output is None:
            raise ScopeValidationError(
                self.name, ["source_reference"], "detect_toc expects PDF bytes"
            )
        data = previous.output
        if not isinstance(data, (bytes, bytearray)):
            raise ValueError(
                "detect_toc expected PDF bytes from previous primitive"
            )

        # Tier 1: embedded outline via pypdf.
        entries: list[dict] = []
        detection_method = "none"
        detection_reason: str | None = None
        struct_tree_present = False
        try:
            import pypdf

            reader = pypdf.PdfReader(io.BytesIO(bytes(data)))
            try:
                root = reader.trailer.get("/Root")
                if root is not None:
                    root_obj = root.get_object()
                    struct_tree_present = "/StructTreeRoot" in root_obj
            except Exception:  # noqa: BLE001 — best-effort probe
                struct_tree_present = False
            outline_items = reader.outline
            if outline_items:
                entries = _walk_outline(reader, outline_items)
                if entries:
                    detection_method = "embedded_outline"
        except Exception as exc:  # noqa: BLE001
            detection_reason = f"pypdf_open_failed: {exc}"

        # Tier 2: TOC page heuristic if tier 1 yielded nothing.
        toc_page_no: int | None = None
        if not entries:
            try:
                import pdfplumber

                with pdfplumber.open(io.BytesIO(bytes(data))) as pdf:
                    entries, toc_page_no = _parse_toc_pages(
                        pdf, self.toc_page_scan_limit
                    )
                    if entries:
                        detection_method = "toc_page_heuristic"
                    elif detection_method == "none":
                        detection_reason = detection_reason or "no_toc_page"
            except Exception as exc:  # noqa: BLE001
                detection_reason = detection_reason or (
                    f"toc_page_scan_failed: {exc}"
                )

        # Tier 3: heading-structure inference.
        if not entries:
            try:
                import pdfplumber

                with pdfplumber.open(io.BytesIO(bytes(data))) as pdf:
                    entries = _infer_from_headings(
                        pdf, self.heading_inference_page_cap
                    )
                    if entries:
                        detection_method = "heading_inference"
                    elif detection_method == "none":
                        detection_reason = (
                            detection_reason or "no_heading_structure"
                        )
            except Exception as exc:  # noqa: BLE001
                detection_reason = detection_reason or (
                    f"heading_inference_failed: {exc}"
                )

        toc_payload: dict[str, Any] = {
            "entries": entries,
            "detection_method": detection_method,
            "struct_tree_present": struct_tree_present,
        }
        if detection_reason is not None:
            toc_payload["detection_reason"] = detection_reason
        if toc_page_no is not None:
            toc_payload["toc_page_number"] = toc_page_no

        # Summary: trace-only small snapshot.
        summary = {
            "status": "ok" if entries else "no_toc_detected",
            "detection_method": detection_method,
            "entries_count": len(entries),
            "struct_tree_present": struct_tree_present,
            "sample_entries": entries[:5],
        }
        if toc_page_no is not None:
            summary["toc_page_number"] = toc_page_no
        if detection_reason:
            summary["detection_reason"] = detection_reason

        return PrimitiveResult(
            output=data,
            summary=summary,
            meta={"toc": toc_payload},
        )
