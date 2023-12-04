#!/usr/bin/python3
"""Something to write
"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object

    Args:
        obj: object to retrieve

    Returns:
        A list with names and attributes
    """
    return dir(obj)
