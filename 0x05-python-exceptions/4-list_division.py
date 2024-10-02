#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ Function that divides element by element from two list

        Args:
            my_list_1 (list): list of integers to act as the dividends
            my_list_2 (list): list of integers to act as the divisors
            list_length (int): number of elements to divide

        Return:
            list: Returns a new list with all divisions if successful.
            For invalid cases 0.
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
