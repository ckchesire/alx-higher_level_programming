#!/usr/bin/python3
""" Module for sub-class MyList that inherits from list """


class MyList(list):
    """Class with method to print sorted list"""
    pass

    def print_sorted(self):
        """Function that sorted a list"""
        print(sorted(list(self)))
