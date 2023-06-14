#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ common_elements - Intersection in sets

        Args:
            set_1: elements in set 1
            set_2: elements in set 2

        Returns:
            set of intersection
    """
    return set(set_1 & set_2)
