#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
curl -w "You got me!" "0.0.0.0:5000/catch_me" -so /dev/null
