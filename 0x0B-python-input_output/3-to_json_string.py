#!/usr/bin/python3

""" Json serialization module"""


def to_json_string(my_obj):
    """
        Function to serialize an object
    """
    import json
    return json.dumps(my_obj)
