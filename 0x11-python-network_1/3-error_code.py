#!/usr/bin/python3
""" sends a request to the URL
& displays the body of the response (decoded in utf-8)."""
import urllib.request
import urllib.error
import sys


def err(url):
    """manage urllib.error.HTTPError exceptions
    & print: Error code: followed by the HTTP status code"""

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    err(url)
