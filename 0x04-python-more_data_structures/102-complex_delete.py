#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = [k for k, val in a_dictionary.items() if val == value]
    for k in del_keys:
        del a_dictionary[k]
    return a_dictionary
