#!/usr/bin/python3

"""

    module to create a class Rectangle that defines a rectangle

"""





class Rectangle():



    """

    Rectangle - defines a rectangle

    Attributes:

        width (int): width class attribute

        height (int): height class attribute

        area(): returns the rectangle area

        perimeter(): returns the rectangle parameter

        __str__: print rectangle with character #

        __repr__: return a string representation of

                 the rectangle to be able to recreate

                 a new instance by using eval()

        ___del___: Print the message Bye rectangle...

        number_of_instances (int): count the number of instance

        print_symbol (any type): Used as symbol for string representation

    Args:

        width (int): width of the rectangle

        height (int): height of the rectangle

    Raises:

        TypeError: width must be an integer

        ValueError: width must be >= 0

        TypeError: height must be an integer

        ValueError: height must be >= 0

    """



    number_of_instances = 0

    print_symbol = "#"



    def __init__(self, width=0, height=0):

        if type(width) != int:

            raise TypeError("width must be an integer")

        elif width < 0:

            raise ValueError("width must be >= 0")

        elif type(height) != int:

            raise TypeError("height must be an integer")

        elif height < 0:

            raise ValueError("height must be >= 0")

        else:

            self.__width = width

            self.__height = height

            type(self).number_of_instances += 1

            self.print_symbol = Rectangle.print_symbol



    @property

    def width(self):

        return self.__width



    @property

    def height(self):

        return self.__height



    @width.setter

    def width(self, value):

        if type(value) != int:

            raise TypeError("width must be an integer")

        elif value < 0:

            raise ValueError("width must be >= 0")

        else:

            self.__width = value



    @height.setter

    def height(self, value):

        if type(value) != int:

            raise TypeError("height must be an integer")

        elif value < 0:

            raise ValueError("height must be >= 0")

        else:

            self.__height = value



    def area(self):

        return self.__height * self.__width



    def perimeter(self):

        if self.__width == 0 or self.__height == 0:

            return 0

        else:

            return 2 * (self.__height + self.__width)



    def __str__(self):

        h = self.__height

        w = self.__width

        if h == 0 or w == 0:

            return ''

        else:

            ch = self.print_symbol

            for i in range(0, h - 1):

                print(str(ch) * w)

            return (str(ch) * w)



    def __repr__(self):

        rp = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

        return rp



    def __del__(self):

        type(self).number_of_instances -= 1

        print("Bye rectangle...")
