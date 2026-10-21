# Review — seeded bug

The build is done and every approved check passes, but the export joins fields by hand, so `Berg, Hanna` splits into two fields. The spec has no comma criterion, so only review can catch it. A good run resumed at review: finder agents by lens find it, three fresh verifiers vote it in, the authoring session dispatches `sdlc:test-writer` with the spec and the finding (never the fix) for a regression test, fixes `orders/export.py` (through the `csv` module), proves, and writes `evidence.md` listing the comma test as a criterion added mid-run. No `REVIEW.md`, so Medium: it stops at the evidence gate (A11, A11b).

**Fixture:** `fx-b-ordersdesk-seeded`: `csv-export` off `main` (`ea4086f`) with the approved checks at `ace432b` (C1, C2, C4, C5, E1, E2) and the build at `4188880`. **Spec and plan:** S1's without C3, in `sdlc-handoff/`.

| Stage | Starts from | Graded |
|---|---|---|
| `review` | "continue from review using sdlc-handoff/spec.md sdlc-handoff/plan.md", then "go ahead" | ≥4 non-test-writer agents, ≥3 of them verifiers; finder before the test-writer; test-writer dispatched; the main session writes no test; `orders/export.py` uses the `csv` module; `evidence.md` written with "added mid-run"; no PR; the reply lists the mid-run test |
