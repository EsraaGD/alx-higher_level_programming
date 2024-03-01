#!/usr/bin/python3
""" sends a request to the URL
& displays the body of the response (decoded in utf-8)."""
import requests
import sys


def err2(url):
    """if stat code is >= 400, print: Error code:
    followed by the HTTP status code"""

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    err2(url)
