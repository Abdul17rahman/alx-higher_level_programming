#!/usr/bin/python3
def element_at(my_list, idx):
    """element_at retrives an element at a given index

    Args:
        my_list: a list of values
        idx: index of the element

    Returns:
        The element at a given index
    """
    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
