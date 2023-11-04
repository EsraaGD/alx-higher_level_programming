#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for t in row:
            print("{:d}".format(t), end=" ")
        print()
