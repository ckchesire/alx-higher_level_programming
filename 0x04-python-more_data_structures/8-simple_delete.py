#!/usr/bin/python3i
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
        return (a_dictionary)
    return (a_dictionary)
