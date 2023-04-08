#!/usr/bin/env bash

curl -sL \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/user | grep "^[[:blank:]]*\"id\"" | cut -d, -f1 | cut -d' ' -f4
