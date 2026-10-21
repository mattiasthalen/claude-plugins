#!/usr/bin/env bash
# The state an sdlc run leaves at its approved test gate: on csv-export, off main, one commit
# holding the test-writer's checks for the CSV export, red at the base.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
git switch -q -c csv-export
cp -R "$here/branch/." .
git add -A
git commit -q -m "Add the approved checks for the CSV export"
