# S9 — Sliced

Two slices in one repo, built as stacked branches. One PR per slice, stacked: through `gh stack` when it is installed, else slice 2's PR based on slice 1's branch with a merge note.

**Fixture:** `ordersdesk-sliced` (`csv-export` on `main`, `csv-export-since` on `csv-export`).

| Stage | Starts from | Graded |
|---|---|---|
| `pr` | approved evidence for both slices | two PR commands; stacked by `gh stack` or `--base csv-export`; a merge note |
