# ADR-0001 — API payloads are parsed into typed records at the edge

**Status:** Accepted (2026-03-09)

## Context

Screens used to read fields straight out of decoded JSON, so a change in the API's payload surfaced as a crash on whichever screen touched the field first.

## Decision

Every payload from `ledger-api` is parsed into a typed record in `ledger_mobile/client.py`, and screens use only those records. The payload's field names appear nowhere else in the app.

## Consequences

- A change to the API's field names is absorbed in one function.
- The captured payload in `tests/fixtures/` must be kept in step with what the API actually sends.
