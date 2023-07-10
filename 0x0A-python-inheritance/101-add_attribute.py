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

        Returns:
            Nothing
    """
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add attribute")
    setattr(ob, name, value)
