#!/usr/bin/python3

""" Addition Module """


def add_integer(a, b=98):
    """
    Function add_integer adds two numbers (integers or floats)

    Args:
        a: first number(int or float)
        b: second number(int or float)

    Raises:
        TypeError: For values that are not numbers

    Returns:
        The sum of two numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
