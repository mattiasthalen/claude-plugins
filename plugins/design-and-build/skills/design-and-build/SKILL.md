---
name: "design-and-build"
description: Design interview in plan mode, then an approved plan carrying the brief, then capture, build, review and PR.
argument-hint: "<pitch>"
disable-model-invocation: true
---

The interview builds the tree; the plan carries the _brief_, the technical spec everything is built and reviewed against. ExitPlanMode is called once, in step 4, with the brief in the plan: that approval is the gate between thinking and writing.

## Progress

The task list (TaskCreate, TaskUpdate) is my view of the run. Before step 1, create one task per step, named by its heading. Mark each in progress as it starts and completed once its done-when holds; add a task for each review round as it starts. If approving the plan cleared the list, recreate it with steps 1 to 4 completed.

## Doubt pass

A fresh-context adversarial review, run from the main session (subagents cannot spawn subagents). Spawn a new general-purpose subagent and give it only the ARTIFACT and the CONTRACT the calling step names, under this prompt:

> Adversarial review. Find what is wrong with this artifact against the contract. Assume the author is overconfident. Look for unstated assumptions, unhandled edge cases, hidden coupling or shared state, contract violations, broken conventions, failure modes under unexpected input. Do not validate. Do not summarize. Find issues, or state explicitly that you found none after thorough examination.

The reviewer gets the artifact and the contract, never the reasoning behind them: no interview or builder conversation, no commit rationale, no claim that the artifact is correct. Re-read the artifact against each finding yourself before classifying it; the calling step says where each class goes.

The prompt is adapted from Addy Osmani's `doubt-driven-development` (agent-skills, MIT).

## 1. Interview

Enter plan mode with EnterPlanMode. Invoke the `design:design-interview` skill and run it through Phase 8. Pitch: $ARGUMENTS

Leave its Phase 8 capture offers to step 5 and carry on to step 2.

Done when: every branch is terminal through the four locks, and the tree, assumptions and lexicon are laid out in the conversation.

## 2. Gap check

Read `references/artifacts.md` in `design-interview`'s skill directory. For every artifact this design needs, walk each section against the tree. A section is either _grounded_ (the tree answers it) or a _gap_. Put every gap to me in prose, and close it by reopening its branch under the four locks or by recording my acceptance of marked inference.

Done when: every section of every needed artifact is grounded or carries accepted inference.

## 3. Plan

Explore the affected code until the build names its files and the commands that turn it green. Extend the plan file into the shape below, the design first. The plan is the design's durable copy: approval can clear the conversation, and steps 5 to 9 work from the plan.

Done when: the plan file carries the design whole, in the shape below.

### Plan shape

1. **Design**: the tree, assumptions and lexicon exactly as step 2 left them, every branch with its rationale. The brief and the capture are written from this section
2. **Brief**: the full technical spec, written out in the plan. Shape per `references/artifacts.md`: functional spec, interface contract, domain model, edge cases, acceptance criteria, with every inference marked. Sections and acceptance criteria numbered, so tests, commits and findings can cite them
3. **Capture**: at the documentation location found in Phase 2: lexicon delta, assumptions record delta, ADRs (flagging any they supersede)
4. **Build**: the branch, then the commits in order. Each commit is a vertical slice, a thin path that works end to end rather than a layer, and lists: the brief sections it implements, the acceptance criteria it covers, the tests written first, the files it touches (aim for five or fewer), its verification command. Mark a checkpoint after the foundational commits. Every brief section and every acceptance criterion is covered by some commit
5. **PR**: the ticket, if any; the PR body; manual steps for me after merge
6. **Risks**: assumptions most likely to break, and the observation that would reveal each

## 4. Doubt the brief

Run a doubt pass. ARTIFACT: the plan's brief section. CONTRACT: the plan's design section (tree, assumptions, lexicon). It catches brief content that drifted from the tree or invented beyond it.

Each valid finding is a gap: put it to me and close it as in step 2, by reopening its branch under the four locks or recording my acceptance of marked inference, then update the plan. Drop noise. Run one cycle, and a second only if the first changed the brief. Then present the plan with ExitPlanMode.

Done when: I approve a plan whose brief has survived its doubt pass.

## 5. Capture

Create the plan's branch. Write the capture section yourself, in the main session, from the plan's design section, and commit it first on that branch.

Copy the approved brief verbatim to `brief.md` in your scratchpad: the builder's hand-off, since it shares no context with the plan. The repo's durable record is the ADRs and assumptions. If the work has a ticket, post the brief there as a comment (Jira through the `twg` CLI).

Done when: every capture artifact exists and uses lexicon terms exactly, `brief.md` matches the approved brief, and the ticket (if any) carries it.

## 6. Build

Confirm `agent-skills:test-driven-development` and `agent-skills:incremental-implementation` are among the available skills. If either is missing, halt and tell me to install `agent-skills`; the build runs only with its method.

Spawn one _builder_ subagent on this session's model at its recommended effort. It loads those two skills and `design:design-philosophy`, starts from `brief.md`, the lexicon and the relevant ADRs, and makes the plan's commits in order. Those two are the only agent-skills it loads: the rest carry their own stop rules and files, which fight this flow. Its contract wins wherever it and the skills disagree:

- Per commit: a failing test citing its acceptance criterion number, then green, then refactor, then the commit's verification command, then the commit, citing the brief section.
- The _floor_: skipping or deleting a test, adding a lint or type suppression, weakening or removing an assertion, leaving a stub, lowering a threshold. Reaching the floor halts the builder and comes to me as a report.
- An invalidated assumption or brief contradiction halts it and comes to me as a design question.

Done when: every planned commit exists, every verification command is green, and every acceptance criterion has a test that failed before its commit.

## 7. Review

Review in rounds, three at most. Each round notes `HEAD` when it starts, and every round walks the whole diff since the capture commits against the brief, section by section; each unmet section is a finding citing its number.

- **Round 1** runs the built-in `/code-review medium` on the diff since the capture commits.
- **Rounds 2 and 3** run `/code-review medium <previous round's HEAD>..HEAD`, so the review covers the builder's fix commits and the callers they reach, and check that each earlier blocker is resolved.

Each round also runs a doubt pass. ARTIFACT: the round's diff (round 1 since the capture commits, rounds 2 and 3 the previous round's `HEAD..HEAD`). CONTRACT: the brief sections that diff implements. Classify each finding, first match wins:

1. A contract misread, because the brief is unclear: a brief gap. It comes to me and leaves the rounds.
2. Valid and actionable: a blocker if it meets the definition below, otherwise a nit.
3. A valid trade-off: goes to step 9.
4. Noise: dropped, noting any contract context that would have prevented it.

A _blocker_ is an unmet brief section, or a correctness finding whose failure scenario you can trace through the code yourself; every other finding is a _nit_. After rounds 1 and 2, send the blockers to the builder (continue it, so it keeps its context) and start the next round. A blocker the builder disputes instead of fixing comes to me with both sides, and leaves the rounds.

Done when: a round finds no blockers, or round 3 ends. Round 3's blockers come to me before step 8, unfixed; nits go to step 9 as tracker candidates.

## 8. Pull request

Open a draft PR. The body lists the brief's acceptance criteria, the manual steps after merge, and links the ticket's brief comment (with no ticket, it notes the brief went to the builder). If Copilot review is available on the repo, request it; fix or answer each thread through the builder, and resolve it. Then mark the PR ready.

Done when: the PR is ready, with every Copilot thread resolved or Copilot unavailable.

## 9. Report

Update the assumptions record with any assumption invalidated during build. Then report: PR link, acceptance criteria met and unmet, invalidated assumptions, trade-offs from the doubt passes, tracker candidates for me to file, review nits among them. Outcomes only.
