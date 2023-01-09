#!/usr/bin/python3

"""

    Module to create a sub class from list class

"""





class MyList(list):

    """

        MyList - inherit from list and perform basic list operations

        Attributes:

            print_sorted(): print the list in sorted and ascending order

    """

    def print_sorted(self):

        sorted_list = self.copy()

        sorted_list.sort()

        print(sorted_list)
