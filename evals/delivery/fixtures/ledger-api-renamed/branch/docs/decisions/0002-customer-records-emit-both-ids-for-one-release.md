# ADR-0002 — Customer records emit accountId and customerId for one release

**Status:** Accepted (2026-10-13)

## Context

`customerId` is renamed to `accountId`. Mobile releases reach users about two weeks after an API deploy, so app versions already installed read `customerId` from the new API until the next app release is out. ADR-0001 makes a payload field name a contract.

## Decision

**The API emits both `accountId` and `customerId`, with the same value, for one release.** `customerId` is removed once the mobile release that reads `accountId` has shipped. This repo owns the decision; ledger-mobile carries a pointer to it.

## Consequences

- Installed app versions keep working through the rollout.
- The payload carries a duplicate field until removal, a follow-up in this repo.
