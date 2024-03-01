#!/usr/bin/python3
"""sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response"""
import urllib.request
import urllib.parse
import sys


def post_r(url, email):
    """Sends a POST req with email as a parameter
    & displays the body of the response"""

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        resp = response.read().decode('utf-8')
        print(resp)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_r(url, email)
