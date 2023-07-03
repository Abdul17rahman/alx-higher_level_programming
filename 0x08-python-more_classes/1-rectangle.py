#!/usr/bin/python3

"""This is a rectangle class"""


class Rectangle:
    """This is a rectangle class """
    def __init__(self, width=0, height=0):
        """Initializing the rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    
    # Class getter properties
    @property
    def width(self):
        """Gets the width"""
        return self.__width
    @property
    def height(self):
        """Gets the height"""
        return self.__height

    # Class setter properties
    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

