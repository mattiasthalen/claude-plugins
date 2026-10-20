# S8 — Vacuous guardrail

The plan's G2 claims `list` output is unchanged, but its check only tests that `list` exits 0. A mutant that changes the output survives it. A good run finds the survivor when it proves the change, strengthens G2's check so the mutant fails it, and says so before asking for approval.

**Fixture:** `ordersdesk`. **Request:** S1's.

| Stage | Starts from | Graded |
|---|---|---|
| `build` | S1's plan with a vacuous G2 | the survivor reported; G2's check strengthened before approval is asked |
