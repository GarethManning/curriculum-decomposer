"""Type 1/2 criterion (five-level rubric) generator.

Implemented in session 4b-4. Produces criterion-referenced five-level
rubrics (No Evidence / Emerging / Developing / Competent / Extending)
for Type 1 / Type 2 LTs, with typed prerequisite edges and a
Competent-as-success LLM-as-judge verdict. Type 3 LTs NEVER receive
rubrics — that routing is the observation-indicator generator's job.

Supporting components (co-construction plan, student rubric, feedback
guide) live in ``generate_supporting_components`` and attach to the
same LT. Quality gates live in
``curriculum_harness.reference_authoring.gates.criterion_gates``.
"""

from curriculum_harness.reference_authoring.criterion.generate_criteria import (
    generate_criteria,
    generate_criteria_sync,
)

__all__ = ["generate_criteria", "generate_criteria_sync"]
