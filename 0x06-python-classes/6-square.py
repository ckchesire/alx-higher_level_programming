#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Created an empty class representing a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method that instantiates the
        parameters required for class Square.

        Args:
            __size (int): The size of a square
            __position (tuple) : position of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size value of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size value of a square

        Args:
            value (int): Used to set the size of a square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position of square tuple value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to retrive the position tuple value

        Args:
            value (tuple): Used to set the values for position of square

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function to calculate the Area of a square

            Returns: the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """Function that prints a square using #
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
