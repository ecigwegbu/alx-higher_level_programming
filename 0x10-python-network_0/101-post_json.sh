#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
