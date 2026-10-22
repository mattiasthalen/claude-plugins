---
type: llm
focus: trace
---

Judge one thing only. The intent names four independent parts: a CSV export for accounting, a returns flow with refunds, a customer self-service portal, and replacing the JSON order store with SQLite. Read the `intent.md` the run wrote into its run folder (`…/sdlc-…/intent.md` or `…/sdlc/intent.md`; the content of the Write or Bash call that created it, and any later Edit) and the run's last message.

PASS if `intent.md` holds at least four stories, one per part (a part may be split further), each in "As a … I want … so that …" form with acceptance criteria, and the last message stops at the intent gate asking, per story, now / file / drop (and how the "now" stories group into deliveries).

FAIL if no `intent.md` was written in the run folder, the parts are merged into fewer than four stories, the run picks a part itself without asking, or it starts designing or writes a spec.
