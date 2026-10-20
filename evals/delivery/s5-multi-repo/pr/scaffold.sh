#!/usr/bin/env bash
exec bash "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../../lib/scaffold.sh" ledger-api-renamed:api ledger-mobile-renamed:mobile ledger-docs:docs
