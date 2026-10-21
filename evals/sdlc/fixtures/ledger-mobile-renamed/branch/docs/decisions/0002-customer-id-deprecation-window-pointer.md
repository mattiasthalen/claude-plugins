# ADR-0002 — Follow ledger-api's one-release window for customerId

**Status:** Accepted (2026-10-13)

## Context

ledger-api renames `customerId` to `accountId` and emits both for one release. The decision and its reasons live in ledger-api's ADR-0002, `docs/decisions/0002-customer-records-emit-both-ids-for-one-release.md` in that repo.

## Decision

**The app reads `accountId`, and falls back to `customerId` when a payload has no `accountId`.**

## Consequences

- The fallback is removed when ledger-api stops emitting `customerId`.
