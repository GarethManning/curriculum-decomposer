# Curriculum Harness — Claude Code Entry Point

Read these files before doing anything else in this repo, in this order:

1. `STATE.md` — current build state, what is done, what is next, what is broken
2. `PROMPT_STANDARDS.md` — invariant rules that apply to every session

## Gate discipline

No downstream artefact is built until the upstream artefact has passed a panel review gate with human sign-off. Gate steps are marked [GATE] in STATE.md section 5. Do not proceed past a gate without explicit human confirmation in the session.

## Current priority

See STATE.md section 5 for the active next session. Do not start work on any other track until that section says it is complete.

## Key paths

- Reference corpus: `docs/reference-corpus/`
- REAL wellbeing artefacts: `docs/reference-corpus/real-wellbeing/`
- Crosswalks: `docs/reference-corpus/crosswalks/`
- Validity gates: `scripts/validity-gate/`
- Build scripts: `scripts/`
