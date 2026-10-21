# Runner probes

What `claude plugin eval` can observe and do. The `sdlc` suite is designed around these results; rerun them after a Claude Code upgrade, before trusting the suite on the new version:

```sh
evals/fetch-deps.sh
claude plugin eval . --eval-dir evals/probes --model claude-opus-5-5 --judge-model claude-opus-5-5 \
  --ablation none --runs 1 --scaffold --trust-plugin \
  --allow-tools EnterPlanMode ExitPlanMode Artifact Write Bash
```

| Case | Expected on 2.1.302 | If it changes |
|---|---|---|
| `plan-mode` | **fails**: the tools do not exist in eval runs | Nothing: `sdlc` uses no plan mode (ADR-0009). |
| `artifact` | **fails**: the Artifact tool is off | The publish line (ADR-0014) needs an eval that fails without it. |
| `task-tools` | passes | Progress graders break. |
| `gh-pr` | passes; `gh` exits 4 (no auth), the `--body` is visible | If `gh` succeeds, a shipping stage could reach GitHub: isolate before running it. |
| `git-in-sandbox` | `python-works` passes; `git-works` **fails**: `/usr/bin/git` is the xcrun shim. `/opt/homebrew/bin/git` commits; `worktree add` needs `--no-checkout` (see `worktree`) | If worktrees work, the test stage's base runs can use plain worktrees. |
| `write-scope` | `tmpdir` passes; `inside-git` **fails**: the permission layer refuses `.git/` writes | Revisit where base copies live. |
| `stage-hook` | passes: a fresh `/sdlc` run writes `phase` at its real session id and the hook refuses a repo write (`--allow-tools Write Edit Bash`) | The stage hook is inert in eval runs: check where the run's folder and the hook's TMPDIR meet (ADR-0009). |
| `worktree` | **fails** (the probe has not run yet; s1-build traces show it): `worktree add` checks out through the shim on PATH. `--no-checkout` then `reset --hard` works | A base copy can use a plain `worktree add` in evals. |
| `read-plugin-folder` | passes | — |

Measured results are recorded in `docs/assumptions.md` under *Measured*.
