# Spec

The intent is the delivery's stories. A document handed in without stories is taken as it arrives: if it holds more than one change, name the changes and ask which one to deliver, then stop.

Invoke `design:design-interview` and run it to its end; ask its questions in prose. Invoking it is the user's request for its capture, so when the tree is complete capture runs without asking. Capture writes under the run's folder: each record in `capture/<repo>/`, `<repo>` being the repository's name as the plan's slices will name it, at the repo-relative path the interview chooses, and whole: a record that amends a file the repo already has starts from the repo's current copy. The brief goes in `brief/`. A gap capture reports goes to the requester, and the run waits for the answer. Skip the interview only when the requester says the change is small; then lay out a short tree yourself, saying who closed each choice.

Once capture has finished, write `spec.md`: the acceptance criteria and edge cases in the shape of design-interview's `references/artifacts.md`. Every criterion and edge case carries the story it serves (or "all"), the design branch it came from, as `[n]`, and its check; the spec may add criteria no story asked for, marked as its own. Each check is a command, or "judged" with the rubric a fresh reviewer will apply; the edge cases get a check column too, and every row fills it: a case with nothing to check is out of scope and goes under Non-criteria. A choice the tree left open becomes a branch the spec adds, numbered after the tree's and marked as the spec's own. "This must not change" is a preservation criterion, checked green at the base and the head.

Write no code, not even in a copy to try a check: the test stage runs the checks. End at the spec gate.
