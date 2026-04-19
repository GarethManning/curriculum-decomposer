# STATE.md discipline

`STATE.md` at the repo root is a live state register. It exists to answer, in under a minute, the questions a future session asks when it starts: what was done last, what is verified to work, what is verified to be broken, what is claimed but unverified, what is next, and what decisions are outstanding. It is deliberately narrow. It is not the forward-looking plan — that lives at `docs/plans/curriculum-harness-remaining-build-plan-v3.md` and tells sessions what to build and why. It is not the historical log — that lives at `docs/project-log/harness-log.md` and narrates what each session did in detail. `STATE.md` carries only the current snapshot, and it must be kept tight enough to stay scannable.

It gets updated at the end of every Claude Code session, before the session closes. The session that just finished doing the work is the session that knows most reliably what changed; waiting to update later means drift. If a session closes without the update, the next session should treat the file as stale and reconcile before proceeding (see below).

A session operator can paste the following brief at the end of any Claude Code session to produce the update:

> Before closing this session, update `STATE.md`. Read it, then:
>
> 1. Replace section 1 (*Last session*) with this session's ID, date, head commit hash after this session's commits, and a one-paragraph summary of what was done.
> 2. Update section 2 (*Verified working*) to add anything this session shipped that is verifiable from the repo, with file path or commit hash citations. Remove entries that are no longer accurate.
> 3. Update section 3 (*Verified broken*) to remove anything this session fixed, and add any new defects discovered, with file paths and line numbers.
> 4. Update section 4 (*Unverified*) to reflect anything claimed but not verifiable under a read-only audit.
> 5. Update section 5 (*Next session*) to reflect the next session from `docs/plans/curriculum-harness-remaining-build-plan-v3.md`, including which artefacts it produces and which model to use.
> 6. Update section 6 (*Open questions*) with anything awaiting human decision. If none, leave the section empty — do not delete the header.
>
> Keep the whole file under one page. Commit as `[docs] STATE.md — <session ID> close` on its own commit at the end of the session.

If `STATE.md` looks stale at session start — for example the last-session entry does not match the actual git head, or a listed broken item turns out to already be fixed — run a read-only audit against it before doing any other work. The audit template is `docs/audits/state-audit-2026-04-19-v1.md`; produce a new dated audit file, reconcile `STATE.md` against the audit, and commit the reconciliation before opening the next session's work.

`STATE.md` replaces the "first action for next session" lists that used to sit at the top of the build plan. The v3 build plan does not carry those. Pick up the next session from `STATE.md` section 5.
