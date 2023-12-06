#!/usr/bin/python3
"""add_item module.

Contains a script that adds all command line arguments to a Python list and
saves the list as a JSON representation in a file named add_item.json.
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_list():
    """Adds all command line arguments to a Python list and saves it to a file."""
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
