#!/usr/bin/python3
"""sends a request to the URL
   & displays the value of the X-Request-Id variable"""
import requests
import sys


def display_xrid2(url):
    """Display val of X-Request-Id"""
    response = requests.get(url)
    xrid2 = response.headers.get('X-Request-Id')
    print(xrid2)


if __name__ == "__main__":
    url = sys.argv[1]
    display_xrid2(url)
