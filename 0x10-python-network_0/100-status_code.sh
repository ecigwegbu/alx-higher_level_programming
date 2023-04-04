#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -w "%{response_code}" -o /dev/null 2> /dev/null "$1"
