#!/usr/bin/python3
"""Post data to a URL using urllib"""


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    # Catch HTTPError (ie wrong URL, for example:
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
