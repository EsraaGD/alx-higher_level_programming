#!/usr/bin/python3
"""takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


def searchuser(letter):
    """sends a POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter."""
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    searchuser(letter)
