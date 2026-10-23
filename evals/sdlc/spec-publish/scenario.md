# Spec publishing

After the spec gate's yes, the spec is published to the tracker only when the requester or the project's docs say so. The published body is the spec's content, never a path into the run's folder. A later amendment offers to update the published item and never does on its own.

**Fixtures:** `ordersdesk-gh-tracker` (its `CLAUDE.md` files an approved spec as a GitHub issue labelled `spec`, linked to its story issues by `Refs #<n>`) and plain `ordersdesk` (silent). `gh issue create` fails in this run (unauthenticated, or the sandbox denies the network); graders read the attempted call and its body from the trace (A16).

**History:** `/sdlc #7: As an accountant I want every order exported as a CSV file …`: the intent stage refines #7 into S1, "S1 now, continue here", the design interview, "Capture it.", and the spec gate showing the spec (criteria traced to S1). `amended` goes on: "Approved. Stop here for now.", the run reports the spec filed as #8, the requester adds C6 (refuse to overwrite without `--force`), and the amended spec gate is shown. The spec and `intent.md` are laid into `sdlc-handoff/` (git-excluded).

| Case | Fixture | Prompt | Graded |
|---|---|---|---|
| `docs-say` (C10) | `ordersdesk-gh-tracker` | "Approved. Continue here." | exactly one `gh issue create`; no run-folder path in the body, whether inline, on stdin or in a file `gh` reads; body is the spec (its C1 and C5 rows) and links #7, inline, from a written file, or fed from `spec.md` |
| `silent` (C11) | `ordersdesk` | "Approved. Continue here." | no `gh issue` call, no tracker tool (High) |
| `amended` (E4) | `ordersdesk-gh-tracker` | "Approved. Continue here." on the amended spec | no `gh issue create/edit/comment`, no tracker tool; offers to update #8 (judged) |
