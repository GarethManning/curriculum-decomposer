# Curriculum Harness — Prompt Standards

*Read this file at the start of every Claude Code session that touches this repo.*

## Invariant rules — apply to every session

**No overwriting.** Never overwrite an existing file. Always write to a new versioned filename (e.g. criterion-bank-v3.json, not criterion-bank-v2.json). The one explicit exception is quality corrections to the current version where the session brief says "overwrite" and explains why — and even then, confirm before saving.

**Verify before reporting.** Never report a task as complete without running a verification command. For file moves: run `ls` on both old and new paths. For character counts: run `python3 -c "print(len('text'))"`. For JSON validity: run `python3 -c "import json; json.load(open('path'))"`. Self-reporting without verification is a failure.

**Description field character limit.** Skill description fields have a hard 250-character limit enforced by CI. After writing or editing any description field, run the character count check before committing. Count must be 250 or below.

**Registry and bundle steps are mandatory.** Every session that adds, moves, or modifies a skill must end with these steps in order — never skip any:
1. `python3 scripts/generate-registry.py`
2. Confirm count. Update `validate.yml` if count changed.
3. `cd mcp-server && npm run bundle-skills`
4. `cd ..`
5. `git add registry.json mcp-server/src/skills.json validate.yml`
6. Commit and push

**h2 Prompt sections.** Every skill's prompt section must use `## Prompt` (h2), never `# Prompt` (h1). A skill with an h1 Prompt header is invisible as a callable tool.

**School-agnostic outputs.** No skill output may reference any named school, programme, unit, or institution. Skills work from LT definitions and framework theory only.

## Criterion bank invariants

**Field order for competency_level_descriptors** — always in this exact order, no exceptions:
1. no_evidence
2. emerging
3. developing
4. competent
5. extending

**T3 entries do not have competency_level_descriptors.** T3 entries have: observation_indicators, confusable_behaviours, absence_indicators, conversation_prompts.

**criterion_statement for T2/T1** must capture the full cognitive demand of the KUD Do statement — not just the first clause.

**criterion_ids** are never reused or reordered. New entries continue from the highest existing ID.

**schema_version** on new or modified entries is always "v2" or higher.

**DAG validation must pass** before any criterion bank file is committed. Run the validation check and report the result.
