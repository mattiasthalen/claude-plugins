---
name: build
description: The build stage of an sdlc run: builds the change slice by slice until its checks pass, unattended. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: build

**First, write `build` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

Add one task per id in the spec (every criterion, preservation criterion and edge case, never a range such as C1–C5), and tick each when its check passes at HEAD.

The first slice in a repo starts with one commit, before any code: that repo's `capture/<repo>/` beside `spec.md`, copied to the same paths in the repo. Nothing else under `capture/` is committed.

Build each slice on its branch, in the plan's order, with atomic commits staged by path, until its checks pass. The tests are fixed: a check that looks wrong goes to the evidence gate as a stop, for a re-plan.

A criterion still red after a fair try, or a tool the build needs that will not run after a search for another install, stops the run: go to prove, which leads the evidence with it.

Between the test gate and the evidence gate the run goes on unattended: no question, no stop, except the stops this stage names.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Next.** When this stage ends, invoke `sdlc:review` with the Skill tool and follow it; never carry on from memory of its rules.
