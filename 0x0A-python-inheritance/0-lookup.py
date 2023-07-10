#!/usr/bin/python3

"""
    Module to show attr and methods
"""


def lookup(obj):
    """ Function that returns the methods and attr of an obj"""
    return list(dir(obj))
