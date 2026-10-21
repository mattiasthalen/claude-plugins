# Spec — README: list order and a Development section

**Intent:** "In the README, say that `orders list` prints oldest first, and add a Development section that says how to run the tests." (requester, in chat)

**Design tree:** 3 branches, all decided: [1] what `list` promises · [2] where the test command lives · [3] preservation.

## Functional spec

`README.md` says that `python3 -m orders list` prints every order oldest first, and gains a `## Development` section with the test command. Nothing but `README.md` changes.

## Acceptance criteria

| id | criterion | branch | check |
|---|---|---|---|
| C1 | the README says `orders list` prints oldest first | [1] | `grep -q 'oldest first' README.md` |
| C2 | the README has a `## Development` section holding `python3 -m unittest discover -s tests` | [2] | `awk '/^## Development$/{f=1} f && /python3 -m unittest discover -s tests/{ok=1} END{exit !ok}' README.md` |

## Preservation criteria

| id | criterion | branch | check |
|---|---|---|---|
| P1 | the existing suite passes | [3] | `python3 -m unittest discover -s tests` |
| P2 | nothing but `README.md` changes | [3] | `test -z "$(git diff --name-only main -- . ':(exclude)README.md')"` |
