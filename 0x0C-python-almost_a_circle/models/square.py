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
        """ Get the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the value of the square and validate through rectangle."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Function to update square attributes """
        attrs = ["id", "size", "x", "y"]
        for i, v in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], v)

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
