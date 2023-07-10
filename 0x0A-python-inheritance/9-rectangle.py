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

    def area(self):
        """Defining the area of the rect"""
        return self.__width * self.__height

    def __str__(self):
        """Print the default Rect"""
        clsname = type(self).__name__
        return "[{}] {}/{}".format(clsname, self.__width, self.__height)
