#!/usr/bin/env bash
# ordersdesk at main, plus the approved spec and plan the resumed run reads from sdlc-handoff/
# (untracked and git-excluded, so they never enter a diff or a commit).
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ordersdesk
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
