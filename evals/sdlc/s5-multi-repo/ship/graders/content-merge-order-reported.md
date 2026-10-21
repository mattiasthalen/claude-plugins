---
type: llm
focus: last_message
---

Judge one thing only: the approved evidence covers `api` and `mobile`, with `docs` untouched, and says `api` merges and deploys first, then `mobile`. Does the reply account for exactly two pull requests (opened, or kept as bodies because `gh` failed), one for `api` and one for `mobile`, none for `docs`, and state that order?

PASS if both PRs or kept bodies are named, `docs` gets none, and the reply says `api` merges (and deploys) before `mobile`.

FAIL if `docs` gets a PR or body, either repo is missing, or the order is missing or reversed.
