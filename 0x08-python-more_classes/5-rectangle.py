#!/usr/bin/python3
""" Module defines Rectangle Class """


class Rectangle:
    """ Rectangle Class Based on 2-Rectangle"""

    def __init__(self, width=0, height=0):
        """ Constructor """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width propert getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ widgth property setter"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height propert getter """

        return self.__height

    @height.setter
    def height(self, value):
        """ height property setter"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Determine the area of the rectangle
        Return: area of rectangle. """

        return self.__width * self.__height

    def perimeter(self):
        """ Determine the perimeter of the rectangle
        Return: perimeter of rectangle. """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ return string representation of Rectangle """

        if self.__width == 0 or self.__height == 0:
            return ""
        __str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                __str = __str + "#"
            if i != self.__height - 1:
                __str = __str + "\n"
        return __str

    def __repr__(self):
        """ return the repr of the rectangle """

        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        return
