---
name: plan
description: The plan stage of an sdlc run: writes plan.md from the spec, ending at the plan gate. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: plan

**First, write `plan` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

Read `spec.md`, then write `plan.md`:

- **Slices**: a table of slice, repo, base, direction and pull request. Every slice ships on its own and leaves the system consistent. Cut vertically by default; cut horizontally, or keep one slice, when a per-feature cut would leave a mixed state, such as a storage swap. Say which, and why.
- **Checks**: for every criterion and edge case by its id, what its check will verify and where it will live. The test stage writes them; the plan names them.
- **Order**: the build order within each slice, and the risks.

Write no tests and no code. End at the plan gate.

**Gate.** The gate presents its document whole, in its order, every row as written with its ids, branch tags, marks and checks, and its path, and asks for approval in prose. A yes moves on for the heads it saw: if one has moved since, rerun every check there before anything else and bring the fresh results back to the gate; "yes, but…" is a change request: amend the document and ask again. The gate is also a seam: ask whether to continue in this session, continue in a new one (and which folder to keep the documents in, naming each document's absolute path there), or stop.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Next.** On the gate's yes, with "continue here", invoke `sdlc:test` with the Skill tool and follow it; never carry on from memory of its rules. A new session continues with `/sdlc continue from test using <paths>`.
