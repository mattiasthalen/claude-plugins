#!/usr/bin/env bash
# The repository's shape after the rebuild: marketplace, sdlc's manifest and skills, nothing of the old sdlc.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
failed=0
check() { local name="$1" out; shift
  if out=$("$@" 2>&1); then echo "ok   $name"; else echo "FAIL $name"; echo "$out" | sed 's/^/     /'; failed=1; fi; }
market=.claude-plugin/marketplace.json
manifest=plugins/sdlc/.claude-plugin/plugin.json
listed_unpinned() { jq -e --arg n "$1" '[.plugins[] | select(.name == $n and (.source | type == "object") and (.source.sha == null))] | length == 1' "$market"; }

check "AC17 marketplace validates" claude plugin validate --strict .
check "AC17 sdlc validates" claude plugin validate --strict plugins/sdlc
# validate reads only local files; an upstream entry's repo or path is first fetched on install.
installs_with_dependencies() {
  local home; home=$(mktemp -d)
  HOME=$home CLAUDE_CONFIG_DIR=$home claude plugin marketplace add "$PWD" >/dev/null &&
    HOME=$home CLAUDE_CONFIG_DIR=$home claude plugin install sdlc@mattiasthalen | grep -q "3 dependencies"
}
check "AC17 sdlc installs with its three dependencies" installs_with_dependencies
check "AC18 sdlc is listed from its directory" jq -e '.plugins[] | select(.name == "sdlc" and .source == "./plugins/sdlc")' "$market"
for p in design implementation mattpocock-skills; do check "AC18 $p is listed unpinned" listed_unpinned "$p"; done
check "AC18 sdlc depends on all three" jq -e '(.dependencies | sort) == ["design", "implementation", "mattpocock-skills"]' "$manifest"
check "AC18 sdlc is 1.0.0" jq -e '.version == "1.0.0"' "$manifest"
check "AC19 no test-writer agent" test ! -e plugins/sdlc/agents
check "AC19 no stage references" test ! -e plugins/sdlc/skills/sdlc/references
check "AC19 no vendor script or manifest" test -z "$(ls scripts/vendor* 2>/dev/null)"
check "AC19 no vendor-refresh workflow" test ! -e .github/workflows/vendor-refresh.yml
check "#62 ablation starts with one run" grep -qE -- "--runs 1\b" evals/README.md
check "#62 a judged line starts with two runs" grep -qE -- "--runs 2\b" evals/README.md
check "#63 CLAUDE.md has no writing-for-agents line" bash -c 'test -f CLAUDE.md && ! grep -q writing-for-agents CLAUDE.md'
check "the eval suite generates and its graders hold" python3 -m unittest tests/test_graders.py
exit $failed
