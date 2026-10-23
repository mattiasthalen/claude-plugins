---
type: llm
focus: last_message
---

Judge one thing only: does the reply stop at the intent gate with the stories, asking the requester to decide each story and where the next stage runs?

PASS if it shows the stories (or the whole `intent.md`), asks for each story whether to deliver it now, file it for later, or drop it, and offers to continue here, continue in a new session (starting from `intent.md`'s path), or stop.

FAIL if it starts the spec or the design interview, writes a spec, asks only open interview questions with no stories shown, omits the now / file / drop choice, or offers fewer than the three ways to continue.
