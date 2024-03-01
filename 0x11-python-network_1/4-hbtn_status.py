#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch_stat_req():
    """must use requests"""

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print("Body resonse:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == "__main__":
    fetch_stat_req()
