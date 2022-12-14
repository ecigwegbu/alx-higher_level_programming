#!/usr/bin/python3
""" This module improves Basegeometry and Rectangle classes
Square class inherits from Rectangle Class
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
        return


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """ Construct rectangle """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangle__width = width
        self._Rectangle__height = height

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return "[Rectangle] " + str(self._Rectangle__width) + "/" +\
                str(self._Rectangle__height)


class Square(Rectangle):
    """ Inherits from Rectangle which in turn
    inherits from BaseGeometry"""

    def __init__(self, size):
        """ Construct square """

        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
        self._Square__size = size

    def area(self):

        return super().area()

    def __str__(self):
        return "[" + self.__class__.__name__ + "] " +\
                str(self._Rectangle__width) + "/" +\
                str(self._Rectangle__height)
