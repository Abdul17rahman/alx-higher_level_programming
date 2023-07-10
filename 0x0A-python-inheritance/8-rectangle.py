#!/usr/bin/python3
"""Define a Rect class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
        Rec class
    """
    def __init__(self, width, height):
        """
            Initialize Rect class

            Args:
                width: width of a rec
                height: height of a rec
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
