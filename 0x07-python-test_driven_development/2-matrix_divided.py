#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
    - matrix (list of lists): Matrix of integers or floats.
    - div (number): Number (integer or float) to divide the elements by.

    Returns:
    - list of lists: New matrix with elements divided by div, round 2 dec place

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats.
    - TypeError: If each row of the matrix does not have the same size.
    - TypeError: If div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """
    if not matrix:
        return matrix

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_num = round(num / div, 2)
            new_row.append(new_num)
        new_matrix.append(new_row)
    return new_matrix
