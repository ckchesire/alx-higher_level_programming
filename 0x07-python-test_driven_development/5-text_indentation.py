#!/usr/bin/python3
"""
Module that adds two new lines after a set of characters.
where there's punctuation i.e('.', ',',':')

"""


def text_indentation(text):
    """ Prints text with added two newlines after
         punctuation characters {'.', '?', ':'}

         Args:
            text: string of characters to modify
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
