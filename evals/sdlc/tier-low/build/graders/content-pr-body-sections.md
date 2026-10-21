---
type: llm
focus: trace
---

Judge one thing only: find the Write tool call (or `cat >` heredoc) that drafts the pull request body, the file later passed to `gh pr create --body-file`. Does that body have the sections Summary, Testing, Risk and How to revert, with Testing holding each criterion's check result at the head (C1, C2, P1, P2)?

PASS if the drafted body has all four sections and Testing lists the criteria's results.

FAIL if no drafted body is visible, a section is missing, Testing has no per-criterion results, or the body pastes the whole spec.
