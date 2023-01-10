#!/usr/bin/python3
""" This module is for a function
that creates a JSON string
"""

import json


def to_json_string(my_obj):
    """ This function creates a JSON string.
    """

    if my_obj is None:
        return
    return json.dumps(my_obj)
