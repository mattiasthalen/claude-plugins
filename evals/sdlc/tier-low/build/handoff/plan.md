# Plan — README: list order and a Development section

Spec: `sdlc-handoff/spec.md` (approved).

## Slices

| slice | repo | base | branch | direction | PR |
|---|---|---|---|---|---|
| S1 README | ordersdesk | `main` | `readme-development` | vertical: ships on its own | one ready PR |

## Approach

- Edit `README.md` only: one line on `list` order next to the `list` command, and a `## Development` section moving the test command under it.

## Checks

- C1, C2, P1, P2: the commands in the spec, run as they are. No test file: every check is a command.

## Progress

- [x] Spec gate
- [x] Plan gate
- [x] Test gate: all four checks are commands in the spec; no test file was written
- [ ] Build
- [ ] Review
- [ ] Prove
- [ ] Evidence gate
- [ ] Ship
