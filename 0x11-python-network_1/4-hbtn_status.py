#!/usr/bin/python3
"""Module that fetches url request
"""

import requests


def get_url(url):
    """
    Method that fetches a url request

    Args:
        url (str): URL to be retrieved

    Returns:
        str : returns response string
    """
    response = requests.get(url)
    body = response.text

    print("Body response")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    get_url(url)
