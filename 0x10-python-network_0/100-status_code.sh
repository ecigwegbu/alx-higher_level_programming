#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -w "%{response_code}" -o /dev/null --stderr /dev/null "$1"
