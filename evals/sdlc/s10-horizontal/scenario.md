# S10 — Horizontal

A storage swap (A18, ported from `delivery`). Cutting it per command leaves some commands reading JSON and some SQLite, which is worse than either end. The tree leaves slicing to the plan; a good plan cuts it horizontally (the store first, behind its unchanged interface) or as one slice, and records why.

**Fixture:** `ordersdesk`. The approved spec (`plan/handoff/spec.md`) is laid into `sdlc-handoff/`, uncommitted.

| Stage | Starts from | Graded |
|---|---|---|
| `plan` | the spec gate, approved, "continue here" | `plan.md` written in the docs dir; the slicing direction decided with a reason that rules out a mixed state; no repo writes, no test-writer, no interview; stops at the plan gate |
