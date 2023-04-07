#!/usr/bin/python3
"""Post data to a URL using urllib"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    data_url_encoded = urllib.parse.urlencode(data)
    data_byte_encoded = data_url_encoded.encode("utf-8")
    # urlopen is a function that takes a request object as parameter
    # or takes url and other parameters
    with urllib.request.urlopen(url, data=data_byte_encoded) as response:
        print(response.read().decode("utf-8"))
