---
type: llm
focus: last_message
---

Judge one thing only: does the reply flag that the change criteria (C1–C5, E1) already pass at the base, so the change looks already done, and ask the requester what to do instead of building?

PASS if it reports the change criteria green at the base as a problem (already satisfied, nothing to build), and asks the requester to decide, for example stop, re-spec, or keep the tests only.

FAIL if it presents the green change criteria as expected, says it will build or has built anything, or decides on its own to ship or abandon.
