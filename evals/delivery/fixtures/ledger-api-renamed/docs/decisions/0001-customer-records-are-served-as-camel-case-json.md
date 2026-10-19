# ADR-0001 — Customer records are served as camelCase JSON

**Status:** Accepted (2026-03-02)

## Context

The mobile app is the API's main consumer and is written in a language whose conventions are camelCase. The service is Python, whose conventions are snake_case. Field names in the payload are a contract: once a released app reads a field, renaming it breaks that app.

## Decision

Customer records are served as JSON objects with camelCase keys: `customerId`, `name`, `currency`. The Python code keeps snake_case internally and converts at the edge, in `ledger_api/customers.py`.

## Consequences

- Clients read the payload without a mapping layer.
- Any rename of a payload field is a breaking change for every released client, and needs a plan for the versions still in use.
