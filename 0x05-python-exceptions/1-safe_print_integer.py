#!/usr/bin/python3
def safe_print_integer(value):
    """ This function checks if value is an integer and returns either
        true or false. If true it prints the integer value.

        Args:
            value (int): value to be checked if its an integer

        Return:
            Returns boolean either True or False
    """
    boolean = False

    try:
        if isinstance(value, int):
            boolean = True
            print("{:d}".format(value))
    except ValueError:
        pass

    return boolean
