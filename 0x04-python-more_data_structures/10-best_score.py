#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    i = 0
    result = None
    for key in a_dictionary:
        if a_dictionary[key] > i:
            result = key
            i = a_dictionary[key]
    return result
