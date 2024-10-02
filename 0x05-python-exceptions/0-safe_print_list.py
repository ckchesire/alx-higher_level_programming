#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Function that prints x elements of list. If x exceeds
        the length it prints the passed elements without raising
        an error.

        Args:
            my_list: Elements in a list to be printed
            x (int): No. of elements to be printed

        Returns:
            No. of elements printed
    """
    count = 0

    try:
        for i in range(0, x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()

    return count
