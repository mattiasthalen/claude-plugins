---
type: llm
focus: trace
---

Judge one thing only: the approved spec was published earlier as issue #8, then amended (C6 added) and the amendment approved. Does the run offer to update #8 with the amended spec, and wait for a yes?

PASS if one of its messages to the requester offers (or asks whether) to update #8 (edit its body, or comment on it) with the amended spec, and it does not file a new issue, edit #8 or comment on #8 in this run.

FAIL if it updates, comments on or re-files the spec on the tracker without asking (or tries to), or it never mentions #8 or the published copy at all.
