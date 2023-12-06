#!/usr/bin/python3
"""
add_item module.

This module provides a script that adds all command line arguments to a Python list
and saves the list as a JSON representation in a file named add_item.json.

Usage:
    $ python3 add_item.py arg1 arg2 arg3 ...

Dependencies:
    - Python 3.x
    - save_to_json_file module (5-save_to_json_file.py)
    - load_from_json_file module (6-load_from_json_file.py)

Functions:
    - add_items_to_list(): Adds all command line arguments to a Python list and saves it to a file.

    This script uses the save_to_json_file and load_from_json_file functions to
    write and read JSON data to/from a file.

Example:
    $ python3 add_item.py apple banana orange
    # This adds 'apple', 'banana', and 'orange' to the existing list (if any)
    # and saves the updated list to the file add_item.json.

Note:
    - If add_item.json doesn't exist, an empty list is created, and the provided command line arguments are added to it.
    - The script assumes that save_to_json_file and load_from_json_file functions are available in files named
      5-save_to_json_file.py and 6-load_from_json_file.py respectively.

Author:
    OpenAI (GPT-3.5)

"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list():
    """
    Adds all command line arguments to a Python list and saves it to a file.

    If add_item.json doesn't exist, an empty list is created, and the provided
    command line arguments are added to it. The updated list is then saved back
    to the file using the save_to_json_file function.
    """
    # Get the existing list from the file, or create an empty list if the file doesn't exist.
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    # Add command line arguments to the list.
    new_items = sys.argv[1:]
    existing_list.extend(new_items)

    # Save the updated list to the file.
    save_to_json_file(existing_list, "add_item.json")


if __name__ == "__main__":
    add_items_to_list()
