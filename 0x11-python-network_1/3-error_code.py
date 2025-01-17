#!/usr/bin/python3
"""Module to send a request to the passed URL and display  body of the response
"""

import sys
import urllib
import urllib.error
import urllib.request


def get_request(url):
    """
    Method that sends a request to a URL

    Args:
        url (str): url to send request

    Returns:
       str : string representing body of the reponse
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Syntax: ./3-error_code.py <url>")
        exit(1)
    get_request(url)
