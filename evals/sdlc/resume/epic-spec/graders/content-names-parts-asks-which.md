---
type: llm
focus: last_message
---

Judge one thing only: the run was handed `sdlc-handoff/back-office.md`, a plain document (no user stories) that holds four changes: a CSV export for accounting, returns with refunds, a customer self-service portal, and replacing the JSON store with SQLite. Does the reply say this is more than one change, name the parts, and ask which one to take through the spec first?

PASS if it names the four parts (or a fair grouping of them) and asks which to start with, and stops there.

FAIL if it starts designing all of it, writes a spec covering more than one part, picks one without asking, or runs the design interview.
