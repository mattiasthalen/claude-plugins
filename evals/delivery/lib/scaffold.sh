#!/usr/bin/env bash
# Shared scaffold for every case: copies one or more fixtures into the run's
# workspace (the working directory) and commits each as its own git repo.
#
#   scaffold.sh <fixture>[:<dir>] ...
#
# A bare <fixture> is copied into the workspace itself. <fixture>:<dir> copies
# it into <dir>/, so a multi-repo case gets one repo per directory. A fixture
# may carry a git-history script, build.sh, which runs inside the copy after
# the first commit and before the workspace is handed over (to add branches,
# work-in-progress commits or uncommitted changes). A fixture's branch/ holds
# files for build.sh to lay over the first commit; it is never committed as is. Graders and specs never
# leave the eval directory: only fixtures/ is copied.
set -euo pipefail
# Fixed dates make every fixture commit, and so every SHA a history quotes, reproducible.
export GIT_AUTHOR_DATE=2026-10-13T09:00:00Z GIT_COMMITTER_DATE=2026-10-13T09:00:00Z
lib="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fixtures="$lib/../fixtures"
for spec in "$@"; do
  name="${spec%%:*}"; dir="."
  [[ "$spec" == *:* ]] && dir="${spec#*:}"
  [ -d "$fixtures/$name" ] || { echo "scaffold: no fixture $name" >&2; exit 1; }
  mkdir -p "$dir"
  (
    cd "$dir"
    cp -R "$fixtures/$name/." .
    rm -rf build.sh branch
    git init -q -b main .
    git add -A
    git -c user.name=ops -c user.email=ops@example.com commit -q -m "Initial import"
    # review-cycle takes its base from origin/HEAD; a fixture has no remote.
    git update-ref refs/remotes/origin/main main
    git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
    if [ -f "$fixtures/$name/build.sh" ]; then
      GIT_AUTHOR_NAME=ops GIT_AUTHOR_EMAIL=ops@example.com GIT_COMMITTER_NAME=ops GIT_COMMITTER_EMAIL=ops@example.com \
        bash "$fixtures/$name/build.sh"
    fi
  )
done
