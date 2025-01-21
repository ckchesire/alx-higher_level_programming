#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """Method to find the peak with the shortest algorithm

       Args:
          list_of_integers (list) : list containing unordered integers

       Returns:
          returns peak integer or none if list is empty
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 0:
        return (None)
    elif size == 1:
        return (list_of_integers[0])
    elif size == 2:
        return max(list_of_integers)

    mid = int(size/2)
    peak = list_of_integers[mid]
    mylist = list_of_integers
    if peak > mylist[mid - 1] and peak > mylist[mid + 1]:
        return peak
    elif peak < mylist[mid -1]:
        return find_peak(mylist[:mid])
    else:
        return find_peak(mylist[mid + 1:])
