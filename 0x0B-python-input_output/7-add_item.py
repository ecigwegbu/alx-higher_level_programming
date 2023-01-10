#!/usr/bin/python3
""" This script adds all arguments to a Python list
and then saves them to a file.
"""


import sys
import json

if len(sys.argv) == 1:
    myargs = []
else:
    myargs = sys.argv[1:]

try:
    with open("add_item.json", "r") as f:
        mylist = json.load(f)
except FileNotFoundError:
    mylist = []

mylist += myargs

with open("add_item.json", "w+") as f:
    json.dump(mylist, f)
