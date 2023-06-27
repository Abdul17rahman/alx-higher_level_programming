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
