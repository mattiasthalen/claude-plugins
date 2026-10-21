#!/usr/bin/env bash
# Lays branch/ over the first commit on the work branch, as the built change.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
git switch -q -c rename-customer-id-to-account-id
cp -R "$here/branch/." .
git add -A
git commit -q -m "Rename customerId to accountId with a one-release deprecation window"
