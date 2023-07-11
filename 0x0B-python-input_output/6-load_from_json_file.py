#!/usr/bin/python3

""" Json deserialization module"""


def load_from_json_file(filename):
    """
        Function to deserialize an object and save to a file
    """
    import json
    with open(filename) as file:
        return json.load(file)
