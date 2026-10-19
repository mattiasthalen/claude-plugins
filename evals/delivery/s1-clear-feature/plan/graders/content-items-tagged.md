---
type: llm
focus: last_message
---

Judge one thing only: does every acceptance criterion, edge case and guardrail in the plan's brief carry the design branch (or branches) it comes from?

PASS if each of them is tagged with a branch number or name from the tree, and every concrete choice in the brief traces to a branch.

FAIL if any criterion, edge case or guardrail has no branch tag, or the brief makes a choice the tree never made without saying so.
