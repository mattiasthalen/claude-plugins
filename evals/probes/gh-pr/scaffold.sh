#!/usr/bin/env bash
set -e
git init -q -b main .
git -c user.email=a@b -c user.name=probe commit -q --allow-empty -m init
git checkout -q -b feature
echo hi > README.md
git add README.md
git -c user.email=a@b -c user.name=probe commit -q -m readme
