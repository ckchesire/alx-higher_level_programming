#!/usr/bin/python3
"""Script that fetches internet resources with urllib
"""
import urllib
import urllib.request


def get_url(url):
    """
    Method to fetch content of a given url and print the response body

    Args:
        url (str): URL to fetch

    Returns:
        str: returns the response body
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    get_url(url)
