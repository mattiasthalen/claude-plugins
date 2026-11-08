---
name: review
description: The review stage of an sdlc run: runs the parallel reviewers, verifiers and security pass and fixes what holds, unattended. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: review

**First, write `review` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

**Tier.** Read the root `REVIEW.md`: its frontmatter maps path globs to `low`, `medium` and `high`. A path takes the highest tier any glob matches, and the change the highest tier of its paths. Unmatched paths, and a repo without `REVIEW.md`, are Medium. `REVIEW.md`, CI configuration and hook or permission configuration are High whatever the file says. Its prose is the reviewers' brief; where it disagrees with `CLAUDE.md`, it wins, and the disagreement is a finding against `CLAUDE.md`.

**Finders.** Launch fresh `general-purpose` reviewers in parallel, one per lens, each with the spec, the base, the diff and `REVIEW.md`'s prose. The lenses are `implementation:review-cycle`'s briefs in its `references/` (adversarial and design parity always; simplification when the change adds interface; platform reality when it touches the assumptions record; every lens at High), passed verbatim. Each reports findings with `file:line` and writes nothing: where a lens brief allows a throwaway test, this overrides it.

**Security.** At every tier, run `/security-review` on the diff, or a fresh reviewer briefed for security where it is absent. Bug and security findings block the evidence gate until fixed, or closed with a reason the evidence shows.

**Verifiers.** At Medium and High, give each finding to three fresh `general-purpose` verifiers, with the finding and the code it cites, and keep it when at least two say it holds. Never judge a finding yourself.

**Ledger.** Keep the findings in `review.md` in the run's folder: one line each with its disposition. A finding whose lines `git blame` dates before the base is `Pre-existing`: a follow-up, never a fix here. Never report a finding twice. Search for each kept finding's class across the change and fix every instance.

**Fixes.** Fix what holds. Any change to a test file, even a comment, goes to `sdlc:test-writer`; a defect that needs a regression test goes there with the spec and the finding, never the fix, and commits that test itself; that test is a new criterion, added mid-run. After the first round, re-review only the diff since the last round. Stop after three rounds and go to prove with what is open.

Between the test gate and the evidence gate the run goes on unattended: no question, no stop, except the stops this stage names.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Next.** When this stage ends, invoke `sdlc:prove` with the Skill tool and follow it; never carry on from memory of its rules.
