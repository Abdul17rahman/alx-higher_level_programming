#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """element_at replaces an element at a given index

    Args:
        my_list: a list of values
        idx: index of the element
        element: the element to replace

    Returns:
        A new changed list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
