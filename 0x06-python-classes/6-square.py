#!/usr/bin/python3

"""Square class"""


class Square:
    """This is an empty sqaure class """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the size and position attributes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(a, int) and a >= 0 for a in position):
            raise TypeError("position must be a tupple of 2 positive integers")
        self.__position = position

    # property decorator/getter for retrieving the size and position

    @property
    def size(self):
        """This retrives our private attribute"""
        return self.__size

    @property
    def position(self):
        """This retrives the val of position"""
        return self.__position

    # Setter, sets the size and position attribute

    @size.setter
    def size(self, value):
        """Perform validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(a, int) and a >= 0 for a in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
