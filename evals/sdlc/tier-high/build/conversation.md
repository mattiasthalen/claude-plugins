## user
/sdlc Run CI on Python 3.12 as well as 3.11.

## assistant
The design interview is closed: 2 branches decided. Here is the spec, written to `$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/spec.md`. Nothing in the repo has changed.

- C1 — the CI matrix includes Python 3.12.
- Preservation criteria: P1 the matrix still includes 3.11; P2 the existing suite passes; P3 nothing but `.github/workflows/ci.yml` changes.

This is the spec gate: approve it, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
Approved, continue here.

## assistant
Here is the plan, written to `$TMPDIR/sdlc-00000000-0000-4000-8000-0000000000aa/plan.md`. One vertical slice on `ci-python-3-12` off `main`, one ready PR. Only `.github/workflows/ci.yml` is edited. Every check is a command in the spec, so the test stage writes no test file.

This is the plan gate: approve it, or tell me what to change. Then: continue here, continue in a new session, or stop?

## user
Approved, continue here.

## assistant
Every check is a command in the spec, so the test-writer wrote no test file. Here is each check at the base, `main` at `10cc306`:

| id | kind | base | expected |
|---|---|---|---|
| C1 | change | red (matrix is `["3.11"]`) | red |
| P1 | preservation | green | green |
| P2 | preservation | green (1 test) | green |
| P3 | preservation | green (no changes) | green |

Nothing is flagged. This is the test gate. After it, build, review and prove run unattended, so switch to auto mode or allow Bash, Edit, Write and Agent before you approve. Approve the tests, or tell me what to change. Then: continue here, continue in a new session, or stop?
