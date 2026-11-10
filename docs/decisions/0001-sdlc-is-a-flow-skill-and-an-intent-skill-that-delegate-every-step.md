# ADR-0001 — sdlc is a flow skill and an intent skill that delegate every step

**Status:** Accepted (2026-11-10)

## Context

The first `sdlc` (0.1 to 0.3, in git history before this record) was one model-invocable skill that loaded a reference file per stage, wrote its own spec, plan and evidence documents, dispatched its own test-writer agent, ran its own review with verifier voting, and enforced stage gates with a hook. Running it showed the cost: long runs, drift past the intent (the spec interview growing a run well past its stories), and steps quietly skipped when the instructions around them were long.

The steps it wrapped already exist as skills Mattias uses directly: `design:design-interview` for design, `design:design-philosophy` and `implementation:code-style` for building, `implementation:review-cycle` for review, and Matt Pocock's `pr` and `retro`. What the flow needs from `sdlc` is the order, the gates where he decides, and the one step nobody else covers: turning a request into user stories before design.

## Decision

`sdlc` holds two skills.

- `sdlc` is the flow: intent, design interview, tests first, build, review cycle, the SHOW ME proof, his go, the pull request, and a retro reminder after merge. It loads by its description. It names the skill each step runs and the condition that ends the step, and holds no copy of what those skills do.
- `intent` turns a request into user stories, why first, and hands the stories it is told to deliver now to `design:design-interview` as the pitch. It is called by Mattias or by `sdlc`, never on its own.

They are separate skills because they are invoked differently, and because a skill that carries both shows the agent design and tests coming while it is still on the stories, which is how a step gets rushed. They are one plugin with one version because `sdlc` names `intent`.

Every line in either skill is earned: it goes in only when an eval case is red without it and green with it.

Rejected:

- **One skill with intent folded in as its first step:** the later steps stay in view during intent and pull it to an early finish.
- **Two plugins:** two versions to keep in step, for a pair that is never installed apart.
- **Keeping the staged sdlc and trimming it:** the stages duplicate skills that exist upstream, so every upstream improvement had to be re-made here.

## Consequences

- The flow is as good as the skills it calls. An upstream change in design, implementation or Pocock's skills changes the flow without a change here; the eval suite is what notices.
- There is no spec, plan, evidence document, test-writer agent, own review or stage hook any more. The tests-first rule rests on the flow's wording and its eval cases, not on a hook that refuses writes.
- A skill starts nearly empty and grows only by failing cases, so its length is a measure of what the agent actually gets wrong.

## Addendum 2026-11-10

Built under the earned-line rule, the `sdlc` skill names fewer steps than the Decision lists. Each line was run with its case and then without it, and only the lines whose case went red stayed. The design interview, the build and the review cycle have no line: with the flow loaded, the agent reached `design:design-interview` from `intent`'s hand-off and `implementation:review-cycle` by its own description, and their cases stayed green without a line. `intent` also has no line in `sdlc` beyond the start: its own description carries it. The Decision stands; the steps it lists are the flow's order, and the skill holds only the lines that order needs to hold.
