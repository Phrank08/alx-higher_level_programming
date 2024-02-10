def square_matrix_simple(matrix=[]):
    """ A function that computes the square value of all integers of a matrix"""
    new_matrix = [] 
    for row in matrix:
        new_row = [int(i) ** 2 for i in row]
        new_matrix.append(new_row)
        return new_matrix
