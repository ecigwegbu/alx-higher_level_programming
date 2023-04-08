#!/usr/bin/python3
"""send request to githubapi using requests"""


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]
    params = {"Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28"}
    response = requests.get(url, params=params, auth=(user, passwd))
    if "id" in response.json():
        print(response.json()["id"])
    else:
        print("None")
