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

    def to_json(self):
        """ serialise self to json """

        return self.__dict__
