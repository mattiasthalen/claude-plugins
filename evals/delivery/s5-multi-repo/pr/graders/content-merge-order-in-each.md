---
type: llm
focus: trace
---

Judge one thing only: does each PR body state the merge order (api first, deploy, then mobile) and name the other PR?

PASS if both bodies carry the order and point at each other.

FAIL if either body lacks the order or the other PR.
