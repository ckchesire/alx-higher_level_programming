#!/usr/bin/python3
""" Module BaseGeometry """


class BaseGeometry:
    """ BaseGeometry class implementation. """

    def area(self):
        """Function to calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate if value is an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
