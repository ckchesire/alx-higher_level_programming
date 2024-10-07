#!/usr/bin/python3
""" Defines a class Rectangle. """


class Rectangle:
    """ Class to define Rectangle Blueprint. """

    def __init__(self, width=0, height=0):
        """ Initializes the data values """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be >= 0")
        self.__width = width
