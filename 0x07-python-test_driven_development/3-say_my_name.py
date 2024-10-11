#!/usr/bin/python3
""" Module to print out a name """


def say_my_name(first_name, last_name=""):
    """ Function that prints out name

        Args:
            first_name (str): first name string value
            last_name (str): last name string value

        Return:
            Method returns a print out of first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return print(f"My name is {first_name} {last_name}")
