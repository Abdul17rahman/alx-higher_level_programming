#!/usr/bin/python3

"""Module to test instance"""



def is_same_class(obj, a_class):
    """ Check if an obj is an instance"""
    if isinstance(obj, a_class):
        return True
    return False
