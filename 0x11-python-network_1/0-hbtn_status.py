#!/usr/bin/python3
"""Fetch a URL using urllib"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print(html)
