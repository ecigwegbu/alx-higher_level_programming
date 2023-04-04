#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -w "%{response_code}" -s -o /dev/null "$1"
