# Assumptions

What this marketplace's designs rest on without having verified, each with how you would know it stopped holding, plus measured facts that would cost time to rediscover.

## Standing

| Id | Assumption | Area | Stops holding when |
|----|------------|------|--------------------|
| A1 | `intent`'s description ("Load only when the sdlc skill starts a change with it") keeps it from loading outside the flow. A skill with `disable-model-invocation: true` cannot be called by another skill, so intent keeps a description. | sdlc / intent | `flow-no-trigger` shows `intent` loaded, or a session outside a change request loads it. |
| A2 | `design:design-interview` honours a pitch that says its [stated] criteria are requirements and its non-goals and later stories are out of scope. | sdlc / upstream | An eval case shows the interview opening a branch on a stated non-goal. |
| A3 | Nobody but Mattias installs `sdlc`, so a breaking rebuild breaks no one else. | marketplace | Someone reports an install of `sdlc@mattiasthalen`. |
| A4 | Upstream plugins release by bumping `version` in their `plugin.json`, and Mattias runs `claude plugin update` to pick a release up (auto-update is off for this marketplace). Evals run upstream's default-branch head. | marketplace / upstream | The versions `evals/fetch-deps.sh` prints differ from `claude plugin list`, or an upstream drops `version`. |
| A5 | With `sdlc` loaded, `design:design-interview` is reached from `intent`'s hand-off and `implementation:review-cycle` by its own description, so `sdlc` names neither. | sdlc / upstream | `flow-review` or `intent-filing-no` goes red after an upstream release. |
| A6 | `sdlc` turned on from claude.ai finds its bare-name `dependencies` met by design, implementation and mattpocock-skills synced the same way. The docs cover only dependencies that name a marketplace for a synced plugin. | sdlc / claude.ai | `claude plugin list` in a cloud session shows `sdlc@synced` disabled for an unmet dependency. |

## Measured

- 2026-11-10, CLI 2.1.322: `claude plugin install sdlc@mattiasthalen` in a fresh config installs sdlc plus its three dependencies, and `claude plugin validate` alone does not fetch upstream sources (a wrong upstream `path` passes validate and fails install).

From the ship-flow eval spike, Claude Code on Linux cloud, `claude-opus-5-5`, 2026-11-10:

- `claude plugin eval` starts every run bare: no user settings, CLAUDE.md, memory, hooks or other plugins. Candidate preferences go in through `append_system_prompt`.
- AskUserQuestion is never offered in eval runs, even when listed in `allowed_tools`.
- The Artifact tool is off in eval runs, and `$TMPDIR` and home are read-only, so the proof can only be graded as shown inline.
- The git directory is read-only in the eval sandbox wherever it lives, so a case ends at its first commit attempt.
- Evals need `bubblewrap` and `socat` installed, or every case granting Bash refuses to start.
- Built-in skills (`code-review`, `simplify`, `dataviz`, `deep-research`) still load in eval runs.
- A `not_contains` grader passes vacuously on a run that errored; read `error` before trusting a score.
- Flow wording that says "when the requester says the change is small" was read as permission to ask; first-person wording with "size is my call" fixed it (kickoff 6/6).
- With all of `mattpocock-skills` loaded, no Pocock skill was called two branches into a design interview (`flow-mid-interview`, 4 of 4 runs across the red and head passes), so `sdlc` ships no hook denying them.
- A preservation criterion (`list` unchanged) cannot start red; at tests first the agent flags it to the requester instead of committing (`flow-tests-first`).
