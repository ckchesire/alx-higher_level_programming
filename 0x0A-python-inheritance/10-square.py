#!/usr/bin/python3
""" Module BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class implementation. """

    def area(self):
        """Function to calculate area

           Raises:
            Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate if value is an integer

            Args:
                name (str): The name of the parameter.
                value (int): The value to validate.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle is a Subclass of BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Function to calculate area
        """
        return self.__width * self.__height

    def __str__(self):
        """ Method to print in a user friendly format """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Class square inherits from rectangle """
    def __init__(self, size):
        """ Method to initialize class attributes """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Function to calculate the area of a square
        """
        return self.__size ** 2
