---
name: "design-and-build"
description: Design interview in plan mode, then an approved plan carrying the brief, then capture, build, review and PR.
argument-hint: "<pitch>"
disable-model-invocation: true
---

The interview builds the tree; the plan carries the _brief_, the technical spec everything is built and reviewed against. ExitPlanMode is called once, in step 3, with the brief in the plan: that approval is the gate between thinking and writing.

## 1. Interview

Enter plan mode with EnterPlanMode. Invoke the `design:design-interview` skill and run it through Phase 8. Pitch: $ARGUMENTS

Leave its Phase 8 capture offers to step 4 and carry on to step 2.

Done when: every branch is terminal through the four locks, and the tree, assumptions and lexicon are laid out in the conversation.

## 2. Gap check

Read `references/artifacts.md` in `design-interview`'s skill directory. For every artifact this design needs, walk each section against the tree. A section is either _grounded_ (the tree answers it) or a _gap_. Put every gap to me in prose, and close it by reopening its branch under the four locks or by recording my acceptance of marked inference.

Done when: every section of every needed artifact is grounded or carries accepted inference.

## 3. Plan

Explore the affected code until the build names its files and the commands that turn it green. Extend the plan file into the shape below, the design first, and present it with ExitPlanMode. The plan is the design's durable copy: approval can clear the conversation, and steps 4 to 8 work from the plan.

Done when: I approve a plan that carries the design whole.

### Plan shape

1. **Design**: the tree, assumptions and lexicon exactly as step 2 left them, every branch with its rationale. The brief and the capture are written from this section
2. **Brief**: the full technical spec, written out in the plan. Shape per `references/artifacts.md`: functional spec, interface contract, domain model, edge cases, acceptance criteria, with every inference marked. Sections numbered, so commits and findings can cite them
3. **Capture**: at the documentation location found in Phase 2: lexicon delta, assumptions record delta, ADRs (flagging any they supersede)
4. **Build**: branch, files, commit order with the brief sections each commit implements, verification commands. Every brief section is covered by a commit
5. **PR**: the ticket, if any; the PR body; manual steps for me after merge
6. **Risks**: assumptions most likely to break, and the observation that would reveal each

## 4. Capture

Create the plan's branch. Write the capture section yourself, in the main session, from the plan's design section, and commit it first on that branch.

Copy the approved brief verbatim to `brief.md` in your scratchpad: the builder's hand-off, since it shares no context with the plan. The repo's durable record is the ADRs and assumptions. If the work has a ticket, post the brief there as a comment (Jira through the `twg` CLI).

Done when: every capture artifact exists and uses lexicon terms exactly, `brief.md` matches the approved brief, and the ticket (if any) carries it.

## 5. Build

Spawn one _builder_ subagent on this session's model at its recommended effort. It starts from `brief.md`, the lexicon, the relevant ADRs and `design:design-philosophy`, and makes the plan's commits in order. An invalidated assumption or brief contradiction halts it and comes to me as a design question.

Done when: every planned commit exists and every verification command is green.

## 6. Review

Review in rounds, three at most:

- **Round 1** runs the built-in `/code-review medium` on the diff since the capture commits, then walks that diff against the brief, section by section; each unmet section is a finding citing its number.
- **Rounds 2 and 3** review only the builder's commits since the previous round: `/code-review medium` on them, plus a check that each earlier blocker is resolved.

A _blocker_ is a correctness finding the review is confident in, or an unmet brief section; every other finding, an uncertain one included, is a _nit_. Send the round's blockers to the builder (continue it, so it keeps its context) and start the next round.

Done when: a round finds no blockers, or the third round ends. Blockers left after the third come to me before step 7; nits go to step 8 as tracker candidates.

## 7. Pull request

Open a draft PR. The body lists the brief's acceptance criteria, the manual steps after merge, and links the ticket's brief comment (with no ticket, it notes the brief went to the builder). If Copilot review is available on the repo, request it; fix or answer each thread through the builder, and resolve it. Then mark the PR ready.

Done when: the PR is ready, with every Copilot thread resolved or Copilot unavailable.

## 8. Report

Update the assumptions record with any assumption invalidated during build. Then report: PR link, acceptance criteria met and unmet, invalidated assumptions, tracker candidates for me to file, review nits among them. Outcomes only.
