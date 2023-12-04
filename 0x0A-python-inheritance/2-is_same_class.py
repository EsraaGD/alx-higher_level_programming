#!/usr/bin/python3
"""_summary_
"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (wow): Object in class
        a_class (class): Class

    Returns:
        True if the object belongs to the class. False otherwise
    """
    return type(obj) == a_class
