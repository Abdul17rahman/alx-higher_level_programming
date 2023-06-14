#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ search_replace - Replaces occurances in a new list

        Args:
            my_list: Original list
            search: element to replace
            replace: new element

        Returns:
            New list with new element
    """
    return [replace if el == search else el for el in my_list]
