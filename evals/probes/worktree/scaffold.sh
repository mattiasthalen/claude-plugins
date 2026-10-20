#!/usr/bin/env bash
set -e
git init -q -b main .
git -c user.email=a@b -c user.name=probe commit -q --allow-empty -m init
