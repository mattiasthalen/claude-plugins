---
type: llm
focus: last_message
---

Judge one thing only: does the reply say that `sdlc-handoff/missing.md` does not exist, refuse to start the plan without it, and ask for the spec (its path or content)?

PASS if it reports the missing file and asks for the document, without writing a plan or starting a new design interview.

FAIL if it writes a plan anyway, invents a spec, starts interviewing from scratch, or does not say the file is missing.
