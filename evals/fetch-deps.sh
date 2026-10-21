#!/usr/bin/env bash
# Checks out the plugins the eval cases load beside the plugin under test into
# .eval-deps/ (gitignored), at the sha the marketplace pins them to. Sparse:
# only the plugin directories, so the runner never finds the upstream repo's own
# eval cases.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dest="$root/.eval-deps/claude-design-skills"
sha="$(jq -r '.plugins[]|select(.name=="design").source.sha' "$root/.claude-plugin/marketplace.json")"
if [ ! -d "$dest/.git" ]; then
  git clone -q --depth 1 --filter=blob:none --sparse https://github.com/the-exodus/claude-design-skills.git "$dest"
fi
git -C "$dest" fetch -q --depth 1 origin "$sha"
git -C "$dest" reset -q --hard FETCH_HEAD
git -C "$dest" sparse-checkout set plugins/design plugins/implementation
