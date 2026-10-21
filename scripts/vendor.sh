#!/usr/bin/env bash
# Upstream copies and pins, from scripts/vendor.json (ADR-0013, ADR-0007).
#
#   vendor.sh --check     each copy matches its pinned upstream commit; each pin in
#                         .claude-plugin/marketplace.json is a full SHA upstream has
#   vendor.sh --drift     names every copy or pin whose upstream path has a newer
#                         commit on its default branch; exits 1 if any has
#   vendor.sh --refresh   moves every copy and pin to that commit, and bumps the patch
#                         version of each plugin whose copy changed
#
# Copies are changed only here; .claude/hooks/protect_vendored.py refuses Claude's Write and Edit to them.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
manifest="$root/scripts/vendor.json"
market="$root/.claude-plugin/marketplace.json"
mode="${1:-}"
case "$mode" in --check|--drift|--refresh) ;; *) sed -n '2,10p' "$0" >&2; exit 2;; esac

# The newest upstream commit that touched <path> on the default branch: a commit elsewhere is not drift.
last_touch() { gh api "repos/$1/commits?sha=$(gh api "repos/$1" --jq .default_branch)&path=$2&per_page=1" --jq '.[0].sha'; }
# One upstream file into <out>; a missing or empty file fails, so a refresh never writes an empty copy.
upstream_file() {
  gh api "repos/$1/contents/$2?ref=$3" --jq .content | base64 -d > "$4" && [ -s "$4" ] || { echo "missing upstream: $1/$2@${3:0:7}" >&2; exit 1; }
}
pin_repo() { jq -r --arg n "$1" '.plugins[]|select(.name==$n).source.url' "$market" | sed -E 's#^https://github.com/##; s#\.git$##'; }
pin_path() { jq -r --arg n "$1" '.plugins[]|select(.name==$n).source.path' "$market"; }
pin_sha() { jq -r --arg n "$1" '.plugins[]|select(.name==$n).source.sha // empty' "$market"; }
# Bump the patch version of the plugin a copy lives in, so `claude plugin update` pulls the refresh.
bump() { local pj; pj="$root/$(echo "$1" | cut -d/ -f1-2)/.claude-plugin/plugin.json"; [ -f "$pj" ] || return 0
  local tmp; tmp=$(mktemp); jq --indent 2 '.version |= (split(".") | .[2] = ((.[2]|tonumber)+1|tostring) | join("."))' "$pj" > "$tmp" && mv "$tmp" "$pj"; }
status=0
n=$(jq '.copies|length' "$manifest")
for i in $(seq 0 $((n - 1))); do
  repo=$(jq -r ".copies[$i].repo" "$manifest"); path=$(jq -r ".copies[$i].path" "$manifest")
  sha=$(jq -r ".copies[$i].sha" "$manifest"); rel=$(jq -r ".copies[$i].dest" "$manifest"); dest="$root/$rel"
  case "$mode" in
    --check)
      for f in $(jq -r ".copies[$i].files[]" "$manifest"); do
        t=$(mktemp); upstream_file "$repo" "$path/$f" "$sha" "$t"
        cmp -s "$t" "$dest/$f" || { echo "drifted from $repo@${sha:0:7}: $rel/$f" >&2; status=1; }; rm -f "$t"
      done ;;
    --drift)
      new=$(last_touch "$repo" "$path"); [ "$new" = "$sha" ] || { echo "behind: $repo/$path ${sha:0:7} -> ${new:0:7}"; status=1; } ;;
    --refresh)
      new=$(last_touch "$repo" "$path"); [ "$new" = "$sha" ] && continue
      for f in $(jq -r ".copies[$i].files[]" "$manifest"); do upstream_file "$repo" "$path/$f" "$new" "$dest/$f"; done
      bump "$rel"
      tmp=$(mktemp); jq --indent 2 ".copies[$i].sha = \"$new\"" "$manifest" > "$tmp" && mv "$tmp" "$manifest" ;;
  esac
done
for name in $(jq -r '.pins[]' "$manifest"); do
  repo=$(pin_repo "$name"); sha=$(pin_sha "$name")
  case "$mode" in
    --check)
      [[ "$sha" =~ ^[0-9a-f]{40}$ ]] && gh api "repos/$repo/commits/$sha" --jq .sha >/dev/null 2>&1 || { echo "bad pin: $name '$sha'" >&2; status=1; } ;;
    --drift)
      new=$(last_touch "$repo" "$(pin_path "$name")"); [ "$new" = "$sha" ] || { echo "behind: $name ${sha:0:7} -> ${new:0:7}"; status=1; } ;;
    --refresh)
      new=$(last_touch "$repo" "$(pin_path "$name")"); [ "$new" = "$sha" ] && continue; tmp=$(mktemp)
      jq --indent 2 --arg n "$name" --arg s "$new" '(.plugins[]|select(.name==$n).source.sha) = $s' "$market" > "$tmp" && mv "$tmp" "$market" ;;
  esac
done
exit $status
