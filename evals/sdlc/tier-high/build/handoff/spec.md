# Spec — CI on Python 3.12

**Intent:** "Run CI on Python 3.12 as well as 3.11." (requester, in chat)

**Design tree:** 2 branches, all decided: [1] the matrix · [2] preservation.

## Functional spec

`.github/workflows/ci.yml` runs the suite on Python 3.11 and 3.12. Nothing but that file changes.

## Acceptance criteria

| id | criterion | branch | check |
|---|---|---|---|
| C1 | the CI matrix includes Python 3.12 | [1] | `grep -Eq 'python-version: \[[^]]*"3\.12"' .github/workflows/ci.yml` |

## Preservation criteria

| id | criterion | branch | check |
|---|---|---|---|
| P1 | the CI matrix still includes Python 3.11 | [2] | `grep -Eq 'python-version: \[[^]]*"3\.11"' .github/workflows/ci.yml` |
| P2 | the existing suite passes | [2] | `python3 -m unittest discover -s tests` |
| P3 | nothing but `.github/workflows/ci.yml` changes | [2] | `test -z "$(git diff --name-only main -- . ':(exclude).github/workflows/ci.yml')"` |
