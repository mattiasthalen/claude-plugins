# Assumptions

What this marketplace's designs rest on without having verified, each with how you would know it stopped holding, plus measured facts that would cost time to rediscover.

## Standing

| Id | Assumption | Area | Stops holding when |
|----|------------|------|--------------------|
| A2 | The exodus skills stay callable by qualified name with a stable hand-off from design-interview's Phase 8 wrap-up, at the `sha` the marketplace pins. | sdlc / upstream | A spec-stage eval fails after a pin bump. |
| A3 | The Artifact tool is off in `claude plugin eval` runs. | evals | A probe finds the Artifact tool present. |
| A7 | TaskCreate/TaskUpdate run in eval cases that list them in `allowed_tools`. | evals | A case listing them shows no Task calls in any run. |
| A8 | `gh` is unauthenticated in eval runs, and a `gh pr create --body` stays visible to graders. | evals | A probe's `gh auth status` succeeds. |
| A12 | The session scratchpad survives for the life of its session, so a chip given its documents' absolute paths can still read them when it starts. Reading them was probed (Measured); their lifetime was not. | sdlc / seams | A resumed stage finds a named document gone. |
| A13 | A model-invocable skill fires from a session-sent first message in a chipped session. | sdlc / seams | A chip asked to continue from a stage sits idle until the requester types. |
| A14 | The repository lets GitHub Actions create pull requests ("Allow GitHub Actions to create and approve pull requests"), which the weekly vendor refresh needs. Applied with branch protection at ship. | repo / CI | `gh api repos/mattiasthalen/claude-plugins/actions/permissions/workflow --jq .can_approve_pull_request_reviews` is false, or a refresh run fails at `gh pr create`. |
| A15 | A `validate` run dispatched on a bot PR's branch satisfies `main`'s required `validate` check, even though the PR's own `pull_request` run waits for approval. | repo / CI | The first bot refresh PR shows `validate` pending or required after the dispatched run is green. |

## Documented

- Plugin `dependencies` given as bare names resolve against the plugin's own marketplace (plugin manifest reference). `implementation` needs `design >=0.7.0`. Tripwire after merge: `claude plugin install sdlc@mattiasthalen` must also install both.
- TaskCreate and TaskUpdate are on by default only on Opus 4.7, Sonnet 4.6, Haiku 4.5 and earlier models. Elsewhere they are off unless opted in (`CLAUDE_CODE_ENABLE_TODO_TOOLS=1`, `--allowedTools TaskCreate`), and `CLAUDE_CODE_ENABLE_TASKS=0` swaps them for TodoWrite (tools reference). Listing them in an eval case's `allowed_tools` opts in, so the suite never sees a session without them.

- The desktop app's task-list tool takes a plan of one to twelve steps (its own schema) and does not exist in eval runs, where only Claude Code's tools are offered.

- PreToolUse hook input carries `session_id`, `cwd`, `scratchpad_dir` (absent without a scratchpad; Claude Code ≥ 2.1.257), `tool_name` and `tool_input`, and `agent_id` and `agent_type` when a subagent calls the tool (hooks reference). A plugin's agent `agents/test-writer.md` is dispatched as `sdlc:test-writer`; `claude plugin eval` loads a plugin's agents and a case reaches them through `Agent` in `allowed_tools` (sub-agents, plugin-evals references).
- A `git-subdir` marketplace source takes `ref` and a full 40-character `sha`; with both, `sha` wins (marketplace reference).
- Skill frontmatter `user-invocable: false` hides a skill from the `/` menu (skills reference).
- Events from `GITHUB_TOKEN` create no workflow runs, except `workflow_dispatch` and `repository_dispatch`, which always do; `pull_request` runs on a PR it opened wait in an approval-required state (GitHub docs, `GITHUB_TOKEN`).

## Measured

Probes in `evals/probes/`, Claude Code 2.1.302, `claude-opus-5-5`, 2026-10-20. Rerun after a Claude Code upgrade.

- Plan-mode tools are absent in eval runs: EnterPlanMode and ExitPlanMode are never called (`plan-mode`).
- The Artifact tool is absent in eval runs (`artifact`).
- `gh pr create` exits 4 with "please run: gh auth login"; the `--body` is visible in the trace (`gh-pr`).
- `/usr/bin/git` fails: the xcrun shim cannot write its cache in the sandbox (exit 72). `/opt/homebrew/bin/git` commits and branches. `worktree add` runs its checkout as a child `git` found on PATH, the shim, so it fails; `--no-checkout` then `reset --hard` with Homebrew's git works, as does `git archive` (`git-in-sandbox`; s1-build traces). `python3` works.
- TaskCreate and TaskUpdate work when listed in `allowed_tools` (`task-tools`).
- Writes to `/tmp` are refused by the sandbox; `$TMPDIR` is writable. Writes into the workspace's `.git/` are refused by the permission layer (`write-scope`).
- Fixture SHAs match across machines only with user git config off: a signing config changes every commit (`GIT_CONFIG_GLOBAL=/dev/null` in the scaffold).
- In a sandboxed eval run the Bash tool's `$TMPDIR` is `<the hook's TMPDIR>/claude-<uid>`; the stage hook looks in both, and in a fresh `/sdlc` run it finds `phase` and refuses a repo write before plan approval (`stage-hook`, 3 of 3). In a resumed case it stays inert: the history's session id is not the run's.
- A session started from another reads a document by its absolute path in the starting session's scratchpad (one probe session, 2026-10-22).
- A run can read a loaded plugin's own files, such as `design:adr`'s `references/format.md` (`read-plugin-folder`).
