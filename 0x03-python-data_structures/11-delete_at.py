#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete_at - deletes an item at a given index

    Args:
        my_list: list of items
        idx: Index to delete

    Returns:
        Nothing
    """
    if idx < 0 or idx > len(my_list):
        return my_list
    del my_list[idx]
    return my_list
