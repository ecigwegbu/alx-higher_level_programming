#!/usr/bin/python3
""" Module defines Rectangle Class """


class Rectangle:
    """ Rectangle Class Based on 8-Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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
                __str = __str + str(self.print_symbol)
            if i != self.__height - 1:
                __str = __str + "\n"
        return __str

    def __repr__(self):
        """ return the repr of the rectangle """

        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """destructor """

        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        return

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compare rectangles """

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
