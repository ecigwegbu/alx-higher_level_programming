#!/usr/bin/python3
""" This module contains a class that defines a student
Student class is to be serialised to json later.
"""


class Student:
    "This class defines a student"""

    def __init__(self, first_name, last_name, age):
        """constructor for the object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        return

    def to_json(self, attrs=None):
        """ serialise self to json """

        isStr = True
        if type(attrs) == list:
            isStr = True
            for elt in attrs:
                if type(elt) != str:
                    isStr is False
        if isStr is False or attrs is None:
            return self.__dict__
        else:
            return {at: self.__dict__[at] for at in attrs if
                    at in self.__dict__}
