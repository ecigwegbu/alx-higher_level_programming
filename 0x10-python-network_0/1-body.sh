#!/bin/bash
# This bash script takes in a URL, sends a request to that URL,
curl --get "$1" 2> /dev/null
