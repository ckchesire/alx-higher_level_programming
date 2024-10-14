#!/usr/bin/python3
""" Module calling method to list available attributes """


def lookup(obj):
    """Function to print return the list of available attributes and methods
        of an object.

        Args:
            obj : refers to a python object

        Return:
            returns the lis of available attributes and methods
    """
    return dir(obj)
