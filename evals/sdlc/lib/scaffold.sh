#!/usr/bin/env bash
# Builds one state of the ordersdesk fixture in the run's workspace (the working directory):
#
#   scaffold.sh base | designed | designed-gap | captured | built
#
# base is the bare repo. designed adds the change's run documents (stories and the
# design interview's brief) to .scratchpad/sdlc/orders-count/, which the cases name
# as the session scratchpad: git ignores it, as a real scratchpad is outside the repo.
# designed-gap carries stories with a stated criterion the brief does not cover.
# captured adds the capture's commit of decisions and an assumptions record, one of them wrong about GitHub Actions.
# built adds the red tests commit and the build commit on feat/orders-count.
set -euo pipefail
# Fixed dates and no user or system git config make every commit, and so every SHA, the same on any machine.
export GIT_AUTHOR_DATE=2026-10-13T09:00:00Z GIT_COMMITTER_DATE=2026-10-13T09:00:00Z
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
export GIT_AUTHOR_NAME=ops GIT_AUTHOR_EMAIL=ops@example.com GIT_COMMITTER_NAME=ops GIT_COMMITTER_EMAIL=ops@example.com
lib="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
state="${1:?state}"
cp -R "$lib/fixtures/ordersdesk/." .
git init -q -b main .
echo ".scratchpad/" >> .git/info/exclude
git add -A && git commit -q -m "Initial import"
# A remote nobody can reach: pushes and gh calls are attempted and fail. review-cycle takes its base from origin/HEAD.
git remote add origin "https://github.com/example/ordersdesk.git"
git update-ref refs/remotes/origin/main main
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
docs=.scratchpad/sdlc/orders-count
case "$state" in
  base) ;;
  designed|designed-gap|captured|built)
    mkdir -p "$docs" && cp "$lib/run-docs/"*.md "$docs/"
    [ "$state" = designed-gap ] && cp "$lib/run-docs-gap/stories.md" "$docs/"
    git checkout -q -b feat/orders-count
    if [ "$state" = captured ]; then
      cp -R "$lib/stages/records/." . && git add -A && git commit -q -m "Record the count design: ADR-0001, ADR-0002, A1 and A2"
    fi
    if [ "$state" = built ]; then
      cp -R "$lib/stages/tests/." . && git add -A && git commit -q -m "Add red tests for orders count (AC1-AC3)"
      cp -R "$lib/stages/build/." . && git add -A && git commit -q -m "Add the orders count subcommand"
    fi ;;
  *) echo "scaffold: no state $state" >&2; exit 1 ;;
esac
