#!/bin/bash
# This bash script takes in a URL, sends a request to that URL,
curl -X "OPTIONS" "$1" -i 2> /dev/null | grep '^Allow' | cut -b 8-
