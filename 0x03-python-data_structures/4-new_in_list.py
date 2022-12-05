#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx >= len(my_list):
        return my_list.copy()
    else:
        list = my_list.copy()
        list[idx] = element
        return list
