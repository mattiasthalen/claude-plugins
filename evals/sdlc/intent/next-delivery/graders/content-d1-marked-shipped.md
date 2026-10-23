---
type: llm
focus: trace
---

Judge one thing only, on the `intent.md` the run wrote or edited in its run folder (`…/sdlc-…/intent.md` or `…/sdlc/intent.md`; read the Write, Edit or Bash calls that touched it): delivery d1 (story S1, the CSV export) was shipped in the earlier turn, with pull request #7 opened, and `sdlc-handoff/intent.md` still shows d1 "in progress". Does the run-folder `intent.md` record d1 as shipped?

PASS if the run-folder `intent.md` marks d1 (or S1) as shipped, done or delivered (pull request #7 named or not), and keeps d2 (S2) as the delivery still to do or now in progress.

FAIL if no `intent.md` was written or edited in the run folder (an edit to `sdlc-handoff/intent.md` does not count), it leaves d1 "in progress" or "not started", or it marks d2 as shipped or done.
