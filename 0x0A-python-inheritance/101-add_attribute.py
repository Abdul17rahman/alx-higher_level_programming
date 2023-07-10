#!/usr/bin/python3
"""
    module for adding attribute to an object
"""


def add_attribute(mc, name, value):
    """
        Function add_attribute - adds attribute to an object
        Args:
            mc: The object
            name: The attribute to add to.
            value: The value to be added to attribute

        Raises:
            TypeError: If attributed cant be added

        Returns:
            Nothing
    """
    if type(mc) not in [int, tuple, dict, str, list, float]:
        mc.name = value
    else:
        raise TypeError("can't add attribute")
