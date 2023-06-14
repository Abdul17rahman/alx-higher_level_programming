#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ multiply_by_2 - Multiply dict values by 2

        Args:
            a_dictionary: dict with values

        Returns:
            dictionary with updated vals
    """
    return {k: val * 2 for k, val in a_dictionary.items()}
