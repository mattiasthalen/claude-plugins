# Spec — Rename customerId to accountId

**Intent:** "Rename customerId to accountId across the API (api/) and the mobile client (mobile/). The mobile app has to keep working with the API during the rollout." (requester, in chat)

**Design tree:** 4 branches, all decided: [1] scope · [2] compatibility window · [3] record ownership · [4] rollout.

**Assumptions:** A1 — no client other than the mobile app reads `customerId`. Stops holding when: another consumer of `ledger-api` turns up.

## Functional spec

The customer record's `customerId` becomes `accountId` in `api/` and `mobile/`. For one release the API emits both fields with the same value; mobile reads `accountId`, falling back to `customerId`. `docs/` never mentions the field and stays untouched. `api` merges and deploys first, then `mobile`.

## Acceptance criteria

| id | repo | criterion | branch | check |
|---|---|---|---|---|
| C1 | api | records carry `accountId` | [1] | `test_record_carries_account_id` |
| C2 | api | `customerId` is still emitted, equal to `accountId` | [2] | `test_deprecated_customer_id_matches_account_id` |
| C3 | mobile | `parse_customer` reads `accountId` | [1] | `test_parses_account_id` |
| C4 | api + mobile | mobile's branch parses every record api's branch emits | [2] | cross-repo: mobile's `parse_customer` over `python3 -m ledger_api customers`, both work branches |

## Preservation criteria

| id | repo | criterion | branch | check |
|---|---|---|---|---|
| P1 | api | the existing suite passes | [1] | `python3 -m unittest discover -s tests` in `api/` |
| P2 | mobile | the existing suite passes | [1] | `python3 -m unittest discover -s tests` in `mobile/` |
| P3 | docs | unchanged | [1] | `git -C docs status --porcelain` empty, no branch |

## Edge cases

| id | repo | case | branch | check |
|---|---|---|---|---|
| E1 | mobile | a payload with only `customerId` still parses | [2] | `test_parses_pre_rename_payload` |
