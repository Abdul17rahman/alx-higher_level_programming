#!/usr/bin/python3
"""
    Base Class Module
"""


class Base:
    """
    This is where our classes inherit from.
        Attr:
            nb_objects: Private class attribute

        Methods:
            Constructor: Initializes the class
            valid_input: Validates inputs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base"""
        if isinstance(id, int) and id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Function to help validate input
    def valid_input(self, name, value, val_typ="cor"):
        """ 
            Validates the input values

            Args:
                name: Name of the field/attribute
                value: Value of the field/attribute
                val_typ: Dimension or Coordinates

            Raises:
                TypeError: If the value is not an int
                ValueError: If the value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if val_typ == "dime":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
