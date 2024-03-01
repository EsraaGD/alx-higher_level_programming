#!/usr/bin/python3

"""
This script takes the repository name
& owner name as arguments and uses the GitHub
API to list 10 commits (from the most recent to oldest)
of the repository by the user.
"""

import requests
import sys


def get_commits(repository, owner):
    """
    Retrieves 10 most recent commits of the specified repository by the user.
    """
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {
        'per_page': 10,
        'sha': 'master'
    }
    response = requests.get(url, params=params)
    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repository, owner)
