#!/usr/bin/python3

"""This is an empty class"""


class Square:
    """This is an empty sqaure class """

    def __init__(self, size=0):
        """Initializing the size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    # property decorator/getter for retrieving the size

    @property
    def size(self):
        """This retrives our private attribute"""
        return self.__size

    # Setter, sets the size attribute

    @size.setter
    def size(self, value):
        """Perform validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of a square"""
        return (self.__size ** 2)
