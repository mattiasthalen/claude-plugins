#!/usr/bin/env bash
# Checks out the plugins sdlc depends on into .eval-deps/, at their default branch,
# as the marketplace follows them (ADR-0002). Re-run before an eval pass.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
deps="$root/.eval-deps"
rm -rf "$deps" && mkdir -p "$deps"
git clone -q --depth 1 https://github.com/the-exodus/claude-design-skills.git "$deps/exodus"
mv "$deps/exodus/plugins/design" "$deps/exodus/plugins/implementation" "$deps/"
# Only the plugin directories stay, so no upstream eval suite sits under the runner's target.
rm -rf "$deps/exodus"
git clone -q --depth 1 https://github.com/mattpocock/skills.git "$deps/mattpocock-skills"
rm -rf "$deps/mattpocock-skills/.git"
for p in design implementation mattpocock-skills; do
  printf '%s %s\n' "$p" "$(jq -r .version "$deps/$p/.claude-plugin/plugin.json")"
done
