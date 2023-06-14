#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ print_sorted_dictionary - Sorts the keys

        Args:
            a_dictionary: dict to loop

        Returns:
            Nothing
    """
    for key, vl in sorted(a_dictionary.items()):
        print("{}: {}".format(key, vl))
