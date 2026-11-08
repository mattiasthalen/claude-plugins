---
name: prove
description: The prove stage of an sdlc run: runs every check at the head and writes evidence.md, ending at the evidence gate. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: prove

**First, write `prove` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

Trust nothing the build reported. At each slice's head, run every check, the repository's existing tests and CI's commands. Run `git diff <test gate commit>..HEAD` over the test paths: a change there outside the test-writer's commits voids the evidence. Where the diff touches a skill, agent, `CLAUDE.md` or hook and the repo has eval suites, run the affected suites with `claude plugin eval` and report their pass rates.

Write `evidence.md`:

- the claim: what was asked for, and what is true now;
- per slice, base and head SHAs and a table of every criterion and edge case: check, result at the head;
- the existing suite and CI at the head;
- tests added mid-run, marked as such, each with the review finding it came from;
- review: rounds used, findings by disposition, what was closed with a reason;
- tier, merge danger (a one- or two-way door, and the blast radius), assumptions, follow-ups.

A criterion red, the existing suite or CI red, an open bug or security finding, or an eval below its bar: no pull request. Lead the evidence with it — its last output, what was tried, why it fails — and offer continue (another try, checks unchanged), re-plan (amend the spec or plan; a wrong check goes here) or abandon. Never call it done.

Otherwise, at Low tier go straight to ship, and say in the final reply that Low tier, and the paths that made it so, is why no evidence gate was asked. At Medium, end at the evidence gate; at High, say which path made it High, and ask the requester to read the diff, not only the evidence. Where the Artifact tool exists, also publish `evidence.md` as a page.

Between the test gate and the evidence gate the run goes on unattended: no question, no stop, except the stops this stage names.

**Gate.** The gate presents its document whole, in its order, every row as written with its ids, branch tags, marks and checks, and its path, and asks for approval in prose. A yes moves on for the heads it saw: if one has moved since, rerun every check there before anything else and bring the fresh results back to the gate; "yes, but…" is a change request: amend the document and ask again. The gate is also a seam: ask whether to continue in this session, continue in a new one (and which folder to keep the documents in, naming each document's absolute path there), or stop.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Next.** On the evidence gate's yes (or straight away at Low tier), with "continue here", invoke `sdlc:ship` with the Skill tool and follow it; never carry on from memory of its rules. A new session continues with `/sdlc continue from ship using <paths>`.
