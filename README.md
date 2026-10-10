# claude-plugins

Mattias Thalén's personal Claude Code plugin marketplace.

## Install

```bash
claude plugin marketplace add mattiasthalen/claude-plugins
claude plugin install <plugin>@mattiasthalen
```

## Layout

```
.claude-plugin/marketplace.json   catalog: one entry per plugin
plugins/<name>/
  .claude-plugin/plugin.json      name, description, version, author
  skills/<skill>/SKILL.md
  commands/*.md
  agents/*.md
  hooks/hooks.json
  .mcp.json
  README.md
```

A plugin carries only the component directories it uses.

## Add a plugin

1. `claude plugin init plugins/<name>` (or create the layout above by hand).
2. Add an entry to `.claude-plugin/marketplace.json`:
   ```json
   { "name": "<name>", "source": "./plugins/<name>", "description": "…", "version": "0.1.0", "category": "workflow" }
   ```
3. Validate: `claude plugin validate --strict .` and `claude plugin validate --strict plugins/<name>`.
4. Try it locally without installing: `claude --plugin-dir plugins/<name>`.

A plugin that lives in another repo is listed with a `git-subdir` or `github` source pinned to a `sha` instead of a local path.

## Versioning

Bump `version` in both `plugin.json` and the marketplace entry on every change that should reach installed copies; `claude plugin update` only pulls a new version.
