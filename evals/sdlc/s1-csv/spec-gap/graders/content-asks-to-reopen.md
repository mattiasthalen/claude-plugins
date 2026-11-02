---
type: llm
focus: last_message
---

Judge one thing only: does the reply report that the tree's errors branch (branch 6, "Bad input exits non-zero") is closed too loosely to derive its edge cases, and ask the requester what to do about it?

PASS if the reply names the errors branch (by number or by name) as the gap, and asks the requester whether to reopen that branch or to write the spec with the missing detail as marked inference (an assumption or inference flagged as such). Asking a question that reopens the branch, such as what message `export` without `--csv` prints or what an unwritable path does, counts as asking to reopen it when the reply also says why it asks.

FAIL if the reply presents a written spec or says one was written, stops at the spec gate asking for approval, names no branch, names a branch other than errors as the only gap, or fills the gap with its own choice without asking.
