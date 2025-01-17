#!/usr/bin/python3
"""Module to send a POST request to the passed URL with the email as parameter
"""

import sys
import urllib
import urllib.parse
import urllib.request


def post_request(url, email):
    """
    Method that sends a POST request to a URL with the email as parameter
    header

    Args:
        url (str): url to send request
        email (str): email to send

    Returns:
       str : string representing output of a POST request
    """
    data = {'email': 'email'}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, encoded_data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = sys.argv[2]
    except IndexError:
        print("Syntax: ./1-hbtn_header.py <url> <email>")
        exit(1)
    post_request(url, email)
