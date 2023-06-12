#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """divisible_by_2 - check for multiples of 2

    Args:
        my_list: list of integers

    Returns:
        True for even and False for odd
    """
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
