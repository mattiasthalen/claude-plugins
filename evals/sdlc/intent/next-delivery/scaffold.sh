#!/usr/bin/env bash
# The documents a resumed history cannot carry: uncommitted, git-excluded, beside the repo.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ordersdesk-csv-export-branch
# The old delivery page the fixture leaves untracked is not part of an sdlc run.
rm -rf .delivering-pitches
mkdir -p sdlc-handoff && cp -R "$here/handoff/." sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
