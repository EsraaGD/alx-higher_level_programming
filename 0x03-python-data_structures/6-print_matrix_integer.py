#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for t in row:
            if t != row[-1]:
                print("{:d}".format(t), end=" ")
            else:
                print("{:d}".format(t), end="")
        print()
