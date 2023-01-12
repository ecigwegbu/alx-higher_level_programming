#!/usr/bin/python3
""" This module contains a function that
Checks if an object's is a subclass of another specified class"""


def inherits_from(obj, a_class):
    """ Check if object's class is a subclass of a given class"""

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
