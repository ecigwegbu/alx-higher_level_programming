#!/usr/bin/python3
"""send POST request using requests module"""


import requests
import sys

if __name__ == "__main__":

    def getLetter():
        try:
            letter = sys.argv[1]
            if letter.isalpha() and len(letter) == 1:
                pass
            else:
                letter = ""
        except IndexError:
            letter = ""
        return letter

    url = "http://0.0.0.0:5000/search_user"
    letter = getLetter()
    data = {"q": letter}
    response = requests.post(url, data=data)

    try:
        js = response.json()
        if (len(js) != 0):
            print(f"[{js['id']}] {js['name']}")
        else:
            print(f"No result")
    except requests.exceptions.JSONDecodeError:
        print(f"Not a valid JSON")
