#!/usr/bin/python3
""" Module prints square representation """


def print_square(size):
    """ Function prints a square based on # symbol

        Args:
            size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#"*size)
