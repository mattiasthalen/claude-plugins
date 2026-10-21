#!/usr/bin/env bash
set -e
printf '# demo\n\nA tiny repo.\n' > README.md
git init -q -b main . && git add README.md && git -c user.name=p -c user.email=p@example.com commit -q -m init
