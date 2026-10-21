#!/usr/bin/env bash
# Copies Matt Pocock's pr skill into plugins/sdlc/skills/pr at the pinned
# commit (ADR-0013). --check exits non-zero if the copy has drifted instead.
set -euo pipefail
commit=e484a80
files=(SKILL.md CREDITS.md)
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
dest="$root/plugins/sdlc/skills/pr"
status=0
for f in "${files[@]}"; do
  upstream="$(gh api "repos/mattpocock/skills/contents/skills/engineering/pr/$f?ref=$commit" --jq .content | base64 -d)"
  if [ "${1:-}" = "--check" ]; then
    if ! diff -q <(printf '%s\n' "$upstream") "$dest/$f" >/dev/null; then
      echo "drifted: $f" >&2
      status=1
    fi
  else
    printf '%s\n' "$upstream" > "$dest/$f"
  fi
done
exit $status
