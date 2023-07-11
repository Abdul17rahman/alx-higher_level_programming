#!/usr/bin/python3
""" File write module"""


def write_file(filename="", text=""):
    """
        Function to write to a  file
    """
    with open(filename, 'w') as file:
        return file.write(text)
