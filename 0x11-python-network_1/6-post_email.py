#!/usr/bin/python3
"""Module to send a POST request to the passed URL with the email as parameter
"""

import sys
import requests


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
    data = {'email': email}
    response = requests.post(url, json=data)
    print(response.text)


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        email = sys.argv[2]
    except IndexError:
        print("Syntax: ./6-post_email.py <url> <email>")
        exit(1)
    post_request(url, email)
