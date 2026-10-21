#!/usr/bin/env bash
# The state a delivery reaches its gate in: on csv-export, off main, the capture commit then
# the export, with the evidence page written but untracked.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
git switch -q -c csv-export
cp -R "$here/branch/capture/." .
git add -A
git commit -q -m "Record the CSV dialect decision"
cp -R "$here/branch/export/." .
git add -A
git commit -q -m "Export every order as CSV"
mkdir -p .delivering-pitches
cp "$here/page/evidence.html" .delivering-pitches/
