#!/usr/bin/python3

""" Print Square Module """

def print_square(size):
    """
    Function print_square - Prints a Square of #

    Args:
        size: size of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than zero
        TypeError: If size is float and less than zero

    Return:
        Nothing
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()
