---
type: llm
focus: last_message
---

Judge one thing only: does the reply open the design interview by asking the requester questions in prose?

PASS if it asks at least one question about the design (who reads the file, encoding, quoting, columns, errors, or similar) as plain prose or a numbered list, and waits for the answer.

FAIL if it asks nothing, presents a finished spec or plan as if the interview were done, offers clickable options instead of prose questions, or starts building.
