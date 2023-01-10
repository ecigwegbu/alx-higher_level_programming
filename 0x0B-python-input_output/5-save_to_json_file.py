#!/usr/bin/python3
""" This module is for a function
that creates a JSON string and saves it to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """ This function creates a JSON string and saves it to a file.
    """

    if my_obj is None or filename is None:
        return

    with open(filename, "w") as f:
        return json.dump(my_obj, f)
