#!/usr/bin/python3
""" This module implements my models
It is part of the Almost a circle project
"""


import json


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

        ls_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(list_objs[0].__class__.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(ls_dicts))
