# Runner probes

What `claude plugin eval` can observe and do. The `delivery` suite is designed around these results; rerun them after a Claude Code upgrade, before trusting the suite on the new version:

```sh
evals/fetch-deps.sh
claude plugin eval . --eval-dir evals/probes --model claude-opus-5-5 --judge-model claude-opus-5-5 \
  --ablation none --runs 1 --scaffold --trust-plugin \
  --allow-tools EnterPlanMode ExitPlanMode Artifact Write Bash
```

| Case | Expected on 2.1.302 | If it changes |
|---|---|---|
| `plan-mode` | **fails**: the tools do not exist in eval runs | The plan-mode line (ADR-0005) needs an eval that fails without it. |
| `artifact` | **fails**: the Artifact tool is off | The publish line (ADR-0005) needs an eval that fails without it. |
| `task-tools` | passes | Progress graders break. |
| `gh-pr` | passes; `gh` exits 4 (no auth), the `--body` is visible | If `gh` succeeds, a shipping stage could reach GitHub: isolate before running it. |
| `git-in-sandbox` | `python-works` passes; `git-works` **fails**: `/usr/bin/git` is the xcrun shim. `/opt/homebrew/bin/git` works | If `/usr/bin/git` works too, nothing changes. |
| `write-scope` | `tmpdir` passes; `inside-git` **fails**: the permission layer refuses `.git/` writes | Revisit where overlay worktrees live (ADR-0002). |
| `read-plugin-folder` | passes | — |

Measured results are recorded in `docs/assumptions.md` under *Measured*.
