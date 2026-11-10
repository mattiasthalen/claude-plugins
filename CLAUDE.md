# claude-plugins

Personal Claude Code plugin marketplace; `README.md` has the layout.

- One plugin per directory under `plugins/`; its directory, `plugin.json` `name` and marketplace entry `name` match.
- Every plugin change bumps `version` in its `plugin.json`, the only place a local plugin's version lives.
- Run `tests/check_repo.sh` before committing; CI runs the same.
- A skill line goes in only with an eval case that is red without it and green with it; `evals/README.md` says how to show both.
- A change to a skill needs its eval suite passing in-session before a pull request: CI has no model token and cannot run evals.
- Only ADRs, `docs/assumptions.md` and `docs/lexicon.md` are committed from a design; stories and briefs stay in the session scratchpad (ADR-0003).
