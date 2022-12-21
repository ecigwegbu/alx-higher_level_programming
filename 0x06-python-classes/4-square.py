#!/usr/bin/python3
""" This module contains one class
    Class:
        Square
"""


class Square:
    """This is square contains one private attribute
    It defines a Square."""

    def __init__(self, size=0):
        """This function initialises the object"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Determine the area of the square
        Return: area of square. """

        return self.__size * self.__size

    @property
    def size(self):
        """ Retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square"""

        self.__size = value
