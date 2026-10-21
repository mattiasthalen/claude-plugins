# ADR-0004 — Skill lines are earned by evals and ablation

**Status:** Superseded by [ADR-0012](0012-the-eval-gate-runs-in-session-and-stage-lines-start-empty.md) (2026-10-21)

## Context

A skill's lines cost context on every run, and a line written from intuition may change nothing. pitch-and-deliver earned each line against a failing eval and confirmed it by deletion, which worked but cost money and churn (about $1.5k in one pass) and froze its suite behind a hook. `claude plugin eval` runs staged cases with deterministic and judged graders.

## Decision

`delivering-pitches` starts empty. The suite in `evals/delivery/` runs against the empty skill first; a line enters only when a case fails without it. After the skill passes, `evals/delivery/tools/ablate.py` deletes each unit in turn and keeps it only if a grader drops below its bar. Cases are staged, resumed from fixed histories, and cover `delivery`'s own stages only. Five runs per case; deterministic graders 5/5, judged 4/5; an intermittent result is rerun at eight before it is trusted, and a grader that cannot hold its bar on an unchanged skill is fixed or deleted. Agent and judge are pinned to `claude-opus-5-5`.

Rejected:
- Writing the skill first and dogfooding: lines nobody needs stay in forever.
- pitch-and-deliver's freeze hook and private held-out set: their friction outweighed what they caught for a one-person repo.
- Statistical tests to prove a change level with main: the cost moved from the skill to arguing about graders.

## Consequences

- Every change to the skill needs histories rebuilt and the affected cases rerun.
- Eval spend is uncapped by choice and runs at pitch-and-deliver's scale.
- Behaviour no case covers cannot enter the skill except under ADR-0005.

## Addendum 2026-10-20

The first `delivering-pitches` ships without meeting this decision in full. The deletion pass was stopped part way, because `delivery` is about to be split into a per-stage `sdlc` plugin that reruns ablation per stage. The partial run kept the task list, the interview call, the five plan sections and the gap check. It found two paragraphs no grader needed: the whole Intake paragraph (reading the pitch and refusing an epic) and the Planning lead-in. Both are still in the skill.

The pre-PR review then added lines without a failing case, against this decision: TodoWrite and the Progress checklist as task fallbacks; already-satisfied and judged checks; removing base copies; the repo's mutation-tool score; checking `gh auth status` before pushing; opening PRs in merge order; and `gh stack` only where stacked PRs are enabled, with bodies set by `gh pr edit` and `gh pr ready`. They are to be earned or removed in the `sdlc` split.
