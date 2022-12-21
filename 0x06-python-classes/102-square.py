#!/usr/bin/python3
""" This module contains one class
    Class:
        Square
"""


class Square:
    """ This is square contains one private attribute
    It defines a Square."""

    def __init__(self, size=0):
        """ This function initialises the object """

        if (type(size) != int) && (type(size) != float):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Determine the area of the square
        Return: area of square. """

        return self.__size * self.__size

    @property
    def size(self):
        """ Retrieve the size of the square """

        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square """

        if (type(size) != int) && (type(size) != float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """ Check if object is equal to another """
 
        return self.area == other.area

    def __ne__(self, other):
        """ Check if object is not equal to another """

        return self.area != other.area

    def __gt__(self, other):
        """ Check if object is greater than another """

        return self.area > other.area

    def __ge__(self, other):
        """ Check if object is greater than or equal to another """

        return self.area >= other.area

    def __lt__(self, other):
        """ Check if object is less than another """
 
        return self.area < other.area

    def __le__(self, other):
        """ Check if object is less than or equal to another """

        return self.area <= other.area
