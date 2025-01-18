#!/usr/bin/python3
"""Module to send a request to the passed URL and display  body of the response
"""

import sys
import requests


def get_request(url):
    """
    Method that sends a request to a URL

    Args:
        url (str): url to send request

    Returns:
       str : string representing body of the reponse
    """
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print("Syntax: ./7-error_code.py <url>")
        exit(1)
    get_request(url)
