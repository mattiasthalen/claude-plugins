## user
/sdlc continue from prove using sdlc-handoff/intent.md sdlc-handoff/d1/spec.md sdlc-handoff/d1/plan.md

## assistant
Prove is done; this is the evidence gate. The evidence is written next to the other documents, at `sdlc-handoff/d1/evidence.md`.

This is delivery d1 of `intent.md` (story S1).

**Slice S1 — CSV export** · base `main` @ `ea4086f` → head `csv-export` @ `70147ca` · tier **Medium** (no `REVIEW.md`): the gate stops for you.

| id | criterion | check | head @ `70147ca` |
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
**How to revert:** `git revert 70147ca 6badc6d`.

This approval holds for head `70147ca` only. Approve the evidence and I'll open the pull request.

## user
Approved. Open the pull request.

## assistant
Ship stopped for delivery d1: the pull request did not open.

- Head still `70147ca`, the approved one.
- `gh auth status` failed: `You are not logged into any GitHub hosts. To log in, run: gh auth login`. So nothing was pushed: `csv-export` is not on `origin`, and no pull request exists for S1.
- The body is written at `sdlc-handoff/d1/pr-csv-export.md`.

To open it yourself once `gh` is logged in:

```
gh auth login
git push -u origin csv-export
gh pr create --base main --head csv-export --title "Export every order as CSV" --body-file sdlc-handoff/d1/pr-csv-export.md
```
