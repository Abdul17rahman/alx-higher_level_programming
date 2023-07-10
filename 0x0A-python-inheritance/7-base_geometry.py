#!/usr/bin/python3

"""
    BaseGeometry class
"""


class BaseGeometry:
    """This is an base geometry class """
    def __init__(self):
        """ Initializing the geometry"""

    def area(self):
        """Area method that generates an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates an integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
