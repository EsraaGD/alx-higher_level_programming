#!/usr/bin/python3
"""sends a request to the URL
   & displays the value of the X-Request-Id variable"""
import urllib.request
import sys


def display_xrid(url):
    """Display val of X-Request-Id"""
    with urllib.request.urlopen(url) as response:
        xrid = response.getheader('X-Request-Id')
        print(xrid)


if __name__ == "__main__":
    url = sys.argv[1]
    display_xrid(url)
