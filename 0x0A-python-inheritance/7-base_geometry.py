#!/usr/bin/python3
""" This module improves Basegeometry class
"""


class BaseGeometry:
    """ Inherit improves another class """

    def area(self):
        """ not yet implemented"""

        raise Exception("area() is not implemented")
        return

    def integer_validator(self, name, value):
        """ validate function """

        if type(value) != int:
            if type(value) == float:
                if value % 1 != 0:
                    raise TypeError(name + " must be an integer")
            else:
                raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

        return
