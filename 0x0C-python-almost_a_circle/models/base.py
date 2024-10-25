#!/usr/bin/python3
""" Creating the base class module """

import json


class Base:
    """ Implement base class blueprint """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the object variables """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ Function to return Json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
