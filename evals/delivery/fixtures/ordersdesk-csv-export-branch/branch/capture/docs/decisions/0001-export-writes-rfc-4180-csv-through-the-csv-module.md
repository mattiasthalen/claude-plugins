# ADR-0001 — Export writes RFC 4180 CSV through the csv module

**Status:** Accepted (2026-10-13)

## Context

`python3 -m orders export --csv <path>` feeds accounting's importer, which reads standard UTF-8 CSV with a header row. Customer names hold commas (`Berg, Hanna`) and non-ASCII (`Åkesson & Dotter`).

## Decision

Rows are written with Python's `csv` module (RFC 4180 quoting), UTF-8 without a byte-order mark. Joining fields by hand was rejected: a comma in a name would split the field.

## Consequences

The file is a contract with accounting's importer; changing the dialect means changing theirs.
