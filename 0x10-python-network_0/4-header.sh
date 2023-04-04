#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -GH "X-School-User-Id: 98" "$1"  2> /dev/null
