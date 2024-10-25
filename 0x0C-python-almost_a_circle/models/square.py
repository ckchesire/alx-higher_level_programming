#!/usr/bin/python3
""" Create a module square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Create square module that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Get the size of the Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the value of the square and validate through rectangle."""
        self.width = value
        self.height = value
