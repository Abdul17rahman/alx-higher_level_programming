#!/usr/bin/python3
""" File append module"""


def append_write(filename="", text=""):
    """
        Function to append to a file
    """
    with open(filename, 'a') as file:
        return file.write(text)
