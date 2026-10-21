#!/usr/bin/env bash
# ordersdesk on csv-export with the approved checks committed at the test gate (15418d3).
# The approved spec and plan go into sdlc-handoff/ (untracked, git-excluded) for the resumed run.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" fx-b-ordersdesk-tests
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
