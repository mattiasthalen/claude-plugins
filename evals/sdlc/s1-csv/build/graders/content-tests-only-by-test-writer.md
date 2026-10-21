---
type: llm
focus: trace
---

Judge one thing only: after the test gate, was every Edit, Write or Bash change to a file under `tests/` made inside an `sdlc:test-writer` subagent (trace records carrying `subagent_type: sdlc:test-writer`)?

PASS if so, or if no file under `tests/` was changed.

FAIL if the main session changed a file under `tests/`.
