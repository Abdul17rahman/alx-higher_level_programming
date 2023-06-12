#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print_matrix_integers - prints a matrix

    Args:
        matrix: nested list

    Returns:
        Nothing
    """
    if matrix == None:
        pass
    for i in matrix:
        for n in i:
            if n != i[-1]:
                print("{:d}".format(n), end=" ")
            else:
                print("{:d}".format(n))
