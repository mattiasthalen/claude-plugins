# S1 — Clear feature

A small, well-defined request on one repo. It carries the baseline expectations for every stage: the interview is delegated to `design:design-interview`, the plan carries the tree and a brief with guardrails, the build ends at an evidence gate, and the pull request follows the agreed body.

**Fixture:** `ordersdesk` (intake, plan, build, gate) and `ordersdesk-csv-export-branch` (the export built on `csv-export`, for the PR stage).

**Request:** `/delivery:delivering-pitches Add a CSV export of all orders: python3 -m orders export --csv <path> should write every order with a header row.`

**Planted:** `data/orders.json` holds `Berg, Hanna` (a comma) and `Åkesson & Dotter` (non-ASCII); totals are Decimal with two places (`89.50`).

| Stage | Starts from | Graded |
|---|---|---|
| `intake` | the bare request | the interview is delegated; no writes; no option picker; a progress list |
| `plan` | the interview's Phase 8 tree | a fresh subagent checks the plan; the plan has the tree, a brief with guardrails and branch tags, slices, capture and progress; no writes |
| `build` | the approved plan | capture through `design:adr`; `review-cycle`; tasks per criterion; evidence with base/head and guardrail mutants; the page; no PR before approval |
| `gate` | evidence + a conditional yes | the change is made, checks rerun, review-cycle rerun, approval asked again, no PR |
| `pr` | approved evidence on `csv-export` | `delivery:pr`; the body kept in `.delivering-pitches/` with Summary / Brief / Evidence / Merge Danger, one `<details>`, no images; the unreachable remote reported with its fix |
