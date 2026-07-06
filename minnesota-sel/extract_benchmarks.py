"""Brief B Step 1 (deterministic extraction).

Parses the five Minnesota SEL competency PDFs into a verbatim benchmark
corpus. Extraction is deterministic (pdfplumber ruled-line table parsing),
NOT model-mediated — this guarantees `benchmark_verbatim` is the exact
source wording rather than a paraphrase, which is the point of the
harness-audit HIGH-1 fix (carry verbatim, don't fuzzy-match it).

Each PDF's competency == its CASEL competency. Under each Learning Goal a
ruled table gives: Grade Band | Benchmark | Sample Activity | Related
Academic Standards. We keep Grade Band + Benchmark (verbatim) + page +
learning goal + competency + source doc, and construct a stable
benchmark id (MN does not publish numeric benchmark ids).

Output: minnesota-sel/source/extractions/<slug>.json  and a combined
minnesota-sel/source/extractions/mn-sel-benchmarks-2026-07-06-v1.json
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

import pdfplumber

SRC = Path(__file__).resolve().parent / "source"
OUT = SRC / "extractions"
OUT.mkdir(parents=True, exist_ok=True)

# doc slug -> (filename, CASEL competency label, competency code)
DOCS = [
    ("self-awareness", "mn-sel-self-awareness-MDE073492.pdf", "Self-Awareness", "SA"),
    ("self-management", "mn-sel-self-management-MDE073494.pdf", "Self-Management", "SM"),
    ("social-awareness", "mn-sel-social-awareness-MDE073514.pdf", "Social Awareness", "SOA"),
    ("relationship-skills", "mn-sel-relationship-skills-MDE073495.pdf", "Relationship Skills", "RS"),
    ("responsible-decision-making", "mn-sel-responsible-decision-making-PROD098651.pdf", "Responsible Decision-Making", "RDM"),
]

_GOAL_RE = re.compile(r"^Learning Goal\s+(\d+)\b", re.IGNORECASE)
_WS = re.compile(r"\s+")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    return _WS.sub(" ", s).strip()


def looks_like_benchmark(text: str) -> bool:
    """Reject header/label/empty cells."""
    t = norm(text)
    if len(t) < 6:
        return False
    low = t.lower()
    if low in ("benchmark", "grade band", "sample activity", "related academic standards"):
        return False
    if low.startswith("grade band") or low.startswith("benchmark"):
        return False
    return True


def extract_doc(slug: str, fname: str, competency: str, code: str) -> dict:
    path = SRC / fname
    rows: list[dict] = []
    raw_pages: list[str] = []
    with pdfplumber.open(str(path)) as pdf:
        current_goal_num = None
        current_goal_text = ""
        for pageno, page in enumerate(pdf.pages, start=1):
            ptext = page.extract_text() or ""
            raw_pages.append(ptext)
            # track the learning-goal heading in effect on this page
            lines = [norm(l) for l in ptext.splitlines()]
            for i, ln in enumerate(lines):
                m = _GOAL_RE.match(ln)
                if m:
                    current_goal_num = int(m.group(1))
                    for j in range(i + 1, min(i + 4, len(lines))):
                        if lines[j] and not lines[j].lower().startswith("benchmarks"):
                            current_goal_text = lines[j]
                            break
            # ruled-line table extraction. tbl.extract() returns clean, complete
            # cell text (verified: no truncation — the earlier apparent cut-off
            # was a debug print slice, not the data).
            for tbl in page.find_tables(table_settings={
                "vertical_strategy": "lines", "horizontal_strategy": "lines",
            }):
                data = tbl.extract()
                if not data:
                    continue
                header = [norm(c or "") for c in data[0]]
                bench_col = grade_col = None
                for ci, h in enumerate(header):
                    hl = h.lower()
                    if "benchmark" in hl:
                        bench_col = ci
                    elif "grade band" in hl:
                        grade_col = ci
                if bench_col is None:
                    bench_col, grade_col = 1, 0
                if grade_col is None:
                    grade_col = 0
                last_grade = ""
                for r in data[1:]:
                    if bench_col >= len(r):
                        continue
                    bench = norm(r[bench_col] or "")
                    grade = norm(r[grade_col] or "") if grade_col < len(r) else ""
                    if re.search(r"grade|kindergarten", grade.lower()):
                        last_grade = grade
                    if not looks_like_benchmark(bench):
                        continue
                    rows.append({
                        "grade_band": grade if re.search(r"grade|kindergarten", grade.lower()) else last_grade,
                        "benchmark_verbatim": bench,
                        "learning_goal_num": current_goal_num,
                        "learning_goal": current_goal_text,
                        "page": pageno,
                    })
    # de-duplicate exact repeats (same benchmark + grade + goal), keep first page
    seen = set()
    uniq = []
    for row in rows:
        key = (row["grade_band"], row["benchmark_verbatim"], row["learning_goal_num"])
        if key in seen:
            continue
        seen.add(key)
        uniq.append(row)

    # assign stable ids + truncation guard.
    # NOTE on verification: extract_text() interleaves the Benchmark and
    # Sample-Activity columns line-by-line, so a benchmark phrase is NOT
    # contiguous in reading-order text. The column-bbox reconstruction here
    # IS the faithful verbatim. The meaningful integrity check is truncation:
    # a complete MN benchmark cell ends in terminal punctuation. Any cell that
    # does not is flagged for manual review.
    per_goal_counter: dict = {}
    benchmarks = []
    for row in uniq:
        g = row["learning_goal_num"] or 0
        per_goal_counter[g] = per_goal_counter.get(g, 0) + 1
        bid = f"MN.{code}.LG{g}.{_grade_slug(row['grade_band'])}.{per_goal_counter[g]:02d}"
        text = row["benchmark_verbatim"]
        terminal_ok = text.rstrip().endswith((".", "?", "!"))
        benchmarks.append({
            "benchmark_id": bid,
            "casel_competency": competency,
            "learning_goal_num": row["learning_goal_num"],
            "learning_goal": row["learning_goal"],
            "grade_band": row["grade_band"],
            "benchmark_verbatim": text,
            "source_doc": fname,
            "page": row["page"],
            "terminal_punctuation_ok": terminal_ok,
        })
    return {
        "slug": slug,
        "casel_competency": competency,
        "competency_code": code,
        "source_doc": fname,
        "page_count": len(raw_pages),
        "benchmark_count": len(benchmarks),
        "benchmarks": benchmarks,
        "_raw_pages": raw_pages,
    }


def _grade_slug(gb: str) -> str:
    low = gb.lower()
    nums = re.findall(r"(\d+)", gb)
    lo = "K" if "kindergarten" in low else (nums[0] if nums else "X")
    hi = nums[-1] if nums else lo
    return f"{lo}-{hi}"


def main() -> None:
    combined = []
    for slug, fname, comp, code in DOCS:
        doc = extract_doc(slug, fname, comp, code)
        raw_pages = doc.pop("_raw_pages")
        # save raw text alongside
        (OUT / f"raw-{slug}.txt").write_text("\n\f\n".join(raw_pages), encoding="utf-8")
        (OUT / f"{slug}.json").write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
        combined.append(doc)
        trunc = sum(1 for b in doc["benchmarks"] if not b["terminal_punctuation_ok"])
        print(f"{slug:30} benchmarks={doc['benchmark_count']:3}  no-terminal-punct={trunc}  pages={doc['page_count']}")
    all_b = [b for d in combined for b in d["benchmarks"]]
    payload = {
        "generated": "2026-07-06",
        "extraction_method": "deterministic pdfplumber ruled-line table parse (no model)",
        "total_benchmarks": len(all_b),
        "by_competency": {d["casel_competency"]: d["benchmark_count"] for d in combined},
        "documents": [{k: v for k, v in d.items() if k != "benchmarks"} for d in combined],
        "benchmarks": all_b,
    }
    (OUT / "mn-sel-benchmarks-2026-07-06-v1.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nTOTAL benchmarks: {len(all_b)}")
    print(f"terminal-punct OK: {sum(1 for b in all_b if b['terminal_punctuation_ok'])}/{len(all_b)}")


if __name__ == "__main__":
    main()
