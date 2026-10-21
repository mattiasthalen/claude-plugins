#!/usr/bin/env bash
# The state an sdlc run reaches at the end of its build: on csv-export, the approved checks
# committed at the test gate, then an export that passes them but joins fields by hand, so a
# customer with a comma (Berg, Hanna) splits into two fields. No check covers the comma.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
git switch -q -c csv-export
cp -R "$here/branch/tests" .
git add -A
git commit -q -m "Add the approved checks for the CSV export"
cp -R "$here/branch/export/." .
git add -A
git commit -q -m "Export every order as CSV"
