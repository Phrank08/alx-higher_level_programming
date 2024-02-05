#!/usr/bin/python3
"""a function that prints a matrix of integers."""
def print_matrix_integer(matrix=[[]]):
    if matrix is not none:
        x = 0
        for horizon in matrix:
            y = 0
            for element in horizon:
                print("{:d} ".format(matrix[x][y], end"")
                y += 1
            print()
            x += 1
