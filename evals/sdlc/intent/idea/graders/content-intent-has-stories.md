---
type: llm
focus: trace
---

Judge one thing only, on the `intent.md` the run wrote into its run folder (`…/sdlc-…/intent.md` or `…/sdlc/intent.md`; read the content of the Write call or Bash command that created it, and any later Edit to it): is the intent written as user stories?

PASS if it holds at least one story with an id, an "As a … I want … so that …" statement (any capitalisation or line breaks), and acceptance criteria for that story.

FAIL if no `intent.md` was written in the run folder, or it holds no story in that form, or a story has no acceptance criteria, or it is a spec (criteria tables with checks, a design tree) rather than stories.
