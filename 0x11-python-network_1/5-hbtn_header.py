#!/usr/bin/python3
"""send request using requests module and get header"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers["X-Request-Id"])
