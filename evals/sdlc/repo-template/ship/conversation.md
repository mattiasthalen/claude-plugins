## user
/sdlc continue from prove using sdlc-handoff/spec.md sdlc-handoff/plan.md

## assistant
Prove is done; this is the evidence gate. The evidence is written next to the other documents, at `sdlc-handoff/evidence.md`.

**Slice S1 — CSV export** · base `main` @ `1fcaa01` → head `csv-export` @ `c7beedc` · tier **Medium** (no `REVIEW.md`): the gate stops for you.

| id | criterion | check | head @ `c7beedc` |
|---|---|---|---|
| C1 | exits 0; header `id,customer,total,placed_on` | `test_writes_header_and_every_order_in_list_order` | ✔ |
| C2 | every order once, in `list` order | same test | ✔ |
| C3 | `Berg, Hanna` stays one field | `test_comma_stays_one_field_and_non_ascii_survives` | ✔ |
| C4 | UTF-8, no BOM, `Åkesson & Dotter` intact | same test | ✔ |
| C5 | `89.50`, ISO dates | `test_totals_keep_two_decimals_and_dates_are_iso` | ✔ |
| E1 | missing `--csv` is a usage error | `test_missing_csv_is_a_usage_error` | ✔ `the following arguments are required: --csv` |
| P1 | `list` byte-identical (preservation) | base output from the test gate vs `python3 -m orders list` | ✔ identical |
| P2 | data unchanged (preservation) | `git diff --exit-code main -- data/orders.json` | ✔ |
| P3 | existing suite passes (preservation) | `python3 -m unittest discover -s tests` | ✔ 5/5 |

**CI:** none configured. **Existing suite:** ✔ 5/5 at the head. No test file changed after the test gate outside the test-writer's commits.
**Review:** 2 rounds. 1 fixed (E1 asserted only "usage", which the old CLI also printed; the test-writer tightened it to the missing-`--csv` message, added mid-run), 0 closed with a reason, 0 pre-existing. Security pass: 0 findings.
**Assumptions:** A1 accounting accepts RFC 4180 quoting — *untested* (no access to the importer).
**Risk:** tier Medium. Two-way door: a new command nothing reads yet. Blast radius: the `orders` CLI.
**How to revert:** `git revert c7beedc e44a484`.

This approval holds for head `c7beedc` only. Approve the evidence and I'll open the pull request.
