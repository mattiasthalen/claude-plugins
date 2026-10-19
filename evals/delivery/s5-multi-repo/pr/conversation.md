## user
/delivery:delivering-pitches Rename customerId to accountId across the API (api/) and the mobile client (mobile/). The mobile app has to keep working with the API during the rollout.

## assistant
Here is the plan. Nothing has been changed yet.

## Design
1. **Scope** — decided. Rename the customer record's `customerId` to `accountId` in `api/` and `mobile/`. `docs/` never mentions it and stays untouched.
2. **Compatibility window** — decided. For one release the API emits both fields with the same value; mobile reads `accountId`, falling back to `customerId`. Fork: a hard switch rejected, because mobile releases lag API deploys by two weeks.
3. **Record ownership** — decided. The window is an API contract decision: ADR in `api/`, pointer ADR in `mobile/`.
4. **Rollout** — decided. `api` merges and deploys first, then `mobile`.

## Brief — Rename customerId to accountId
- D1 [1] api records carry `accountId`. Check: `test_record_carries_account_id`.
- D2 [2] `customerId` still emitted, equal to `accountId`. Check: `test_deprecated_customer_id_matches_account_id`.
- D3 [1] mobile `parse_customer` reads `accountId`. Check: `test_parses_account_id`.
- E1 [2] a payload with only `customerId` still parses. Check: `test_parses_pre_rename_payload`.
- C1 [2] mobile's branch parses every record api's branch emits. Check: cross-repo, both work branches.
- G1 [1] `api` suite passes. G2 [1] `mobile` suite passes. G3 [1] `docs` unchanged.

## Slices
| Slice | Repo | Base | Direction | PR |
|---|---|---|---|---|
| S1 api | api | `main` | vertical | one ready PR, merges first |
| S2 mobile | mobile | `main` | vertical | one ready PR, merges after api deploys |

## Capture
- api ADR-0002 (← 2, 3); mobile pointer ADR-0002 (← 3).

## Progress
- [ ] Capture · [ ] Build · [ ] Review · [ ] Evidence and gate · [ ] Pull requests

Approve the plan and I'll build it.

## user
Approved — go ahead.

## assistant
**Claim.** Before: the API only sent `customerId`, so renaming it would break every installed app. Now `api` sends both for one release and `mobile` reads `accountId`, falling back to `customerId`.

**Slice S1 — api** · base `main` @ `c528721` → head `rename-customer-id-to-account-id` @ `ef62c95`
**Slice S2 — mobile** · base `main` @ `8f08c6a` → head `rename-customer-id-to-account-id` @ `8bbd47a`

| | Repo | Criterion | Check | Base | Head |
|---|---|---|---|---|---|
| D1 | api | records carry `accountId` | `test_record_carries_account_id` | ✘ `KeyError: 'accountId'` | ✔ |
| D2 | api | `customerId` still emitted, equal | `test_deprecated_customer_id_matches_account_id` | ✘ `KeyError: 'accountId'` | ✔ |
| D3 | mobile | reads `accountId` | `test_parses_account_id` | ✘ `AttributeError: 'Customer' object has no attribute 'account_id'` | ✔ |
| E1 | mobile | only-`customerId` payload parses | `test_parses_pre_rename_payload` | ✘ `AttributeError` | ✔ |
| C1 | api + mobile | mobile parses every record api emits | cross-repo, both work branches | ✘ `AttributeError` | ✔ 3/3 |

**Guardrails:** G1 `api` suite 4/4 → 6/6 (mutant: `customerId` dropped → ✘) · G2 `mobile` suite 3/3 → 5/5 (mutant: fallback removed → ✘) · G3 `docs` no branch, no commit (mutant: a touched guide → ✘).
**Review:** api and mobile each reviewed at their tops; 0 findings held.
**Assumptions:** no client other than the mobile app reads `customerId` — *untested*.
**Merge Danger:** `api` first, deploy it, then `mobile`. api is a two-way door; removing `customerId` later is one-way (installed app versions).
**Follow-ups:** remove `customerId` after the two-week window.

Approve the result and I'll open the pull requests.
