#!/usr/bin/python3
""" Module to write an Object to a text file using JSON """


import json


def save_to_json_file(my_obj, filename):
    """Function that writes a Json object to a text file

        Args:
            my_obj : python data object
            filename: file to write Json string
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
