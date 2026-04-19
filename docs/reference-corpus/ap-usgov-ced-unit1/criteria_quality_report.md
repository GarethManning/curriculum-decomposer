# Criterion quality report — 5-ap-usgov-ced-unit1

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 15
- **rubrics_halted_lts:** 11
- **rubrics_with_gate_failures:** 5
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 4
- **stability_distribution:** rubric_unstable=10, stable=5

## Per-LT gate results

### `cluster_02_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand, with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_04_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner 'identifies how' the specified limitations affected the Articles, which matches the LT's demand without hedging language or framing Competent as incomplete.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_04_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor directly states the learner 'explains how' the connection works, matching the LT's demand without hedging, incompleteness markers, or positioning it as a waystation to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_05_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the learner can identify and accurately describe major compromises and their structural outcomes, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_05_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated ('Explains how multiple specific compromises...') without hedging language, incompleteness markers, or positioning it as a way-station to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the learner as independently demonstrating the capability to identify, distinguish, and explain all three power types and their authority allocation—matching the LT's level of demand with no hedging language or incompleteness framing.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_07_lt_03`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated without hedging language, frames Competent as meeting the LT's demands (identify, compare, explain), and stands alone as success without implying incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_09_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent, accurate identification across different scenarios and contexts, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_09_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to describe how political elements operate across different scenarios and contexts accurately, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_10_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and at the LT's level of demand ('identifies and extracts...accurately'), with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_10_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['developing']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to explain connections between arguments and political frameworks at the level demanded by the LT, with no hedging language or implication of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_11_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent identification of multiple relevant political concepts without hedging language, incompleteness markers, or framing Competent as a stepping stone to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_12_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — FAIL (halts): levels without observable action verb: ['emerging', 'developing', 'competent', 'extending']
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated ('Articulates') at the target level without hedging, incompleteness language, or framing Competent as a stepping stone to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_13_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand without hedging language, incompleteness markers, or positioning it as a way-station to Extending.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_13_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('developing', 'competent'), ('competent', 'extending')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to identify and distinguish all required components without hedging language, implying the learning target is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

