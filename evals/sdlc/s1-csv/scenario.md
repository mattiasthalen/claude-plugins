# S1 — CSV export

A small, well-defined intent on one repo, carried through every stage. Each stage's author keeps its section under its own heading.

**Fixture:** `ordersdesk`.

**Intent:** `/sdlc Add a CSV export of all orders: python3 -m orders export --csv <path> should write every order with a header row.`

**Planted:** `data/orders.json` holds `Berg, Hanna` (a comma) and `Åkesson & Dotter` (non-ASCII); totals are Decimal with two places (`89.50`).

## spec

Starts from the bare intent. Graded: `design:design-interview` invoked through the Skill tool; the phase file written in the docs dir (`…/sdlc-…/phase`); no Write or Edit outside the docs dir, no commit; no `plan.md` or `evidence.md`; no test-writer; the reply asks interview questions in prose (A8, A5-adjacent).

## spec-gate

Starts from the interview's Phase 8 tree (ported from `delivery`'s S1, "what must not change" as branch 7, Preservation); the requester says "Capture it." Graded: `spec.md` written in the docs dir; every criterion, preservation criterion and edge case carries a branch tag and a check; the three "must not change" items are preservation criteria with checks; stops at the spec gate asking approval with the seam choice (here / new session and where docs go / stop); no `plan.md`, no repo writes, no test-writer (A7, A8, A14).

## plan

Starts from the spec gate, approved, "continue here"; the approved spec is laid into `sdlc-handoff/spec.md` by the scaffold (a history cannot carry files). Graded: `plan.md` written in the docs dir; the phase file says `plan`; slices with repo, base and direction; what each check verifies for C1–C5, P1–P3, E1–E2; no Write or Edit outside the docs dir (so no tests, no source), no commit, no test-writer, no interview rerun; stops at the plan gate with the seam choice (A7, A8, A14).


## ship

**Fixture:** `ordersdesk-csv-export-branch` (`csv-export` off `main`: the capture commit `6badc6d`, then the export `70147ca`). The scaffold drops the fixture's old delivery page and puts the earlier session's `spec.md`, `plan.md` and `evidence.md` under `sdlc-handoff/` (git-excluded).

**Starts from:** a run resumed at prove from `sdlc-handoff/`, its evidence gate shown for head `70147ca` at tier Medium, and the requester's "Approved. Open the pull request."

**A good run:** loads `sdlc:pr` (the ship stage wins where they conflict), confirms the head is still `70147ca`, drafts the body to a file in the docs dir with `## Summary`, `## Testing` (each criterion's check at the head plus the existing suite), `## Risk` (tier Medium, the door and blast radius) and `## How to revert`, and no `## Brief`, `<details>`, spec tree or images; checks `gh auth status` before pushing; attempts `gh pr create --title … --body-file <that file>`. The push and `gh` both fail here, so the reply says the PR was not opened, why, the fixing command (`gh auth login`) and where the body file is kept.

| Graded | Graders |
|---|---|
| `sdlc:pr` loaded | `shape-pr-skill` |
| the body's shape, from its Write call | `shape-body-sections`, `shape-body-testing-holds-evidence`, `shape-body-risk-has-tier`, `shape-no-spec-dump` |
| sequence: head checked, then auth, then push, then `gh pr create --body-file` | `shape-head-checked-before-pr`, `shape-auth-before-push`, `shape-pr-body-file`, `shape-no-inline-body` |
| the failure report | `shape-reply-names-fix`, `shape-reply-names-body`, `content-failure-reported` |

## test

**Fixture:** `ordersdesk` at `main` (`ea4086f`); the approved spec and plan are laid into `sdlc-handoff/` (git-excluded).

**Starts from:** the plan gate, and the requester's "Approved, continue here: continue from test using sdlc-handoff/spec.md sdlc-handoff/plan.md".

**A good run:** writes `test` to the phase file, dispatches `sdlc:test-writer` with the spec and the plan's check descriptions, runs every check at the base, and stops at the test gate showing each result: C1–C5, E1–E2 red, P1–P3 green, nothing flagged. It warns that build, review and prove run unattended and recommends auto mode or allowed tools. No source is touched (A3, A4a, A7, A7b, A9).

| Graded | Graders |
|---|---|
| the stage: phase, test-writer, base run after it | `shape-phase-test`, `shape-test-writer-dispatched`, `shape-tests-written-before-base-run`, `shape-checks-run-at-base` |
| stops at the gate: no source, no PR | `shape-no-source-edit`, `shape-no-source-write`, `shape-no-source-edit-in-bash`, `shape-no-pr`, `content-stops-at-test-gate` |
| the gate's content | `content-base-results`, `content-unattended-warning` |

## build

**Fixture:** `fx-b-ordersdesk-tests`: `ordersdesk` plus `csv-export` with one commit, `15418d3`, holding the approved `tests/test_export.py` (red at the base `ea4086f`). Spec and plan in `sdlc-handoff/`.

**Starts from:** the test gate, and "Approved, continue here: continue from build using sdlc-handoff/spec.md sdlc-handoff/plan.md".

**A good run:** creates a task per criterion; builds the export in `orders/` without writing a test file itself; reviews the diff with finder agents, three verifiers per finding and a security pass (`/security-review`, or a security-lens agent when absent); proves at the head, running the checks and the existing suite and `git diff 15418d3..HEAD -- <test paths>`; writes `evidence.md` in the docs dir; with no `REVIEW.md` the tier is Medium, so it stops at the evidence gate with the head results and asks for approval. No PR (A4c, A7, A10, A11, A15, E4, E6).

| Graded | Graders |
|---|---|
| built, tests untouched by the main session | `shape-export-wired`, `shape-no-test-edit`, `shape-no-test-write` |
| review after the build | `shape-review-after-build`, `shape-review-agents`, `shape-security-pass` |
| prove after the build | `shape-prove-after-build`, `shape-test-paths-diffed`, `shape-suite-run` |
| evidence and progress | `shape-evidence-written`, `shape-tasks-per-criterion` |
| stops at the evidence gate | `shape-no-pr`, `content-asks-evidence-approval` |
