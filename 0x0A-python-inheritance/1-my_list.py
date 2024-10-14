#!/usr/bin/python3
""" Module that prints a sorted list in ascending order """


class MyList(list):
    """ Class with method to print a sorted list """
    pass

    def print_sorted(self):
        """Function that prints a list sorted in ascending order
        """
        print(sorted(list(self)))
