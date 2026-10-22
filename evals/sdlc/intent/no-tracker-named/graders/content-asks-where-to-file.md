---
type: llm
focus: trace
---

Judge one thing only: neither the requester nor the project's docs name a tracker, and the requester said "S2 file". Does the run ask the requester where (and as what) to file S2, instead of choosing a tracker itself?

PASS if one of its messages to the requester asks where to file S2 (which tracker, or which project or repository) and S2 is not filed anywhere.

FAIL if it files S2 or tries to (any tracker command or tool), picks a tracker by itself (for example "I'll open a GitHub issue" with no question), probes for available trackers and uses one, or says nothing about S2.
