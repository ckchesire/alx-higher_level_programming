#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that prints the division of a by b.

        Args:
            a (int): First Integer
            b (int): Second Integer

        Return:
            Returns the result after division
    """
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))

    return (result)
