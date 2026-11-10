# ADR-0002 — The warehouse gets the count from a nightly workflow

**Status:** Accepted (2026-10-13)

## Context

The warehouse team wants the order count on their board before the 06:00 shift. The board reads a file the repository publishes.

## Decision

A GitHub Actions workflow, `.github/workflows/nightly-count.yml`, runs `python3 -m orders count` on `schedule: cron: "0 2 * * *"`, which fires at 02:00 Stockholm time (A2), and publishes the output for the board.

Rejected: **a server that answers on request**, a service to run for one number a day.

## Consequences

- The count on the board is at most one day old.
