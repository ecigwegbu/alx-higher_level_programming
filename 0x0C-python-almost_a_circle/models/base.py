#!/usr/bin/python3
""" This module contains the base module class """

import json

""" This is the Rectangle Class

    Classes:

        Rectangle
"""


class Base:
    """ The base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of a
        a list of dictionaries"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This Class method creates a JSON string and saves it to a file.
        """

        if list_objs is None or len(list_objs) == 0:
            json_str = "[]"
        else:
            ls_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(ls_dicts)
        with open(cls.__name__ + ".json", "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """

        pass
        return
