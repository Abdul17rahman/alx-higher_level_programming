#!/usr/bin/python3

"""Square class"""


class Square:
    """This is an empty sqaure class """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the size and position attributes"""
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(num, int)
                and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
