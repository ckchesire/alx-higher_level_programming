#!/usr/bin/python3
""" Module to check if an object is an instance of inherited class. """


def inherits_from(obj, a_class):
    """Function to check if object is an instance of an inherited class
        or a subclss.

        Args:
            obj : this is an object instance
            a_class : this refers to the original object class

        Returns
            returns true conditions are met
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
