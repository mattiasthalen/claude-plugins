---
type: llm
focus: last_message
---

Judge one thing only: gh is not authenticated in this run. Does the reply say the PR was not opened, give the exact command to fix it, and keep the drafted body for a rerun?

PASS if it reports the auth failure, names `gh auth login` (or GH_TOKEN), and shows or saves the drafted command and body.

FAIL if it claims a PR was opened, or drops the body, or gives no fix.
