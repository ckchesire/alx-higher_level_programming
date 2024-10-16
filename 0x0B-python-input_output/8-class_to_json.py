#!/usr/bin/python3
""" Module to convert Class to JSON """


def class_to_json(obj):
    """Function to convert Class to JSON

        Args:
            obj : class object to be converted

        Returns:
            returns the dictionary description
    """
    res = {}
    for k, v in obj.__dict__.items():
        if isinstance(v, (list, dict, str, int, bool)):
            res[k] = v
    return res
