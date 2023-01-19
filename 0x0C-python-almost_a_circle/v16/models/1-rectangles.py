#!/usr/bin/python3
""" This module implements my models
It is part of the Almost a circle project
"""

from models.base import Base


class Rectangle(Base):
    """ The Rectangle class based on base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width propert getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ width property setter """

        self.__width = value

    @property
    def height(self):
        """ height propert getter """

        return self.__height

    @height.setter
    def height(self, value):
        """ height property setter """

        self.__height = value

    @property
    def x(self):
        """ x propert getter """

        return self.__x

    @x.setter
    def x(self, value):
        """ x property setter """

        self.__x = value

    @property
    def y(self):
        """ y propert getter """

        return self.__y

    @y.setter
    def y(self, value):
        """ y property setter """

        self.__y = value
