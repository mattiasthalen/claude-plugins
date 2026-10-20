---
description: Probe whether an eval run can read a loaded plugin's own files, such as design:adr's references/format.md.
plugins: ["../../../.eval-deps/claude-design-skills/plugins/design"]
max_turns: 10
allowed_tools: [Skill, Read, Glob, Bash]
---

Invoke the `design:adr` skill. Its loaded text names its base directory. Read `references/format.md` in that directory and quote its first line verbatim. If you cannot read it, say exactly what the tool returned.
