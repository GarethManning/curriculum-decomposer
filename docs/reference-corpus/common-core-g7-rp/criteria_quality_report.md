# Criterion quality report — 2a-regression-common-core-7rp

**Overall:** HALTED
**Halted by:** `criterion_gates`

## Summary

- **rubrics_total:** 7
- **rubrics_halted_lts:** 1
- **rubrics_with_gate_failures:** 1
- **rubrics_competent_judge_fail:** 0
- **rubrics_propositional_thin_flag:** 2
- **stability_distribution:** rubric_unstable=3, stable=4

## Per-LT gate results

### `cluster_01_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand, with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_02_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand, with no hedging language or framing of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_02_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently at the LT's level of demand, using no hedging language and standing alone as a verdict that the LT is met.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: verb-bucket diversity across applied levels — no thin flag

### `cluster_03_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares the capability as demonstrated independently and accurately across all required contexts, standing alone as evidence the LT is met without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_03_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent capability to use the constant of proportionality to write equations and interpret ordered pairs accurately, which directly matches the LT's demand and stands alone as success.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional_lt_rubric_thin: all four applied levels share one verb bucket; structurally valid but differentiation may be thin (reviewer-confirm)

### `cluster_04_lt_01`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — FAIL (halts): adjacent level pairs with no topic-lemma overlap: [('emerging', 'developing')]
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent, accurate solving of multistep ratio and percent problems at the level specified in the LT, with no hedging language or implication of incompleteness.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

### `cluster_04_lt_02`

- **word_limit** — PASS: all five levels within their respective word limits
- **observable_verb** — PASS: every level (except no_evidence) contains an observable action verb
- **single_construct** — PASS: adjacent applied levels share topic-lemma overlap — single construct preserved
- **no_inline_examples** — PASS: no inline examples or banned substrings in any descriptor
- **competent_framing_regex** — PASS: Competent descriptor contains no deficit hedge-phrases
- **competent_framing_judge** — PASS: LLM-as-judge verdict: pass — The descriptor declares independent application of proportional relationships to multistep problems with accurate reasoning, which directly matches the LT's demand and stands alone as success without hedging or incompleteness language.
- **level_progression** — PASS: adjacent levels preserve progression roles
- **propositional_thin_flag** — PASS: propositional-thin check skipped (not Type 1)

