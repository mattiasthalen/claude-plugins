---
name: spec
description: The spec stage of an sdlc run: runs the design interview, captures its records and writes spec.md, ending at the spec gate. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: spec

**First, write `spec` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

The intent is the delivery's stories. A document handed in without stories is taken as it arrives: if it holds more than one change, name the changes and ask which one to deliver, then stop.

Invoke `design:design-interview` and run it to its end; ask its questions in prose. Invoking it is the user's request for its capture, so when the tree is complete capture runs without asking. Capture writes under the run's folder: each record in `capture/<repo>/`, `<repo>` being the repository's name as the plan's slices will name it, at the repo-relative path the interview chooses, and whole: a record that amends a file the repo already has starts from the repo's current copy. The brief goes in `brief/`. A gap capture reports goes to the requester, and the run waits for the answer. Skip the interview only when the requester says the change is small; then lay out a short tree yourself, saying who closed each choice.

Once capture has finished, write `spec.md`: the acceptance criteria and edge cases in the shape of design-interview's `references/artifacts.md`. Every criterion and edge case carries the story it serves (or "all"), the design branch it came from, as `[n]`, and its check; the spec may add criteria no story asked for, marked as its own. Each check is a command, or "judged" with the rubric a fresh reviewer will apply; the edge cases get a check column too, and every row fills it: a case with nothing to check is out of scope and goes under Non-criteria. A choice the tree left open becomes a branch the spec adds, numbered after the tree's and marked as the spec's own. "This must not change" is a preservation criterion, checked green at the base and the head.

Write no code, not even in a copy to try a check: the test stage runs the checks. End at the spec gate.

**Publishing.** On the spec gate's yes, before the seam, publish the spec if the requester or the project's docs say to and it is not published yet: where and as what they say, linked to its stories, with the spec's content as the body, never a path into the run's folder. Make the call once, even when the tracker looks unreachable or unauthenticated; a failure is reported with its error, and the run goes on. A published spec amended and approved again gets an offer to update the published item, acted on only on a yes.

**Gate.** The gate presents its document whole, in its order, every row as written with its ids, branch tags, marks and checks, and its path, and asks for approval in prose. A yes moves on for the heads it saw: if one has moved since, rerun every check there before anything else and bring the fresh results back to the gate; "yes, but…" is a change request: amend the document and ask again. The gate is also a seam: ask whether to continue in this session, continue in a new one (and which folder to keep the documents in, naming each document's absolute path there), or stop.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Next.** On the gate's yes, with "continue here", invoke `sdlc:plan` with the Skill tool and follow it; never carry on from memory of its rules. A new session continues with `/sdlc continue from plan using <paths>`.
