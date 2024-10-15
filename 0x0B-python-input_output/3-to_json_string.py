#!/usr/bin/python3
""" Module to return the JSON representation of an object or string """


import json


def to_json_string(my_obj):
    """Function to return the JSON rep of an object

        Args:
            my_obj: python object or string

        Return:
            returns the JSON representation
    """
    return json.dumps(my_obj)
