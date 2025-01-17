#!/usr/bin/python3
"""Module to send request to a URL and display the X-Request-Id
"""

import sys
import urllib.request


def get_X_request_Id(url):
    """
    Method sends request to URL and extracts value X-Request-Id from the
    header

    Args:
        url (str): url to send request

    Returns:
       str : string representing X-Request-Id
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Syntax: ./1-hbtn_header.py <url>")
        exit(1)
    get_X_request_Id(url)
