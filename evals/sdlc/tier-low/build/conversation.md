## user
/sdlc In the README, say that `orders list` prints oldest first, and add a Development section that says how to run the tests.

## assistant
The design interview is closed: 3 branches decided. Here is the spec, written to `$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/spec.md`. Nothing in the repo has changed.

- C1 — the README says `orders list` prints oldest first.
- C2 — the README has a `## Development` section holding `python3 -m unittest discover -s tests`.
- Preservation criteria: P1 the existing suite passes; P2 nothing but `README.md` changes.

This is the spec gate: approve it, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
Approved, continue here.

## assistant
Here is the plan, written to `$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/plan.md`. One vertical slice on `readme-development` off `main`, one ready PR. Only `README.md` is edited. Every check is a command in the spec, so the test stage writes no test file.

This is the plan gate: approve it, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
Approved, continue here.

## assistant
Every check is a command in the spec, so the test-writer wrote no test file. Here is each check at the base, `main` at `10cc306`:

| id | kind | base | expected |
|---|---|---|---|
| C1 | change | red (no "oldest first") | red |
| C2 | change | red (no `## Development`) | red |
| P1 | preservation | green (1 test) | green |
| P2 | preservation | green (no changes) | green |

Nothing is flagged. This is the test gate. After it, build, review and prove run unattended, so switch to auto mode or allow Bash, Edit, Write and Agent before you approve. Approve the tests, or tell me what to change. Then: continue here, continue in a new session, or stop?
