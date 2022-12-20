#!/usr/bin/python3
"""
    This module defines a class Square with
    private instance, attribute, public instance method
    setter and getter to modify private instance and raise exceptions """

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
        TypeError: if size is not an integer.
    """
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """ :size: returns the private instances size """
        return self.__size

    @size.setter
    def size(self, size):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
    def area(self):
        """
        Calculate area of the square and return the result
        Returns:
            Square area.
        """
        area = self.__size * self.__size
        return area
