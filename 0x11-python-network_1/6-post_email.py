#!/usr/bin/python3
"""sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response"""
import requests
import sys


def post_r2(url, email):
    """Sends a POST req with email as a parameter
    & displays the body of the response"""

    payload = {'email': email}
    resp = requests.post(url, data=payload)
    print(resp.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_r2(url, email)
