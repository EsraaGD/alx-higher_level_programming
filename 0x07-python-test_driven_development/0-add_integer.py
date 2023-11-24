#!/usr/bin/python3
    """Define int additon function"""
    
    
def add_integer(a, b=98):
    """Adds two numbers a & b that are integers or floats

    Args:
        a (int or float): first number
        b (int or float): second number

    Raises:
        TypeError: if either a or b are not an integer or a float

    Returns:
        int: Sum of a and b as integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)