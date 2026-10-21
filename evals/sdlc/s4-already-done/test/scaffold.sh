#!/usr/bin/env bash
# ordersdesk with the CSV export already on main.
# The approved spec and plan go into sdlc-handoff/ (untracked, git-excluded) for the resumed run.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ordersdesk-csv-export
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
