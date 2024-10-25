#!/usr/bin/python3
""" Creating the base class module """

import os
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Function to return Json string

            Args:
                list_dictionaries (list): List of dictionaries to convert

            Returns:
                str: JSON string representation of list_dictionaries.
                Returns "[]" if list_dictionaries is None or empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list")

        if not all(isinstance(d, dict) for d in list_dictionaries):
            raise TypeError("All elements must be dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances that inherits from Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        json_list = []
        for obj in list_objs:
            json_list.append(obj.to_dictionary())

        json_string = cls.to_json_string(json_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Function to return the list of the JSON string representation

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string or an empty list if
            json_string is None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function to return an instance with all attributes already set

        Args:
            dictionary (dict): dictionary of attributes to set.

        Returns:
            instance: returns an instance of the class with attributes
            set according to the dictionary.
        """
        if dictionary is None:
            return None
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(3, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(2)
        else:
            return None

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Function Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []

        with open(filename, "r", encoding="utf-8") as f:
            json_string = f.read()
            list_dicts = cls.from_json_string(json_string)

        return [cls.create(**d) for d in list_dicts]
