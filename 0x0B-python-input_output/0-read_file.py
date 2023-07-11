#!/usr/bin/python3
""" File read module"""


def read_file(filename=""):
    """ 
        Function to read file
    """
    with open(filename) as file:
        content = file.read()
        print(content.rstrip())
