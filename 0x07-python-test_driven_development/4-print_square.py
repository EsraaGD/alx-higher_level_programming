#!/usr/bin/python3
"""Define function"""


def print_square(size):
    """Print square with size size using #

    Args:
        size (int): size of lenghth of square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
