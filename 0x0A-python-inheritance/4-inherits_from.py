#!/usr/bin/python3

"""Module to test subclass"""


def inherits_from(obj, a_class):
    """ Check if an obj is a kind of an obj"""
    return isinstance(obj, a_class) and type(obj) is not a_class
