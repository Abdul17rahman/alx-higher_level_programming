#!/usr/bin/python3
"""module for adding attribute to an object"""


def add_attribute(ob, name, value):
    """
        Function add_attribute - adds attribute to an object
    """
    if hasattr(ob, "__slots__") and name not in ob.__slots__:
        raise TypeError("can't add attribute")
    object.__setattr__(ob, name, value)
