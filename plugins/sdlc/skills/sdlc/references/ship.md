# Ship

Check that every head is the one the evidence was approved at. If one moved, prove again at the new head — every check and the existing suite, run there — and bring the fresh evidence back to the gate.

For each slice, invoke `sdlc:pr` and write the body into the run's folder as `pr-<branch>.md`. When the repository has a `.github/pull_request_template.md`, use its sections and only those, with tier, merge danger and revert inside them; otherwise `## Summary`, `## Testing` (this slice's criteria and their results at the head, the existing suite, eval pass rates), `## Risk` (tier, merge danger, merge order) and `## How to revert`. Wherever the evidence goes, its rows keep their ids (C1, E1, P1). Where `pr` asks for screenshots, a glossary or other sections, this wins: no images, no spec, no design tree.

Check `gh auth status`, then push each branch and open one ready pull request per slice and repo with `gh pr create --title … --body-file …`, in merge order. Base a later slice on the earlier slice's branch with `--base` and say in its Risk to merge the lower one first. Across repos, each body names the others and the merge order. A repo with no change gets no pull request.

If `gh` or a push fails, say what failed, the exact command that fixes it, and where the bodies are. End with the links and follow-ups, and write `done` to `phase`.
