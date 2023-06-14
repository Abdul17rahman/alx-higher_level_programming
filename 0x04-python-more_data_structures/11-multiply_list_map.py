#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ multiply_list_map - Uses the map to multiply

        Args:
            my_list: List of values
            number: num to multiply by

        Returns:
            New list of values
    """
    return list(map(lambda i: i * number, my_list))
