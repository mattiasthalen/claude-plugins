# Build

Add one task per criterion and edge case by its id, and tick each when its check passes at HEAD.

Build each slice on its branch, in the plan's order, with atomic commits staged by path, until its checks pass. The tests are fixed: a check that looks wrong goes to the evidence gate as a stop, for a re-plan.

A criterion still red after a fair try stops the run: go to prove, which leads the evidence with it.
