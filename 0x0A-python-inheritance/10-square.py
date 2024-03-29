#!/usr/bin/python3
"""Define a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square class
    """
    def __init__(self, size):
        """
            Initialize Square class

            Args:
                size: width of a square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Defining the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Print the default square"""
        clsname = type(self).__name__
        return "[{}] {}/{}".format(clsname, self.__size, self.__size)
