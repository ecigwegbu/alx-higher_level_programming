#!/usr/bin/python3
""" This module implements my models
It is part of the Almost a circle project

    Classes:
        Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ The Rectangle class based on base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor for Rectangle Class"""

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
        """ x property getter """

        return self.__x

    @x.setter
    def x(self, x):
        """ x property setter """

        self.integer_validator(name="x", value=x)
        self.__x = x

    @property
    def y(self):
        """ y property getter """

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

    def area(self):
        """ Compute the area of the rectangle """

        return self.width * self.height

    def display(self):
        """ Display the rectangle """

        __str = ""
        if self.__width == 0 or self.__height == 0:
            pass
        else:
            __str = "\n" * self.__y
            for i in range(self.__height):
                __str += " " * self.__x
                for j in range(self.__width):
                    __str = __str + "#"
                if i != self.__height - 1:
                    __str = __str + "\n"
        print(__str)

    def __str__(self):
        """ return the string version of the Rectangle """

        return f"[Rectangle] ({self.id}) {self.__x}\
/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute """

        attrs = ("id", "width", "height", "x", "y")
        if args is None or len(args) == 0:
            # do **kwargs
            for at, arg in kwargs.items():
                if at in attrs:
                    self.__setattr__(at, arg)
                else:
                    raise AttributeError(at +
                                         " does not exist in Rectangle class")
        else:
            # do *args
            for at, arg in zip(attrs, args):
                self.__setattr__(at, arg)
        return

    def to_dictionary(self):
        """ Return a dictionary representation of Rectangle """

        return {key: self.__getattribute__(key) for key in
                ["id", "width", "height", "x", "y"]}
