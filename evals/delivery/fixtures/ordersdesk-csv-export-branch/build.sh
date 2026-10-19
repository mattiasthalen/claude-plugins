#!/usr/bin/env bash
# Builds the CSV export on its own branch, csv-export, off main, and leaves the
# workspace on it: the state a delivery reaches its gate in.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
git switch -q -c csv-export
cp -R "$here/branch/csv-export/." .
git add -A
git commit -q -m "Export every order as CSV"
