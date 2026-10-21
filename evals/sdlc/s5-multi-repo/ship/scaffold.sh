#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../../lib/scaffold.sh" ledger-api-renamed:api ledger-mobile-renamed:mobile ledger-docs:docs
# The documents the earlier session left at its seam: beside the three repos, in none of them.
mkdir -p sdlc-handoff && cp "$here/handoff/"* sdlc-handoff/
