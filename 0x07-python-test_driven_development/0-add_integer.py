#!/usr/bin/python3
""" Module for adding two integers """
def add_integer(a, b=98):
    """Function that adds two integers

       args:
            a (int, float): First integer
            b (int, float): Second integer, default is 98

       Raises:
            TypeError if a or b are neither an integer or float

        Returns:
            Returns the sum of the integers a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
