#!/usr/bin/python3

""" Json deserialization module"""


def from_json_string(my_str):
    """
        Function to deserialize an object
    """
    import json
    return json.loads(my_str)
