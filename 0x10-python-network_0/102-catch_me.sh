#!/bin/bash
# This bash script takes in a URL, sends a request to that URL
# curl -w "%{stdout}" -w "You got me!" -s -o stdout "0.0.0.0:5000/catch_me"
curl -s -w "%{stdout}" -w "You got me!\n" -o stdout "0.0.0.0:5000/catch_me"
