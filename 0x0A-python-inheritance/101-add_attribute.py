#!/usr/bin/python3
""" This module contains a function that adds
an attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """ Add an attribute if possible """

    if hasattr(obj, "__dict__") or\
            hasattr(obj, "__slot__") and attribute in obj.__slot__:
        obj.__setattr__(attribute, value)
    else:
        raise TypeError("can't add new attribute")
    return
