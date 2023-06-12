#!/usr/bin/python3
def max_integer(my_list=[]):
    """max_integer - finds the maximum num

    Args:
        my_list: list of integers

    Returns:
        The maximum number
    """
    if my_list == "":
        return None
    max_val = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_val:
            max_val = my_list[i]
    return max_val
