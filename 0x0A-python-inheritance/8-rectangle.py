#!/usr/bin/python3
""" This module improves Basegeometry class
Rectangle class inherits from it
"""


class BaseGeometry:
    """ BaseGeometry class """

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
        return value


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ Construct rectangle """

        self._Rectangle__width = self.integer_validator("width", width)
        self._Rectangle__height = self.integer_validator("height", height)
