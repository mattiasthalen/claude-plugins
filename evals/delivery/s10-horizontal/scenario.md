# S10 — Horizontal

A storage swap. Cutting it per command leaves some commands reading JSON and some SQLite, which is worse than either end. The tree leaves slicing to the plan; a good plan cuts it horizontally (the store first, behind its unchanged interface) or as one slice, and records why.

**Fixture:** `ordersdesk`.

| Stage | Starts from | Graded |
|---|---|---|
| `plan` | the interview's tree, no slicing branch | the slicing direction is decided with a reason that rules out a mixed state |
