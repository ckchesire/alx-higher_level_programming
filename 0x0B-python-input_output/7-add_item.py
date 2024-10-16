#!/usr/bin/python3
""" Module that adds commmand line arguments to python list and then saves
    them to JSON file
"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(filename):
    """ Function that adds command line arguments to python list and saves
        them to JSON file

        Args:
            filename : Takes filename as input
    """
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    for i, arg in enumerate(sys.argv[1:], start=1):
        my_list.append(arg)

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item('add_item.json')
