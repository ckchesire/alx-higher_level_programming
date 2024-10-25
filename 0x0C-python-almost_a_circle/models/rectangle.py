#!/usr/bin/python3
""" Created Rectangle module that inherits from Base Class """

from models.base import Base


class Rectangle(Base):
    """ Creating Rectangle subclass """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiating object variables

            Args:
                width (int): width of rectangle
                height (int): height of rectangle
                x (int): x coordinate
                y (int): y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """ Getter method to retrieve the value of width

            Return:
                Returns the value of the width
        """
        return self.__width

    @width.setter
    def width(self, w_value):
        """ Setter method used to set width value

            Args:
                value(int) : value to be set as width
        """
        self.integer_validator("width", w_value)
        self.__width = w_value

    @property
    def height(self):
        """ Getter method to retrieve the value of height

            Return:
                Returns the value of the height
        """
        return self.__height

    @height.setter
    def height(self, h_value):
        """ Setter method used to set the value of height

            Args:
                value(int): value to be set as the height
        """
        self.integer_validator("height", h_value)
        self.__height = h_value

    @property
    def x(self):
        """ Getter methof to retrive the value of x

            Return:
                Returns the value of x
        """
        return self.__x

    @x.setter
    def x(self, x_value):
        """ Setter method used to set the value of x

            Args:
                value(int): value to be set as x
        """
        self.coord_validator("x", x_value)
        self.__x = x_value

    @property
    def y(self):
        """ Getter method to retrieve the value of y

            Return:
                returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, y_value):
        """ Setter method used to set the value of y

            Args:
                value(int): value to be set as y
        """
        self.coord_validator("y", y_value)
        self.__y = y_value

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
            raise ValueError("{} must be > 0".format(name))

    def coord_validator(self, name, value):
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
        if (value < 0):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ Function to calculate the area of a rectangle

            Returns:
                returns the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """ Function to print out rectangle instance with '#' """
        for i in range(self.height + self.y):
            if i < self.y:
                print('')
            else:
                print(' '*self.x, end='')
                print('#'*self.width)

    def update(self, *args, **kwargs):
        """ Function to update rectangle attributes """
        attrs = ["id", "width", "height", "x", "y"]
        for i, v in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], v)

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
