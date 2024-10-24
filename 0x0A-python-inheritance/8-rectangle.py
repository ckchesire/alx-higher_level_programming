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
