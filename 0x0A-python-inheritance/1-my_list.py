#!/usr/bin/python3

"""
    Module to Sort a list
"""

class MyList(list):
    """This class prints a sorted list """

    def __init__(self):
        """Initialise MyList"""
        super().__init__()

    def print_sorted(self):
        """ Print sorted list"""
        print(sorted(self))
