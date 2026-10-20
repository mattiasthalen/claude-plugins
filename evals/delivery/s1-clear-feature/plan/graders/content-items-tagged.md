---
type: llm
focus: last_message
---

Judge one thing only: does every acceptance criterion, edge case and guardrail in the plan's brief carry the design branch (or branches) it comes from?

PASS if each criterion, edge case and guardrail is tagged with a branch number from the plan's Design section. Branches the run added beyond the interview's tree count, as long as the Design section lists them and marks them as its suggestion. Prose in the functional spec need not be tagged.

FAIL if any criterion, edge case or guardrail has no branch tag, or cites a branch the Design section does not have.
