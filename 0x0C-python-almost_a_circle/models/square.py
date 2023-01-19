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

        print("size getter running...")
        return self.width

    @size.setter
    def size(self, sz):
        """ size property setter """

        self.integer_validator(name="width", value=sz)
        self.width = sz
        self.height = sz
        return
