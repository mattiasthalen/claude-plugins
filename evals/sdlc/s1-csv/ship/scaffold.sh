#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ordersdesk-csv-export-branch
# The old delivery page the fixture leaves untracked is not part of an sdlc run.
rm -rf .delivering-pitches
# The documents the earlier session left at its seam: in the workspace, never committed.
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
mkdir -p .git/info && echo "sdlc-handoff/" >> .git/info/exclude
