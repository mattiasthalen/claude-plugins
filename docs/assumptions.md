# Assumptions

What this marketplace's designs rest on without having verified, each with how you would know it stopped holding, plus measured facts that would cost time to rediscover.

## Standing

| Id | Assumption | Area | Stops holding when |
|----|------------|------|--------------------|
| A2 | The exodus skills stay callable by qualified name with stable hand-offs (design-interview's Phase 8 wrap-up, review-cycle's hand-back to the PR step). | delivery / upstream | A hand-off fails in an eval run after an upstream release. |
| A3 | Plan-mode tools are absent in `claude plugin eval` runs; the Artifact tool is off. | evals | A probe finds plan-mode tools present. |
| A7 | TaskCreate/TaskUpdate run in eval cases that list them in `allowed_tools`. | evals | A case listing them shows no Task calls in any run. |
| A8 | `gh` is unauthenticated in eval runs, and a `gh pr create --body` stays visible to graders. | evals | A probe's `gh auth status` succeeds. |
| A11 | `gh stack submit --auto` opens drafts with generated titles and takes no body (documented); we assume it also needs the repository's stacked-PR preview enabled (recalled, unverified). The skill sets bodies with `gh pr edit` and marks PRs ready. | delivery / shipping | `gh stack` works on a repo without the preview, or `submit` gains a body option. |

## Documented

- Plugin `dependencies` given as bare names resolve against the plugin's own marketplace (plugin manifest reference). `implementation` needs `design >=0.7.0`. Tripwire after merge: `claude plugin install delivery@mattiasthalen` must also install both.
- TaskCreate and TaskUpdate are on by default only on Opus 4.7, Sonnet 4.6, Haiku 4.5 and earlier models. Elsewhere they are off unless opted in (`CLAUDE_CODE_ENABLE_TODO_TOOLS=1`, `--allowedTools TaskCreate`), and `CLAUDE_CODE_ENABLE_TASKS=0` swaps them for TodoWrite (tools reference). Listing them in an eval case's `allowed_tools` opts in, so the suite never sees a session without them.

- The desktop app's task-list tool takes a plan of one to twelve steps (its own schema) and does not exist in eval runs, where only Claude Code's tools are offered.

## Measured

Probes in `evals/probes/`, Claude Code 2.1.302, `claude-opus-5-5`, 2026-10-20. Rerun after a Claude Code upgrade.

- Plan-mode tools are absent in eval runs: EnterPlanMode and ExitPlanMode are never called (`plan-mode`).
- The Artifact tool is absent in eval runs (`artifact`).
- `gh pr create` exits 4 with "please run: gh auth login"; the `--body` is visible in the trace (`gh-pr`).
- `/usr/bin/git` fails: the xcrun shim cannot write its cache in the sandbox (exit 72). `/opt/homebrew/bin/git` commits and branches. `worktree add` runs its checkout as a child `git` found on PATH, the shim, so it fails; `--no-checkout` then `reset --hard` with Homebrew's git works, as does `git archive` (`git-in-sandbox`; s1-build traces). `python3` works.
- TaskCreate and TaskUpdate work when listed in `allowed_tools` (`task-tools`).
- Writes to `/tmp` are refused by the sandbox; `$TMPDIR` is writable. Writes into the workspace's `.git/` are refused by the permission layer (`write-scope`).
- Fixture SHAs match across machines only with user git config off: a signing config changes every commit (`GIT_CONFIG_GLOBAL=/dev/null` in the scaffold).
- A run can read a loaded plugin's own files, such as `design:adr`'s `references/format.md` (`read-plugin-folder`).
