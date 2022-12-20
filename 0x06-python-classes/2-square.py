#!/usr/bin/python3
"""
    This module defines a class Square with private instances
    attribute size and raise exceptions """

class Square:
    """
    Square (class): create a square with the size specified by
    the parameter size and raise error if type is not int or
    size is less than zero.
    Attributes:
        size (int): specify the size of the square.
    Args:
        size (int): size of the square.
    Raises:
        ValueError: if size is less than zero(0).
        TypeError: if size is not an integer.  """

    def __init__(self, size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = 
