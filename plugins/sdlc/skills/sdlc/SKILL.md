---
name: sdlc
description: Runs one change through the SDLC — spec, plan, tests, build, review, evidence, pull requests — from an intent (a ticket, text or file), or continues a run from a named stage given its documents' paths.
argument-hint: "<intent> | continue from <stage> using <paths>"
---

An intent, from user stories to ready pull requests, in eight stages: intent once, then spec to ship for each delivery. Each stage reads the documents the stages before it wrote and writes its own; read `references/<stage>.md` when the stage starts and follow it.

| Stage | Writes | Ends at |
|---|---|---|
| intent | `intent.md` | the intent gate |
| spec | `spec.md` | the spec gate |
| plan | `plan.md` | the plan gate |
| test | the tests | the test gate |
| build | the change | review, unattended |
| review | fixes | prove, unattended |
| prove | `evidence.md` | the evidence gate |
| ship | pull requests | done |

**Documents** live in the run's folder: `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

**Phase.** As each stage starts, write its name to `phase` in the run's folder (`intent`, `spec`, `plan`, `test`, `build`, `review`, `prove`, `ship`), and `done` whenever the run ends: its last delivery shipped, stopped at a gate, abandoned, or refused at intake. The plugin's hook reads it to refuse writes the stage must not make, so write files with Write or Edit, not the shell, where it can see them; a refusal is information, never an obstacle to route around.

**Gates.** A gate, and a stop, presents its document whole, in its order, every row as written with its ids, branch tags, marks and checks, and its path, and asks for approval in prose. A yes moves on for the heads it saw: if one has moved since, rerun every check there before anything else and bring the fresh results back to the gate; "yes, but…" is a change request: amend the document and ask again. Every gate is also a seam: ask whether to continue in this session, continue in a new one (and which folder to keep the documents in, naming each document's absolute path there), or stop. Between the test gate and the evidence gate the run goes on unattended.

**Publishing.** On the spec gate's yes, before the seam, publish the spec if the requester or the project's docs say to and it is not published yet: where and as what they say, linked to its stories, with the spec's content as the body, never a path into the run's folder. Make the call once, even when the tracker looks unreachable or unauthenticated; a failure is reported with its error, and the run goes on. A published spec amended and approved again gets an offer to update the published item, acted on only on a yes.

**Deliveries.** `intent.md` in the run's folder (a handed-in one is read where it is until the first delivery ships, then copied there unchanged, and each seam names the copy) marks a delivery shipped when its pull requests open. After ship, the first delivery not yet shipped starts at spec, its documents in a subfolder of the run's folder named for it (`d2/`, `d3/`, …), instead of ending the run.

**Continuing.** "continue from <stage> using <paths>" starts at that stage with those documents, which must exist and be read first; a missing one is refused with its path and the run asks for it.

**Progress.** Keep the stages as a task list from the first turn, spec to ship once per delivery, and tick them as they end.
