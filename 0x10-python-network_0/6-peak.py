#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak integer found in the list.
    - None if the list is empty.
    """
    if not list_of_integers:
        return None

    return max(list_of_integers)
