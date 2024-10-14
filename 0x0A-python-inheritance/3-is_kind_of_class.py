#!/usr/bin/python3
""" Module to check same class or inherit from """


def is_kind_of_class(obj, a_class):
    """Function to check if object is an instance of a class or the object is
        an instance of a class that inherited from the specified class

        Args:
            obj : this is an object instance
            a_class : this refers to the original object class

        Returns
            returns true conditions are met
    """
    return isinstance(obj, a_class)
