# S9 — Sliced

Two slices in one repo, built as stacked branches. One PR per slice, stacked: through `gh stack` when it is installed, else slice 2's PR based on slice 1's branch with a merge note in its Risk. Each body carries only its slice's criteria. Ported from `delivery`'s S9 (A18).

**Fixture:** `ordersdesk-sliced` (`csv-export` @ `7871671` on `main` @ `ea4086f`, `csv-export-since` @ `487969e` on `csv-export`). The scaffold puts the earlier session's `spec.md`, `plan.md` and `evidence.md` under `sdlc-handoff/`, git-excluded.

| Stage | Starts from | Graded |
|---|---|---|
| `ship` | the evidence gate for both slices, "Approved. Open the pull requests." | `sdlc:pr`; two `gh pr create --body-file`; slice 2 `--base csv-export` or `gh stack`; slice 1's Testing has C1 and not C5, slice 2's has C5 and not C1; slice 2's Risk says it merges after slice 1 (or retargets/rebases); no spec dump; the reply names both and the stacking |
