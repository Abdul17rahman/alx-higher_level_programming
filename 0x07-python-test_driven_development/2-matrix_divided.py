#!/usr/bin/python3

"""This a Matrix Division Module"""


def matrix_divided(matrix, div):
    """
    Function matrix_divided - Divides div by each number in matrix

    Args:
        matrix: The List of numbers (ints or floats)
        div: number to divide by

    Raises:
        TypeError: if matrix is not a list of ints or floats
        TypeError: if one row is bigger or smaller than other
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0

    Returns:
        New Matrix with the division result rounded to
        2 decimal places
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == []
            or not all(isinstance(i, list) for i in matrix)):
        raise TypeError(msg)
    if not all(isinstance(el, (int, float)) for i in matrix for el in i):
        raise TypeError(msg)
    row_len = [len(i) for i in matrix]
    if not all(size == row_len[0] for size in row_len):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    return [list(map(lambda i: round(i / div, 2), row)) for row in matrix]
