#!/usr/bin/env bash
# ordersdesk with a REVIEW.md whose tiers mark README.md and docs/** Low, at main.
# The approved spec and plan go into sdlc-handoff/ (untracked, git-excluded) for the resumed run.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" fx-b-ordersdesk-lowtier
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
