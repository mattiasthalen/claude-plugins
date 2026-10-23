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
docs/decisions/                   ADRs; docs/lexicon.md, docs/assumptions.md beside them
evals/<plugin>/                   eval suites, run in-session (evals/README.md)
REVIEW.md                         what review looks for, and risk tiers by path
scripts/vendor.sh                 upstream copies and pins, from scripts/vendor.json
```

A plugin carries only the component directories it uses.

## Add a plugin

1. `claude plugin init plugins/<name>` (or create the layout above by hand).
2. Add an entry to `.claude-plugin/marketplace.json`:
   ```json
   { "name": "<name>", "source": "./plugins/<name>", "description": "…", "category": "workflow" }
   ```
3. Validate: `claude plugin validate --strict .` and `claude plugin validate --strict plugins/<name>`.
4. Try it locally without installing: `claude --plugin-dir plugins/<name>`.

A plugin that lives in another repo is listed with a `git-subdir` or `github` source instead of a local path. Leave out `sha` and `version` to follow its default branch and its own `plugin.json` version; add a `sha` to freeze it.

## Versioning

A local plugin's version lives only in its `plugin.json`; the marketplace entry leaves it out so the two cannot drift. Bump it on every change that should reach installed copies: `claude plugin update` only pulls a new version.

## How a change ships here

This repository runs the SDLC its `sdlc` plugin encodes, after Anthropic's [AI-native SDLC playbook](https://claude.com/resources/articles/the-ai-native-sdlc-playbook). A change goes:

1. **Intent.** Whatever prompted it: an idea, an issue, a bug report. Say `/sdlc <intent>`. The intent stage writes it as user stories; at the intent gate you decide each story: deliver it now, file it on the tracker, or drop it.
2. **Spec.** A design interview (`design:design-interview`) settles the open questions; the spec lists each acceptance criterion and edge case with a check. You approve it.
3. **Plan.** Slices, order, what each check verifies. You approve it.
4. **Tests.** The `test-writer` agent writes every check from the spec alone and runs it on `main`: what should change is red, what must not change is green. You approve them. From here the run is unattended.
5. **Build, review, prove.** The change is built; reviewers by lens, verifier votes and a security pass review it, up to three rounds; every check runs at the head with CI and the eval suite of any skill it touches. `REVIEW.md` decides the tier.
6. **Evidence.** You approve it, unless the change is Low tier (docs), which opens its pull request on green.
7. **Pull requests**, with Summary, Testing, Risk and How to revert. `main` requires `validate` and an up-to-date branch, for admins too. The decisions behind each step are [ADR-0007 to ADR-0015](docs/decisions/README.md).

**When something escapes.** A reverted pull request, or a bug found after merge, is the next intent: `/sdlc` on it yields a spec whose first criterion is a failing eval case that reproduces it, so the suite catches it from then on. For example, if a skill started firing on unrelated conversations, the fix's first criterion is a negative trigger case built from the conversation it fired on.
