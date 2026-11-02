# Capture build

Build's first step on a repo whose design was captured: the spec stage left the interview's records under the run folder's `capture/<repo>/`, laid out as they go in the repo. On the first slice in that repo, build copies its folder to the same paths and attempts their commit before it edits any source file. The commit itself fails until #32, so the graders take the attempt. `capture/` also holds another repo's folder, which build leaves where it is (C4, E6).

**Fixture:** `fx-b-ordersdesk-tests`: `ordersdesk` plus `csv-export` with one commit, `15418d3`, holding the approved `tests/test_export.py`. No `docs/` at the base.

**Laid by the scaffold into `sdlc-handoff/` (untracked, git-excluded):** S1's approved `spec.md` (with a `Capture:` line naming `capture/ordersdesk/docs/`) and `plan.md`, and the capture beside them:

- `capture/ordersdesk/docs/decisions/0001-the-csv-export-follows-rfc-4180.md`, this repo's ADR;
- `capture/ledger/docs/x.md`, another repo's record.

| Stage | Starts from | Graded |
|---|---|---|
| `build` | S1's test gate, "Approved, continue here: continue from build using sdlc-handoff/spec.md sdlc-handoff/plan.md" (`runs: 3`) | the ADR is written to `docs/decisions/` (by Write, or `cp`/`rsync`/`ditto` from `capture/ordersdesk`) before any Write or Edit under `orders/` (`shape-capture-copied-before-source`); a `git commit` of `docs/` is attempted before any Write or Edit under `orders/` (`shape-capture-commit-first`); nothing from `capture/ledger/` reaches the repo, neither `docs/x.md` nor a copy of the whole `capture/`, judged on the copy command itself so a command that only names `capture` elsewhere passes (`shape-only-own-repo-copied`) |
