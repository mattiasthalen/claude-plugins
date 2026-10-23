#!/usr/bin/env bash
# ordersdesk at main, plus the intent.md the run resumes from in sdlc-handoff/ (untracked, git-excluded).
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ordersdesk
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
echo "sdlc-handoff/" >> .git/info/exclude
