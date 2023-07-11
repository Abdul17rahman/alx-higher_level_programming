#!/usr/bin/python3

import json
""" Json serialization module"""


def to_json_string(my_obj):
    """
        Function to serialize an object
    """
    return json.dumps(my_obj)
