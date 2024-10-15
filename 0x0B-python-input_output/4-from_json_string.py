#!/usr/bin/python3
""" Module to return an object represented by a JSON string """


import json


def from_json_string(my_str):
    """Function returns an object represented by a JSON string

        Args:
            my_obj: JSON string

        Return:
            returns the object represented by a JSON string
    """
    return json.loads(my_str)
