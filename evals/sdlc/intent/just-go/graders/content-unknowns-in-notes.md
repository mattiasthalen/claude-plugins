---
type: llm
focus: trace
---

Judge one thing only, on the `intent.md` the run wrote into its run folder (read the content of the Write call or Bash command that created it): the requester said "just go, don't ask me anything", so are the stories written from what the intent says, with what is not known left as notes instead of invented or asked?

PASS if `intent.md` holds at least one story in "As a … I want … so that …" form with acceptance criteria, and the things the intent does not settle (who exactly, what "easier" means, scope) appear in the stories' notes or an open-questions note, marked as unknown or as the run's assumption.

FAIL if no `intent.md` was written, the run asked the requester interview questions and stopped before writing it, or it presents invented specifics as the requester's decisions with no note that they are unknown or assumed.
