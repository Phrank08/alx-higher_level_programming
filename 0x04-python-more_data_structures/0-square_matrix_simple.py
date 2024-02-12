#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ A function that computes the square value of all integers of a matrix"""
    if matrix is not None:
    new_matrix = [] 
    for row in matrix:
        if row is not None:
            new_row = []
            for element in row:    
                new_row.append(element ** 2)
        new_matrix.append(new_row)
        return new_matrix
    else:
        return matrix

