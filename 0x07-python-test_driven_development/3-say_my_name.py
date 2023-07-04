#!/usr/bin/python3

""" Name Module """

def say_my_name(first_name, last_name=""):
    """
    Function say_my_name - Prints a string with fullname

    Args:
        first_name: First name of the person
        last_name: Last name of the person

    Raises:
        TypeError: If name is not a string

    Returns:
        Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
