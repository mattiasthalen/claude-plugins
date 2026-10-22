---
type: llm
focus: trace
---

Judge one thing only, on the `intent.md` the run wrote into its run folder (read the content of the Write call or Bash command that created it, and any later Edit to it): the intent arrived as one well-formed story from ticket #42 (a back-office clerk listing one customer's orders). Is it kept as one story, refined in place?

PASS if `intent.md` holds exactly one story, that story is the clerk's customer filter (its "As a … I want … so that …" and the three acceptance criteria from the intent are there, possibly sharpened or with criteria added), and it records that it came from #42.

FAIL if no `intent.md` was written, it holds two or more stories (for example the original plus a refined copy, or the story split up), or the story's meaning was changed.
