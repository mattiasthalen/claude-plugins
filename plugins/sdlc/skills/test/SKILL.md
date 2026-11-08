---
name: test
description: The test stage of an sdlc run: dispatches the test-writer, runs the checks at the base and ends at the test gate. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: test

**First, write `test` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

Dispatch the `sdlc:test-writer` agent with `spec.md` and the plan's check descriptions, and only those. It writes every test and judged rubric and commits them on the slice's branch. Dispatch it before asking anything, even when the repository already seems to hold the change or its tests: the base run shows it, and the question comes after.

Then run every check at the base and show each result by id: a change criterion should be red, a preservation criterion green. Flag every other result; a change criterion already green means the work may be done already, so ask the requester before going on.

End at the test gate. Say that the next stretch — build, review, prove — runs unattended, and recommend auto mode or allowed tools for the build's commands so it does not wait on prompts.

**Gate.** The gate presents its document whole, in its order, every row as written with its ids, branch tags, marks and checks, and its path, and asks for approval in prose. A yes moves on for the heads it saw: if one has moved since, rerun every check there before anything else and bring the fresh results back to the gate; "yes, but…" is a change request: amend the document and ask again. The gate is also a seam: ask whether to continue in this session, continue in a new one (and which folder to keep the documents in, naming each document's absolute path there), or stop.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Next.** On the gate's yes, with "continue here", invoke `sdlc:build` with the Skill tool and follow it; never carry on from memory of its rules. A new session continues with `/sdlc continue from build using <paths>`.
