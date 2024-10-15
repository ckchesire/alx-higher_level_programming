#!/usr/bin/python3
""" Module to write string to text files """


def write_file(filename="", text=""):
    """Function that writes a string to a text file and returns the
        number of characters

        Args:
            filename: text file to write to

        Returns:
            returns the number of characters written to a text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        chars = f.write(text)

    return chars
