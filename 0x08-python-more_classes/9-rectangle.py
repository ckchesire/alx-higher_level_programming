#!/usr/bin/python3
""" Defines a class Rectangle.

    Attributes:
        height: An integer value representing the height of a rectangle
        width: An integer value representing the width of a rectangle
        number_of_instances: Used to keep track of instances created and
                            deleted
        print_symbol: prints symbol that represents a rectangle instance
"""


class Rectangle:
    """ Class to define Rectangle Blueprint. """

    # public class attribute to count no. of instances
    number_of_instances = 0

    # public class attribute to print symbol
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the data values of a rectange

            Args:
                width: int value for width default being 0
                height: int value for height default being 0
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Deleting an object instance """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """ Method to print rectangle  nicely formated
            string outputted using '#'
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        my_string = ''
        for h in range(self.__height):
            my_string += str(self.print_symbol)*self.__width
            my_string += '\n'
        return my_string[:-1]

    def __repr__(self):
        """ Method to print rectangle that returns a more technical
            or recreatable output
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def height(self):
        """ Getter to retrieve height private attribute value

            Returns:
                returns the height private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter sets the height private attribute value.

            Validates the assignment of the height private attribute.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Getter to retrieve width private attribute value

            Returns:
                returns the width private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter sets the width private attribute value.

            Validates the assignment of the width private attribute.

        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Method calcuates the area of a rectangle

            Returns:
                The area of the retangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Method calculates the perimetet of a rectangle

            Returns:
                The perimeter of the rectangle if both height
                and width is greater than zero
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2*self.__height) + (2*self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
