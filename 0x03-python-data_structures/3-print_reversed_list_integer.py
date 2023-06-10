#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print int values in a list in reverse

    Args:
        my_list: a list of integers defaults to empty

    Returns:
        Nothing
    """
    if my_list == None:
        pass
    else:
        my_list.sort(reverse = True)
        for num in my_list:
            print("{:d}".format(num))
