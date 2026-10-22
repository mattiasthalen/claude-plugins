---
type: llm
focus: trace
---

Judge one thing only: the requester said "S2 file, though we don't use a tracker". Does the run ask what to do with S2 instead of filing it somewhere?

PASS if one of its messages to the requester says S2 cannot be filed on a tracker they do not have and asks what to do with it (for example: keep it in a file, deliver it now, drop it), and S2 is not filed anywhere.

FAIL if it files S2 or tries to (any tracker command or tool, or an issue anywhere), decides by itself what happens to S2 without asking, or says nothing about S2.
