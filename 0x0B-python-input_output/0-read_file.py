#!/usr/bin/python3
""" Module to read text files """


def read_file(filename):
    """Function that reads text file and prints to stdout

        Args:
            filename: text file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
