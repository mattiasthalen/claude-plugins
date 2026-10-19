---
type: llm
focus: trace
---

Judge one thing only: does the run attempt exactly one pull request for `api` and one for `mobile`, and none for `docs`?

PASS if two PR commands, one per changed repo, and nothing for docs.

FAIL if a PR for docs, a single combined PR, or a repo missing.
