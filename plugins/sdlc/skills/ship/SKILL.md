---
name: ship
description: The ship stage of an sdlc run: writes the pull request bodies and opens the pull requests. Invoked by the sdlc skill or by the stage before it, never outside a run.
---

# sdlc: ship

**First, write `ship` to `phase`** in the run's folder, with Write or Edit, not the shell. The plugin's hook reads it to refuse writes this stage must not make; a refusal is information, never an obstacle to route around. Then tick off the stage before it in the task list and mark this one in progress.

**Run folder.** The run's documents live in `sdlc/` in the session scratchpad, or `${TMPDIR:-/tmp}/sdlc-${CLAUDE_SESSION_ID}/` in a session without one — never inside a repository. Documents handed in from elsewhere are read where they are; what the run writes goes to its folder. No file outside the run's folder is written before the plan is approved, and the documents are never committed.

Check that every head is the one the evidence was approved at. If one moved, prove again at the new head — every check and the existing suite, run there — and bring the fresh evidence back to the gate.

For each slice, invoke `sdlc:pr` and write the body into the run's folder as `pr-<branch>.md`. When the repository has a `.github/pull_request_template.md`, use its sections and only those, with tier, merge danger and revert inside them; otherwise `## Summary`, `## Testing` (this slice's criteria and their results at the head, the existing suite, eval pass rates), `## Risk` (tier, merge danger, merge order) and `## How to revert`. Wherever the evidence goes, its rows keep their ids (C1, E1, P1). Where `pr` asks for screenshots, a glossary or other sections, this wins: no images, no spec, no design tree.

Check `gh auth status`, then push each branch and open one ready pull request per slice and repo with `gh pr create --title … --body-file …`, in merge order. Base a later slice on the earlier slice's branch with `--base` and say in its Risk to merge the lower one first. Across repos, each body names the others and the merge order. A repo with no change gets no pull request.

If `gh` or a push fails, say what failed, the exact command that fixes it, and where the bodies are. End with the links and follow-ups, and write `done` to `phase`.

**Stops.** A stop presents its document the same way, whole and with its path, and offers the same seam: continue here, continue in a new session (naming each document's absolute path), or stop. When the run ends — its last delivery shipped, stopped, abandoned, or refused at intake — write `done` to `phase`.

**Deliveries.** `intent.md` in the run's folder (a handed-in one is read where it is until the first delivery ships, then copied there unchanged, and each seam names the copy) marks a delivery shipped when its pull requests open. After ship, the first delivery not yet shipped starts at spec, its documents in a subfolder of the run's folder named for it (`d2/`, `d3/`, …), instead of ending the run: invoke `sdlc:spec` for it.
