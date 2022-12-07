#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = []
    for i in sorted(a_dictionary):
        list.append(i)
    for key in list:
        print("{}: {}".format(key, a_dictionary.get(key)))
