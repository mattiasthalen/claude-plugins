# Assumptions

What this marketplace's designs rest on without having verified, each with how you would know it stopped holding, plus measured facts that would cost time to rediscover.

## Standing

| Id | Assumption | Area | Stops holding when |
|----|------------|------|--------------------|
| A1 | `intent`'s description ("Load only when the sdlc skill reaches its intent step") keeps it from loading outside the flow. A skill with `disable-model-invocation: true` cannot be called by another skill, so intent keeps a description. | sdlc / intent | `flow-no-trigger` shows `intent` loaded, or a session outside a change request loads it. |
| A2 | `design:design-interview` treats a pitch's stated criteria as requirements and its non-goals and later stories as out of scope, without being told how. | sdlc / upstream | An eval case shows the interview opening a branch on a stated non-goal. |
| A4 | Nobody but Mattias installs `sdlc`, so a breaking rebuild breaks no one else. | marketplace | Someone reports an install of `sdlc@mattiasthalen`. |

## Measured

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
