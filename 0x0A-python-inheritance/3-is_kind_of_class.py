#!/usr/bin/python3
""" This module contains a function that
Checks if an object inherits from a specified class"""


def is_kind_of_class(obj, a_class):
    """ Check if object inherits from a specified class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
