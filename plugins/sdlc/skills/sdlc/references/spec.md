# Spec

The intent is the delivery's stories. A document handed in without stories is taken as it arrives: if it holds more than one change, name the changes and ask which one to deliver, then stop.

Invoke `design:design-interview` and run it through its Phase 8 wrap-up; ask its questions in prose. Skip it only when the requester says the change is small; then lay out a short tree yourself, saying who closed each choice.

Then write `spec.md`: the acceptance criteria and edge cases in the shape of design-interview's `references/artifacts.md`. Every criterion and edge case carries the story it serves (or "all"), the design branch it came from, as `[n]`, and its check; the spec may add criteria no story asked for, marked as its own. Each check is a command, or "judged" with the rubric a fresh reviewer will apply; the edge cases get a check column too, and every row fills it: a case with nothing to check is out of scope and goes under Non-criteria. A choice the tree left open becomes a branch the spec adds, numbered after the tree's and marked as the spec's own. "This must not change" is a preservation criterion, checked green at the base and the head.

Write no code, not even in a copy to try a check: the test stage runs the checks. End at the spec gate.

After the spec gate's yes, publish the spec when the requester or the project's docs say to, where and as what they say, linked to its stories: the body is the spec's content, never a path into the run's folder. When a spec already published is amended and approved again, offer to update the published item, and update it only on a yes.
