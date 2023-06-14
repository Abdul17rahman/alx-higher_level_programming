#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ uniq_add - Adds all uniq ints

        Args:
            my_list: List of Ints

        Returns:
            The sum of uniq Ints
    """
    set_of_ints = set(my_list[:])
    return sum(set_of_ints)
