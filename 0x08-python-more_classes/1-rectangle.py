#!/usr/bin/python3
""" Defines a class Rectangle.

    Attributes:
        height: An integer value representing the height of a rectangle
        width: An integer value representing the width of a rectangle
"""


class Rectangle:
    """ Class to define Rectangle Blueprint. """

    def __init__(self, width=0, height=0):
        """ Initializes the data values of a rectange

            Args:
                width: int value for width default being 0
                height: int value for height default being 0
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Getter to retrieve height private attribute value

            Returns:
                returns the height private attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter sets the height private attribute value.

            Validates the assignment of the height private attribute.

        Arg:
            height: the value to be set
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ Getter to retrieve width private attribute value

            Returns:
                returns the width private attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter sets the width private attribute value.

            Validates the assignment of the width private attribute.

        Arg:
            height: the value to be set
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
