#!/usr/bin/python3
"""takes your GitHub credentials & uses the GitHub API to display your id
"""
import requests
import sys


def display_gitid(username, password):
    """Use basic auth with Personal Access Token as password"""
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data["id"])
    else:
        print(None)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    display_gitid(username, password)
