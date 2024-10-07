#!/usr/bin/python3
def add_integer(a, b=98):
    """Function that adds two integers

        args:
        (a, int): First integer
        (b, int): Second integer

        Raises:
        TypeError if a or b are neither and integer or float

        Returns:
        Returns the sum of the integers a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
