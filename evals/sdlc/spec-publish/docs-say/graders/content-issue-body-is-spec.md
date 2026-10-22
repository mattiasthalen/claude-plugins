---
type: llm
focus: trace
---

Judge one thing only, on the Bash `gh issue create` call in the trace (its `--body`, or the content of the file its `--body-file` / `-F` points to, read from the Write or Bash call that wrote that file): the project's `CLAUDE.md` says an approved spec is filed as a GitHub issue with the spec as its body, linked to its story issue(s). Is that what was filed?

PASS if the issue's body carries the spec's content (its acceptance criteria C1–C5 with their checks, at least in substance, and the preservation criteria or edge cases), links story #7 (`Refs #7`, `#7`, or a link to it), and holds no path into the run's folder (`$TMPDIR/sdlc-…/`, `…/sdlc/…`, `sdlc-handoff/…`) in place of the content.

FAIL if there is no `gh issue create` call, the body is only a summary or a pointer to a file, the criteria are missing, #7 is not linked, or the body cannot be found in the trace.
