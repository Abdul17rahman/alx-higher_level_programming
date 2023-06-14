#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ only_diff_elements - semetric different elements

        Args:
            set_1: elements in set 1
            set_2: elements in set 2

        Returns:
            set of unique elements from both
    """
    return set(set_1 ^ set_2)
