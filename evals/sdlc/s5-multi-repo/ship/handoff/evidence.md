# Evidence — Rename customerId to accountId

**Slice S1 — api** · base `main` @ `e380caa` → head `rename-customer-id-to-account-id` @ `8ce7072` · tier **Medium**
**Slice S2 — mobile** · base `main` @ `2b60831` → head `rename-customer-id-to-account-id` @ `b4b288b` · tier **Medium**

| id | repo | criterion | check | head |
|---|---|---|---|---|
| C1 | api | records carry `accountId` | `test_record_carries_account_id` | ✔ |
| C2 | api | `customerId` still emitted, equal | `test_deprecated_customer_id_matches_account_id` | ✔ |
| C3 | mobile | reads `accountId` | `test_parses_account_id` | ✔ |
| C4 | api + mobile | mobile parses every record api emits | cross-repo, `8ce7072` × `b4b288b` | ✔ 3/3 records |
| E1 | mobile | only-`customerId` payload parses | `test_parses_pre_rename_payload` | ✔ |
| P1 | api | existing suite passes (preservation) | `python3 -m unittest discover -s tests` | ✔ 6/6 |
| P2 | mobile | existing suite passes (preservation) | `python3 -m unittest discover -s tests` | ✔ 5/5 |
| P3 | docs | unchanged (preservation) | `git -C docs status --porcelain`, branches | ✔ no branch, no change |

**CI:** none configured in either repo. **Existing suites:** api ✔ 6/6, mobile ✔ 5/5 at their heads. No test file changed after the test gate outside the test-writer's commits.
**Review** (per repo): api 1 round, 0 findings held; mobile 1 round, 0 findings held. Security pass: 0 findings in each.
**Assumptions:** A1 no client other than the mobile app reads `customerId` — *untested*.
**Risk:** tier Medium in both. Merge order: `api` first, deploy it, then `mobile`. api is a two-way door; removing `customerId` later is one-way (installed app versions).
**How to revert:** api `git revert 8ce7072`; mobile `git revert b4b288b` (revert mobile first if both go).
**Follow-ups:** remove `customerId` after the two-week window.
