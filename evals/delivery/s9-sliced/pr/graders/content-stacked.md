---
type: llm
focus: trace
---

Judge one thing only: is slice 2's pull request (`csv-export-since`) set to stack on slice 1's (`csv-export`): through `gh stack`, or a `--base csv-export`, whether or not the command could run?

PASS if the run stacks it or prepares the command that would.

FAIL if slice 2 targets main, or the PRs are merged into one.
