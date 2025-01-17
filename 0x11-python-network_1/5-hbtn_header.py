#!/usr/bin/python3
"""Module that fetches url request and displays X-Request-Id
"""

import sys
import requests


def get_url(url):
    """
    Method that fetches a url request and displays X-Request-Id

    Args:
        url (str): URL to be retrieved

    Returns:
        str : returns response string of X-Request-Id
    """
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Syntax: ./5-hbtn_header.py <url>")
        exit()
    get_url(url)
