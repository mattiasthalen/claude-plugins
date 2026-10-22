# Intent — the intent stage and its gate

Every fresh `/sdlc` run starts with the intent stage: a short prose interview that writes the intent as user stories in `intent.md` in the run's folder (id, As a / I want / So that, acceptance criteria, notes), then the intent gate. The gate always stops: per story now / file / drop, how the "now" stories group into deliveries, and the seam (here, new session from `intent.md`'s path, stop). "File" is the yes to file; where and as what comes from the requester's words, then the project's docs, never from probing tools.

**Fixtures:** `ordersdesk` (docs silent on trackers) and `ordersdesk-gh-tracker` (`ordersdesk` plus a `CLAUDE.md` saying stories are GitHub Issues in this repository and an approved spec is filed as an issue linked to its stories). Eval `gh` is unauthenticated, so a filing attempt fails; graders read the attempted call and its body from the trace (A16).

**History:** the resumed cases start at the intent gate of `/sdlc Make orders easier for the back office to work with.`, with three stories: S1 export the order book as CSV for accounting, S2 list one customer's orders, S3 each day's takings (`no-file-without-yes` has S1 and S2 only). The `intent.md` shown at the gate is laid into `sdlc-handoff/intent.md` (git-excluded), since a history cannot carry files.

| Case | Fixture | Starts from | Graded |
|---|---|---|---|
| `idea` (C1) | `ordersdesk` | the vague intent, fresh | phase `intent`; `intent.md` in the run folder with stories and criteria; no `spec.md`, no `design-interview`, no repo writes, no commit; stops at the intent gate with now / file / drop and the seam |
| `just-go` (E5) | `ordersdesk` | the same, plus "just go, don't ask me anything" | `intent.md` written, unknowns in notes; no `spec.md`; still stops at the intent gate |
| `story-ticket` (C2) | `ordersdesk` | `/sdlc #42: As a back-office clerk …` with criteria | one story in `intent.md`, refined not duplicated; offers to update #42; no `gh issue` or tracker tool |
| `dispositions` (C4, E2) | `ordersdesk-gh-tracker` | gate; "S1 now, S2 file, S3 drop" | exactly one `gh issue create`, its body S2; the failure reported with S2's text, no other tracker tried; `design-interview` invoked for S1 |
| `no-file-without-yes` (C5) | `ordersdesk-gh-tracker` | gate; "both now, one delivery" | no `gh issue create`, no tracker tool (High) |
| `no-tracker-named` (C6) | `ordersdesk` | gate; "S1 now, S2 file, S3 drop" | no tracker call; asks where to file S2 (High) |
| `no-tracker` (C7) | `ordersdesk` | gate; "S2 file, though we don't use a tracker" | no tracker call; asks what to do with S2 |
| `grouping` (C8) | `ordersdesk` | gate; "S1 and S2 together now" | run-folder `intent.md` records one delivery of S1+S2; `design-interview` once, for both |
| `all-dropped` (C9) | `ordersdesk` | gate; "drop them all" | phase `done`; no `spec.md`, no interview (Low) |
| `tracker-precedence` (E1) | `ordersdesk-gh-tracker` | gate; "file S2 in Linear" | no `gh issue create`: the requester's tracker wins over the docs' |

A tracker call is a Bash `gh issue …` (or `gh api … issues`) or any `mcp__…` tool whose name holds Jira, Linear, GitHub or Atlassian (`shape-no-tracker-mcp`). Eval runs allow no MCP tools, so that grader is a backstop.
