#!/usr/bin/python3
"""Fetch a URL using urllib"""


import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        mydict = response.info().items()

    print("Body response:")
    for elt in mydict:
        print(f"\t- {elt[0]}: {elt[1]}")
