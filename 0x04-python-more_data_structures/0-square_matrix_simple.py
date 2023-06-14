#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ square_matrix_simple - computes the square of the matrix vals

        Args:
            matrix: matrix of values

        Returns:
            New matrix without modifying the original
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col * col)
        new_matrix.append(new_row)
    return new_matrix
