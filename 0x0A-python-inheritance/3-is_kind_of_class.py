#!/usr/bin/python3
""" This module contains a function that
Checks if an object is an instance of a class"""


def def is_kind_of_class(obj, a_class):
    """ Check if object is an instance of a class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
