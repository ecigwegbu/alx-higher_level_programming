#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -s -d @"$2" "$1"
