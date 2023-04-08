#!/usr/bin/python3
"""send POST request using requests module"""


import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = sys.argv[1]
        if letter.isalpha() and len(letter) == 1:
            pass
        else:
            letter = ""
    except IndexError:
        letter = ""
    print(letter, len(letter))
