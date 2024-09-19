#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dictionary = a_dictionary
        for k, v in new_dictionary.items():
            v * 2
        return (new_dictionary)
