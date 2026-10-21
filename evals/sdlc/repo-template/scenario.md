# Repo template — the repository's pull request template wins

The CSV export, approved at the evidence gate, shipped into a repo that carries `.github/pull_request_template.md` with its own sections: `## What`, `## Why`, `## Verification`. The ship stage fills the repo's template instead of Summary / Testing / Risk / How to revert, with the evidence (each criterion's check at the head and the existing suite) under Verification (A13, design [8]).

**Fixture:** `fx-c-ordersdesk-template` — `ordersdesk-csv-export-branch`'s `csv-export` on a base that adds the template: base `main` @ `1fcaa01`, capture `e44a484`, head `c7beedc`. The scaffold puts the earlier session's `spec.md`, `plan.md` and `evidence.md` under `sdlc-handoff/`, git-excluded.

| Stage | Starts from | Graded |
|---|---|---|
| `ship` | the evidence gate for `c7beedc`, "Approved. Open the pull request." | `sdlc:pr`; the template read before the body is written; the body's Write has What / Why / Verification in order, C1, E1 and the suite under Verification, no Summary / Testing / How to revert, no spec dump; `gh pr create --title … --body-file` |
