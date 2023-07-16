#!/usr/bin/python3

from models.base import Base

"""
    Rectangle Class - Inherits from Base
"""


class Rectangle(Base):
    """
        Rectangle

            Args:
                Base - inherited class

            Attributes:
                width - width of the rect
                height - height of the rect
                x - coordinate on the x-axis
                y - coordinate on the y-axis

            Methods
                Constructor(init) - Initalizes the Rect
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initailizing the Rectangle"""
        super().__init__(id)
        super().valid_input("width", width, "dime")
        self.__width = width
        super().valid_input("height", height, "dime")
        self.__height = height
        super().valid_input("x", x)
        self.__x = x
        super().valid_input("y", y)
        self.__y = y

    # Property getters and setters of the instance attributes

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        Base.valid_input(self, "width", val, "dime")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        Base.valid_input(self, "height", val, "dime")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        Base.valid_input(self, "x", val)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        Base.valid_input(self, "y", val)
        self.__y = val

    def area(self):
        """
            Computes the Area of a Rect

            Returns:
                The value of the Area
        """
        return self.__width * self.__height

    def display(self):
        """
            Displays # onto the screen using width and height
        """
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ Prints the class string represenation"""
        clsname = type(self).__name__
        _id = self.id
        _x = self.__x
        _y = self.__y
        w = self.__width
        h = self.__height
        return "[{}] ({}) {}/{} - {}/{}".format(clsname, _id, _x, _y, w, h)
