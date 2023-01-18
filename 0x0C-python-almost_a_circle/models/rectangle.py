#!/usr/bin/python3
""" This module implements my models
It is part of the Almost a circle project
"""

from models.base import Base


class Rectangle(Base):
    """ The Rectangle class based on base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.integer_validator(name="width", value=width)
        self.integer_validator(name="height", value=height)
        self.integer_validator(name="x", value=x)
        self.integer_validator(name="y", value=y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width propert getter """

        return self.__width

    @width.setter
    def width(self, width):
        """ width property setter """

        self.integer_validator(name="width", value=width)
        self.__width = width

    @property
    def height(self):
        """ height propert getter """

        return self.__height

    @height.setter
    def height(self, height):
        """ height property setter """

        self.integer_validator(name="height", value=height)
        self.__height = height

    @property
    def x(self):
        """ x propert getter """

        return self.__x

    @x.setter
    def x(self, x):
        """ x property setter """

        self.integer_validator(name="x", value=x)
        self.__x = x

    @property
    def y(self):
        """ y propert getter """

        return self.__y

    @y.setter
    def y(self, y):
        """ y property setter """

        self.integer_validator(name="y", value=y)
        self.__y = y

    def integer_validator(self, name, value):
        """ validate function """

        if type(value) != int:
            if type(value) == float:
                if value % 1 != 0:
                    raise TypeError(name + " must be an integer")
            else:
                raise TypeError(name + " must be an integer")
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(name + " must be > 0")
        elif name == "x" or name == "y":
            if value < 0:
                raise ValueError(name + " must be >= 0")
            return
