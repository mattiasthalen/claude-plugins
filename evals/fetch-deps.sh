#!/usr/bin/env bash
# Checks out the plugins the eval cases load beside the plugin under test into
# .eval-deps/ (gitignored), at the commit the marketplace resolves today. Sparse:
# only the plugin directory, so the runner never finds the upstream repo's own
# eval cases.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dest="$root/.eval-deps/claude-design-skills"
if [ ! -d "$dest/.git" ]; then
  git clone -q --depth 1 --filter=blob:none --sparse https://github.com/the-exodus/claude-design-skills.git "$dest"
  git -C "$dest" sparse-checkout set plugins/design
else
  git -C "$dest" pull -q --ff-only
fi
