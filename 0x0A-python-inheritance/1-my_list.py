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
        if not (isinstance(i, int) for i in self):
            raise TypeError("List should contain integers only")
        print(sorted(self))
