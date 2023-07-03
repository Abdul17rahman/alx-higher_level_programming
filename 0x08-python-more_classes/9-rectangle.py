#!/usr/bin/python3

"""This is a rectangle class"""


class Rectangle:
    """This is a rectangle class """

    # Public class variables
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rec"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """str Prints a (#) rectangle)"""
        if self.__width == 0 or self.__height == 0:
            return ""
        str_ = self.print_symbol
        for i in range(self.__height - 1):
            print(str(str_) * self.__width)
        return (str(str_) * self.__width)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # public static method
    @staticmethod
    def bigger_or_equal(self, rect_1, rect_2):
        """Compares the instances of a Rectangle according to the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    # public class method
    @classmethod
    def square(cls, size=0):
        """Sets the dimensions of a Rect to size"""
        return cls(size, size)

