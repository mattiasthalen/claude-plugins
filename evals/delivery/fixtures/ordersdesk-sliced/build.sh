#!/usr/bin/env bash
# Builds the two slices as stacked branches: csv-export on main, csv-export-since on
# csv-export. Each lays its folder under branch/ over the branch it starts from.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
git switch -q -c csv-export
cp -R "$here/branch/1-csv-export/." .
git add -A
git commit -q -m "Export every order as CSV"
git switch -q -c csv-export-since
cp -R "$here/branch/2-csv-export-since/." .
git add -A
git commit -q -m "Limit the CSV export to orders placed since a date"
