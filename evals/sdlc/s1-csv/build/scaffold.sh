#!/usr/bin/env bash
# ordersdesk on csv-export with the approved checks committed (15418d3), plus the approved spec and plan the resumed run reads from sdlc-handoff/
# (untracked and git-excluded, so they never enter a diff or a commit).
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" fx-b-ordersdesk-tests
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
