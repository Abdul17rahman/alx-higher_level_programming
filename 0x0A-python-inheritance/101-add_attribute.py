#!/usr/bin/python3
"""
    module for adding attribute to an object
"""


def add_attribute(ob, name, value):
    """
        Function add_attribute - adds attribute to an object
        Args:
            ob: The object
            name: The attribute to add to.
            value: The value to be added to attribute

        Raises:
            TypeError: If attributed cant be added

        Return:
            Nothing
    """
    if hasattr(ob, "__slots__") and name not in ob.__slots__:
        raise TypeError("can't add attribute")
    object.__setattr__(ob, name, value)
