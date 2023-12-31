#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result_matrix = [[0] * num_cols for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
