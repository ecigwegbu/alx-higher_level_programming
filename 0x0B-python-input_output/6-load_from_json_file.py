#!/usr/bin/python3
""" This module is for a function
that loads a JSON string from a file
"""


import json


def load_from_json_file(filename):
    """ This function loads a JSON string from a file.
    """

    if filename is None:
        return

    with open(filename, "r") as f:
        return json.load(f)
