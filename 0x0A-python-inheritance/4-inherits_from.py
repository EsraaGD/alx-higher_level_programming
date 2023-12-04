#!/usr/bin/python3
"""Something to write
"""


def inherits_from(obj, a_class):
    """Check if obj is instance of class that inherited

    Args:
        obj: Object to check
        a_class: Class to compare against

    Returns:
        True if true fasle if false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
