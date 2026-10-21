# Plan — CI on Python 3.12

Spec: `sdlc-handoff/spec.md` (approved).

## Slices

| slice | repo | base | branch | direction | PR |
|---|---|---|---|---|---|
| S1 CI matrix | ordersdesk | `main` | `ci-python-3-12` | vertical: ships on its own | one ready PR |

## Approach

- Edit `.github/workflows/ci.yml` only: add `"3.12"` to `matrix.python-version`.

## Checks

- C1, P1, P2, P3: the commands in the spec, run as they are. No test file: every check is a command.

## Progress

- [x] Spec gate
- [x] Plan gate
- [x] Test gate: all four checks are commands in the spec; no test file was written
- [ ] Build
- [ ] Review
- [ ] Prove
- [ ] Evidence gate
- [ ] Ship
