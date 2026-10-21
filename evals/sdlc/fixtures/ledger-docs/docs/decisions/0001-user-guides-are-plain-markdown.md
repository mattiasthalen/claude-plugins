# ADR-0001 — User guides are plain Markdown

**Status:** Accepted (2026-02-16)

## Context

The guides are written by support staff, not developers, and are published by the help-centre tool, which renders Markdown directly.

## Decision

User guides are plain Markdown files under `guide/`, one page per task, linked relatively. There is no build step; a test checks that every relative link resolves.

## Consequences

- Anyone who can edit a text file can edit the guides.
- Guides describe what the user sees in the app, never the API or its payloads.
