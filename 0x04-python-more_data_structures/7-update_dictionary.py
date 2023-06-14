#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ update_dictionary - update key and value in dict

        Args:
            a_dictionary: dict to loop
            key: The key to update
            value; The new value

        Returns:
            dictionary with updated vals
    """
    a_dictionary[key] = value
    return a_dictionary
