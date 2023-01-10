#!/usr/bin/python3
""" This module is for a function
that creates an object from  a JSON string
"""

import json


def from_json_string(my_str):
    """ This function creates an object from a  JSON string.
    """

    if my_str is None:
        return
    return json.loads(my_str)
