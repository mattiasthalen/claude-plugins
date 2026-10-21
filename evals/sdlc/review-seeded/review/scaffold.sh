#!/usr/bin/env bash
# ordersdesk on csv-export: approved checks (ace432b), then an export that passes them but splits names with commas (4188880).
# The approved spec and plan go into sdlc-handoff/ (untracked, git-excluded) for the resumed run.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" fx-b-ordersdesk-seeded
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
