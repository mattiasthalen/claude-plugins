#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ordersdesk
# The approved documents a resumed history cannot carry: uncommitted, beside the repo.
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
