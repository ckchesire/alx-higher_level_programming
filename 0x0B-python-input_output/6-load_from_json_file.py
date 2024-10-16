#!/usr/bin/python3
""" Module to that creates an Object from JSON file"""


import json


def load_from_json_file(filename):
    """Function that creates an object from Json file

        Args:
            filename: Json file to read from
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
