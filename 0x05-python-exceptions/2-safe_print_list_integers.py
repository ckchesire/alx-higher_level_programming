#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Function that prints x elements of a list. If x exceeds
        the length it prints the passed elements without raising
        an error. It also checks if value is an integer if it is
        an integer it gets printed, else the value is skipped.

        Args:
            my_list: Elements in a list to be printed
            x (int): No. of elements to be printed

        Returns:
            No. of elements printed
    """
    count = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
