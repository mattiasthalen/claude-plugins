#!/usr/bin/env bash
# ordersdesk-csv-export-branch's state (csv-export off main: the capture commit, then the export) on a
# base that carries a pull request template with its own sections. Its build.sh lays the branches;
# the old delivery page it leaves untracked is removed.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$here/../ordersdesk-csv-export-branch/build.sh"
rm -rf .delivering-pitches
