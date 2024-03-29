#!/usr/bin/python3
"""list commits in a github repo"""


import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28"}
    response = requests.get(url, params=params)
    if len(response.json()) != 0:
        for commit in response.json()[:10]:
            print(f"{commit['sha']}: {commit['author']['login']}")
