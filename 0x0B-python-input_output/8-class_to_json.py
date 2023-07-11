#!/usr/bin/python3
"""
    Module to return dictionary description with simple data structure
"""


def class_to_json(obj):
    """
       class_to_json - returns dict representation
       Args:
            obj (class): The class
    """
    return obj.__dict__
