"""Prompts for competency clustering.

The LT authoring skill says 2-3 LTs per competency. A competency
cluster groups KUD items that together form ONE coherent capability
the learner is expected to develop. Clustering applies the LT skill's
decomposition logic in reverse: items that would plausibly decompose
FROM the same competency belong together.

For prose dispositional sources like Welsh CfW, the natural cluster
boundary is the source's top-level organising claim — each Statement
of What Matters is one coherent capability, and the supporting
propositional/orientation content inside that Statement decomposes
back into the same cluster. The classifier does not invent new
boundaries: it recovers the source's own organising structure.
"""

from __future__ import annotations

SYSTEM_PROMPT = """You cluster KUD items into competencies for a reference-authoring pipeline. You apply the Learning Target authoring skill's decomposition logic in reverse: items that would plausibly decompose FROM the same competency belong together.

A COMPETENCY is ONE coherent capability a learner is expected to develop. The LT authoring skill says 2-3 LTs per competency.

CLUSTERING LOGIC — APPLY IN ORDER

1. Use the source's organising structure as the primary cluster boundary. Prose sources (e.g. Welsh CfW Statements of What Matters, Ontario Big Ideas, Common Core cluster headings) have top-level organising claims that each name ONE coherent capability. Detect these boundaries from:
   - Explicit section headings visible in heading_path or block_type=heading.
   - Lead "fundamental claim" bullets (sentences of the form "X has lifelong benefits", "How we Y affects Z", "X is fundamental to Y") — these signal the start of a new top-level capability, and the bullets that follow them elaborate the same capability until the next fundamental claim.
   Use these as the cluster boundaries — do not invent finer-grained or broader groupings than the source supports.

2. Inside a source section, knowledge-type coherence is a SECONDARY grouping signal. If a section bundles propositional content (Type 1), occasion-triggered skills (Type 2), and a sustained orientation (Type 3) in service of ONE overarching capability, those items belong to the SAME competency. The section-level grouping takes precedence over type-level splitting — a competency may span multiple knowledge types.

3. Sub-themes within a section belong to the SAME cluster. If one item describes positive formation (e.g. "forming healthy relationships") and another describes recognition or remediation within the same topic (e.g. "recognising unhealthy relationships"), they belong to the same cluster — they are different LTs within the same competency, not different competencies.

4. Competency grain. A competency typically contains 4-8 KUD items (LT skill: 2-3 LTs per competency, 1-3 KUD items per LT). A cluster of 1-2 items is usually a sign that you have over-split — merge into a broader cluster. A cluster of >10 items is usually a sign that you have under-split — but only split if there is a clear section boundary in the source.

5. Name each competency in a brief noun-phrase style (Title Case) describing the overall capability.

6. Define each competency as ONE sentence beginning "The ability to..." or "A sustained orientation toward..." (for predominantly dispositional competencies). Keep it under 25 words.

7. Assign a DOMINANT KNOWLEDGE TYPE to each competency based on which type predominates in the cluster. If a cluster is roughly half Type 1 and half Type 3, and the source claim is a sustained orientation, the dominant type is Type 3.

8. Prefer FEWER, broader clusters over many narrow ones when the choice is ambiguous. The pipeline's downstream stages (LT generation) split each competency into 2-3 LTs; fragmenting competencies produces an excessive LT count downstream.

NO LEFTOVERS — MANDATORY

Every KUD item in the input MUST be assigned to exactly one cluster. Items that do not obviously fit a section-level cluster still have a home: assign them to the cluster whose competency they most plausibly support. Do NOT leave items unassigned.

OUTPUT JSON SCHEMA — STRICT

Respond with ONE JSON object (no prose, no fences) with this exact shape:

{
  "clusters": [
    {
      "competency_name": "<Title Case noun phrase>",
      "competency_definition": "<one sentence, 'The ability to...' or 'A sustained orientation toward...' — under 25 words>",
      "dominant_knowledge_type": "Type 1" | "Type 2" | "Type 3",
      "kud_item_ids": ["<item_id>", ...],
      "source_section_label": "<short label naming which source claim this cluster maps to>"
    }
  ]
}

CONSTRAINTS

- Every input KUD item id appears in exactly one cluster.
- Clusters are ordered by the earliest source_block_id they contain (source order).
- Expect roughly one cluster per top-level source section. Do not over-split; do not under-merge.
- Do NOT invent KUD items. Only use item ids from the input.
"""


def build_user_prompt(
    *,
    source_slug: str,
    kud_items: list[dict],
    source_blocks: list[dict] | None = None,
) -> str:
    """Build the user prompt for a single clustering run.

    ``kud_items`` is a compact list of dicts, one per KUD item:
    { item_id, kud_column, knowledge_type, content_statement,
      source_block_id, source_line_start }.

    ``source_blocks`` (optional) is the verbatim source inventory
    (headings + non-heading blocks) used to expose the source's
    organising structure to the classifier. When provided, the prompt
    includes a full source-structure map so the classifier can anchor
    cluster boundaries to the source's section organisation rather
    than inferring them from the KUD items alone.
    """
    lines: list[str] = []
    lines.append(f"SOURCE: {source_slug}")
    lines.append("")
    if source_blocks:
        lines.append("SOURCE STRUCTURE (verbatim, with block_type and headings):")
        lines.append("")
        for b in source_blocks:
            marker = "##" if b.get("block_type") == "heading" else "- "
            heading = " > ".join(b.get("heading_path") or []) or "(root)"
            raw = (b.get("raw_text") or "").replace("\n", " ")
            lines.append(
                f"{marker} `{b.get('block_id')}` L{b.get('line_start', '?')} "
                f"[{b.get('block_type')}] ({heading}): {raw}"
            )
        lines.append("")
    lines.append(
        "KUD items to cluster (in source order):"
    )
    lines.append("")
    for it in kud_items:
        lines.append(
            "- id=`{item_id}` | {kt} | {col} | blk=`{blk}` | L{line} | {content}".format(
                item_id=it["item_id"],
                kt=it["knowledge_type"],
                col=it["kud_column"],
                blk=it["source_block_id"],
                line=it.get("source_line_start", "?"),
                content=(it["content_statement"] or "").replace("\n", " "),
            )
        )
    lines.append("")
    lines.append(
        "Cluster these items into competencies using the source's organising "
        "structure as the primary boundary. Every item must be assigned to "
        "exactly one cluster. Prefer FEWER, broader clusters when ambiguous. "
        "Emit ONE JSON object per the schema."
    )
    return "\n".join(lines)
