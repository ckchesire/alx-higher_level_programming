#!/usr/bin/python3
""" Module to append a string at the end of text files """


def append_write(filename="", text=""):
    """Function that appends a string to the end of atext file and returns the
        number of characters added

        Args:
            filename: text file to write to

        Returns:
            returns the number of characters added to a text file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        chars = f.append(text)

    return chars
