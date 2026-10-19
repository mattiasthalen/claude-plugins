# Assumptions

What this marketplace's designs rest on without having verified, each with how you would know it stopped holding, plus measured facts that would cost time to rediscover.

## Standing

| Id | Assumption | Area | Stops holding when |
|----|------------|------|--------------------|
| A2 | The exodus skills stay callable by qualified name with stable hand-offs (design-interview Phase 8/9, review-cycle's hand-back to the PR step). | delivery / upstream | A hand-off fails in an eval run after an upstream release. |
| A3 | Plan-mode tools are absent in `claude plugin eval` runs; the Artifact tool is off. | evals | A probe finds plan-mode tools present. |
| A4 | `dependencies` in `plugin.json` resolves `design` and `implementation` against this marketplace. | delivery / install | The eval runner rejects a case loading `plugins/delivery` with both dependencies; after merge, `claude plugin install delivery@mattiasthalen` doesn't install them. |
| A5 | `git` is broken in the eval sandbox, so build, review and evidence are graded on files, trace commands and reported output. | evals | A probe commits successfully. |
| A7 | TaskCreate/TaskUpdate run in eval cases that list them in `allowed_tools`. | evals | A case listing them shows no Task calls in any run. |
| A8 | `gh` is unauthenticated in eval runs, and a `gh pr create --body` stays visible to graders. | evals | A probe's `gh auth status` succeeds. |
| A11 | `gh stack` (github/gh-stack) is an optional extension, absent by default. | delivery / shipping | — the fallback covers both. |
| A12 | Task tools are off by default on current models outside cloud and background sessions; `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` turns them on. | delivery / progress | Setting it shows no Task tools. |

## Measured

Probes in `evals/probes/`, Claude Code 2.1.302, `claude-opus-5-5`, 2026-10-20. Rerun after a Claude Code upgrade.

- Plan-mode tools are absent in eval runs: EnterPlanMode and ExitPlanMode are never called (`plan-mode`).
- The Artifact tool is absent in eval runs (`artifact`).
- `gh pr create` exits 4 with "please run: gh auth login"; the `--body` is visible in the trace (`gh-pr`).
- `git` fails: `/usr/bin/git` is the xcrun shim and cannot write its cache in the sandbox (exit 72). `python3` works (`git-in-sandbox`).
- TaskCreate and TaskUpdate work when listed in `allowed_tools` (`task-tools`).
- Writes to `/tmp` are refused by the sandbox; `$TMPDIR` is writable. Writes into the workspace's `.git/` are refused by the permission layer (`write-scope`).
- A run can read a loaded plugin's own files, such as `design:adr`'s `references/format.md` (`read-plugin-folder`).
