# Evidence — CSV export of orders, with --since

**Slice 1 — `csv-export`** · base `main` @ `ea4086f` → head @ `7871671` · tier **Medium**

| id | criterion | check | head @ `7871671` |
|---|---|---|---|
| C1 | exits 0; header | `test_writes_header_and_every_order_in_list_order` | ✔ |
| C2 | every order once, in `list` order | same test | ✔ |
| C3 | comma field, UTF-8 without BOM | `test_comma_stays_one_field_and_non_ascii_survives` | ✔ |
| C4 | two decimals, ISO dates | `test_totals_keep_two_decimals_and_dates_are_iso` | ✔ |
| E1 | missing `--csv` is a usage error | `test_missing_csv_is_a_usage_error` | ✔ |
| P1 | existing suite (preservation) | `python3 -m unittest discover -s tests` | ✔ 5/5 |
| P2 | `list` byte-identical (preservation) | base output vs head | ✔ |
| P3 | data unchanged (preservation) | `git diff --exit-code main -- data/orders.json` | ✔ |

**Slice 2 — `csv-export-since`** · base `csv-export` @ `7871671` → head @ `487969e` · tier **Medium**

| id | criterion | check | head @ `487969e` |
|---|---|---|---|
| C5 | `--since` keeps later orders | `test_since_keeps_only_later_orders` | ✔ |
| C6 | `--since` is inclusive | `test_since_includes_the_day_itself` | ✔ |
| E2 | bad date is a usage error | `test_bad_since_is_a_usage_error` | ✔ `invalid fromisoformat value: '3/9'` |
| P1 | existing suite (preservation) | `python3 -m unittest discover -s tests` | ✔ 8/8 |
| P2 | `list` byte-identical (preservation) | base output vs head | ✔ |
| P3 | data unchanged (preservation) | `git diff --exit-code main -- data/orders.json` | ✔ |

**CI:** none configured. No test file changed after the test gate outside the test-writer's commits.
**Review:** slice 1, 1 round, 0 findings held; slice 2, 1 round, 0 findings held. Security pass: 0 findings.
**Risk:** two-way doors. Slice 2 is stacked on slice 1 and merges after it; once slice 1 merges, slice 2's PR is retargeted to `main`.
**How to revert:** slice 2 `git revert 487969e`; slice 1 `git revert 7871671` (slice 2 first).
