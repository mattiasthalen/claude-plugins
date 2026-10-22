---
type: llm
focus: trace
---

Judge one thing only, on the Bash `gh issue create` call in the trace (its `--title` and its `--body`, or the content of the file its `--body-file` / `-F` points to, read from the Write or Bash call that wrote that file): is what it files S2, the clerk's "find a customer's orders" story?

PASS if the issue's body holds S2's story (as a back-office clerk … list only the orders of the customer I name … so that …) and its acceptance criteria, and holds nothing of S1 (the CSV export) or S3 (daily takings).

FAIL if there is no `gh issue create` call, its body is S1 or S3 or several stories, its body is only a title or a path to a file in the run folder, or the body cannot be found in the trace.
