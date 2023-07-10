#!/usr/bin/python3

"""Module to test kind of"""


def is_kind_of_class(obj, a_class):
    """ Check if an obj is a kind of an obj"""
    if isinstance(obj, a_class):
        return True
    elif issubclass(a_class, type(obj)):
        return True
    else:
        return False
