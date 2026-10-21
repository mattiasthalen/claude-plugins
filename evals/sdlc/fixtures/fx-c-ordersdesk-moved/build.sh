#!/usr/bin/env bash
# ordersdesk-csv-export-branch's state, then one more commit on csv-export after the head whose
# evidence was approved: the export switches to Unix line endings. Checks still pass; the head moved.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../ordersdesk-csv-export-branch/build.sh"
rm -rf .delivering-pitches
cp -R "$here/branch/moved/." .
git add -A
git commit -q -m "Write the CSV with Unix line endings"
