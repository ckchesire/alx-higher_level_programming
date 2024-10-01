#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Created an empty class representing a Square
    """
    def __init__(self, size=0):
        """The __init__ method that instantiates the
        parameters required for class Square.

        Args:
            size (int): The size of a square
        """
        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size value of a square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Setter method to set the size value of a square

        Args:
            size (int): Used to set the size of a square
        """
        if not (isinstance(size, int)):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Function to calculate the Area of a square
        """
        return int(self.__size) ** 2
