# claude-plugins

Mattias Thalén's personal Claude Code plugin marketplace.

```bash
claude plugin marketplace add mattiasthalen/claude-plugins
claude plugin install sdlc@mattiasthalen
```

## Plugins

- **sdlc**: how a change ships. A change request runs `intent` (user stories, why first), Tobias Karlsson's design interview, a platform check of the design's records with his review cycle, tests first, the build, his review cycle, a proof you approve, then Matt Pocock's `pr` on your go and a reminder to run his `retro` after merge. Say "small change" to start at tests first.
- **design**, **implementation** ([the-exodus/claude-design-skills](https://github.com/the-exodus/claude-design-skills)) and **mattpocock-skills** ([mattpocock/skills](https://github.com/mattpocock/skills)): listed unpinned from their own repositories and installed with `sdlc` as its dependencies; an install follows each one's released version, and `design` its release tags (ADR-0002).

## Layout

```
.claude-plugin/marketplace.json   one entry per plugin
plugins/<name>/                   a local plugin
docs/decisions/                   ADRs; docs/lexicon.md and docs/assumptions.md beside them
evals/<plugin>/                   eval suites, run in-session (evals/README.md)
tests/check_repo.sh               the repository's shape; CI runs it
```
