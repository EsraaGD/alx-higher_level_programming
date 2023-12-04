#!/usr/bin/python3
"""_summary_
"""


def is_kind_of_class(obj, a_class):
    """_summary_

    Args:
        obj: Object to check
        a_class: class to compare against

    Returns:
        True if object is instance of class, or inherited
    """
    return isinstance(obj, a_class)
