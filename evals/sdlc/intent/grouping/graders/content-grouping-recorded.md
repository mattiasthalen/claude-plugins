---
type: llm
focus: trace
---

Judge one thing only, on the `intent.md` the run wrote or edited in its run folder (`…/sdlc-…/intent.md` or `…/sdlc/intent.md`; read the Write, Edit or Bash calls that touched it): does it record that S1 (CSV export) and S2 (find a customer's orders) are "now" and go as one delivery, and that S3 is dropped?

PASS if the run-folder `intent.md` records S1 and S2 together in one delivery (a delivery section, a table, or a line naming both) and marks S3 as dropped.

FAIL if no `intent.md` was written or edited in the run folder (an edit to `sdlc-handoff/intent.md` does not count), it records S1 and S2 as separate deliveries, or it does not record the grouping at all.
