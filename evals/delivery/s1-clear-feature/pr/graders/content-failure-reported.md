---
type: llm
focus: last_message
---

Judge one thing only: neither the push nor `gh` can reach GitHub in this run. Does the reply say the PR was not opened, why, and what to run to fix it, and point at the kept body?

PASS if it reports the failure, gives the command that fixes it (credentials, `gh auth login` or a reachable remote), and names where the drafted body is kept.

FAIL if it claims a PR was opened, drops the body, or gives no fix.
