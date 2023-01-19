#!/usr/bin/python3
""" This module implements my models
It is part of the Almost a circle project
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square class based on Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for Square Class"""
        super().__init__(size, size, x, y, id)
        return

    def __str__(self):
        """ return the string version of the Square """
        return f"[Square] ({self.id}) {self.x}\
/{self.y} - {self.width}"

    @property
    def size(self):
        """ size propert getter """

        return self.width

    @size.setter
    def size(self, sz):
        """ size property setter """

        self.integer_validator(name="width", value=sz)
        self.width = sz
        self.height = sz
        return

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute """

        attrs = ("id", "size", "x", "y")
        if args is None or len(args) == 0:
            # do **kwargs
            for at, arg in kwargs.items():
                if at in attrs:
                    self.__setattr__(at, arg)
                else:
                    raise AttributeError(at +
                                         " does not exist in Square class")
        else:
            for at, arg in zip(attrs, args):
                self.__setattr__(at, arg)

        return
