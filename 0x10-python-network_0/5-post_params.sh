#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"  2> /dev/null
