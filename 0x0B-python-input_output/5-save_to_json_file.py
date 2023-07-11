#!/usr/bin/python3

""" Json serialization module"""


def save_to_json_file(my_obj, filename):
    """
        Function to serialize an object and save to a file
    """
    import json
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
