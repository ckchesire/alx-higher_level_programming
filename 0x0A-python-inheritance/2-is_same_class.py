#!/usr/bin/python3
""" Module to check if an object is same as specified class """


def is_same_class(obj, a_class):
    """Function checks if an object is the same as a class
    """
    return type(obj) is a_class
