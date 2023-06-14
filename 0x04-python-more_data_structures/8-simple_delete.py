#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ simple_delete - deletes key and value in dict

        Args:
            a_dictionary: dict to loop
            key: The key to delete

        Returns:
            dictionary with updated vals
    """
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    return a_dictionary
