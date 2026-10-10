# claude-plugins

Personal Claude Code plugin marketplace. `README.md` holds the layout and the add-a-plugin steps; follow them.

- One plugin per directory under `plugins/`; its name, directory, `plugin.json` `name` and marketplace entry `name` match.
- Every plugin change bumps `version` in `plugin.json` and the marketplace entry together.
- Run `claude plugin validate --strict` on the marketplace and the touched plugin before committing; CI runs the same.
- Load the `writing-for-agents` skill before writing or editing a `SKILL.md`, agent or command.
- Eval suites live in `evals/<plugin>/`; read `evals/README.md` before adding a case or running them.
