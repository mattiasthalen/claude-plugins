# claude-plugins

Personal Claude Code plugin marketplace. `README.md` holds the layout and the add-a-plugin steps; follow them.

- One plugin per directory under `plugins/`; its name, directory, `plugin.json` `name` and marketplace entry `name` match.
- Every plugin change bumps `version` in its `plugin.json`, the only place a local plugin's version lives.
- Run `claude plugin validate --strict` on the marketplace and the touched plugin before committing; CI runs the same.
- Load the `writing-for-agents` skill before writing or editing a `SKILL.md`, agent or command.
- Eval suites live in `evals/<plugin>/`; read `evals/README.md` before adding a case or running them.
- Changes here go through `/sdlc`. `REVIEW.md` says what review looks for, and its tiers say which changes stop for you.
- A change to a skill, agent, `CLAUDE.md` or hook needs its eval suite passing in-session before a pull request: CI has no Claude token and cannot run evals.
- Vendored copies change only through `scripts/vendor.sh`.
