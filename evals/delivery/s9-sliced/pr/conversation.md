## user
/delivery:delivering-pitches Add a CSV export of orders, with a --since date so accounting can pull only new orders.

## assistant
Here is the plan. Nothing has been changed yet.

## Design
1. **Scope** — decided. `export --csv <path>` then `--since <YYYY-MM-DD>`.
2. **Slicing** — decided. Two vertical slices: the export ships on its own; the filter builds on it. Fork: one slice rejected, because accounting can use the plain export a week earlier.

## Brief
Slice 1 — A1 [1] export writes the file · A2 [1] header · A3 [1] every order in `list` order · A4 [1] comma and UTF-8. Slice 2 — B1 [1] `--since` keeps later orders · B2 [1] inclusive · B3 [1] bad date is a usage error. Guardrails: G1 suite, G2 `list` byte-identical, G3 data unchanged. Each with a test in `tests/`.

## Slices
| Slice | Repo | Base | Direction | PR |
|---|---|---|---|---|
| S1 `csv-export` | ordersdesk | `main` | vertical | PR 1 |
| S2 `csv-export-since` | ordersdesk | `csv-export` | vertical | PR 2, stacked on PR 1 |

## Progress
- [ ] Build S1 · [ ] Build S2 · [ ] Review · [ ] Evidence and gate · [ ] Pull requests

Approve the plan and I'll build it.

## user
Approved — go ahead.

## assistant
**Claim.** Before: no export. Now accounting can export every order, and pull only orders since a date.

**Slice 1 — `csv-export`** · base `main` @ `ae6e79b` → head @ `eb167f1`: A1–A4 ✘ `invalid choice: 'export'` → ✔.
**Slice 2 — `csv-export-since`** · base `csv-export` @ `eb167f1` → head @ `df203a7`: B1, B2 ✘ `unrecognized arguments: --since` → ✔; B3 ✘ exit 2 for the wrong reason → ✔ `invalid fromisoformat value: '3/9'`.
**Guardrails:** G1 suite 1/1 → 5/5 → 8/8 · G2 `list` byte-identical · G3 data unchanged; each with a mutant → ✘.
**Merge Danger:** two-way doors; slice 2 merges after slice 1.

Approve the result and I'll open the pull requests.
