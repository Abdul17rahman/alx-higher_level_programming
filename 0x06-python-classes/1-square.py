#!/usr/bin/python3
"""
   This module creates an empty class Square that defines a square
"""
class Square:
    """
    The class Square uses the size argument to create a square
    The __init__ method create a private instance variable size
        Args:
            size (int): Takes an integer."""
    def __init__(self, size):
        self.__size = size
