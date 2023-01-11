#!/usr/bin/python3
""" This module returns a dictionary which is the
json serialisation of an object
"""


def class_to_json(obj):
    """ This function serialises an object"""

    return obj.__dict__
