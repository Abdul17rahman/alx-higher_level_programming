#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # Check First tuple
    # if second index is empty
    if len(tuple_a) > 0 and len(tuple_a) < 2:
        b = 0
        a = tuple_a[0]

    # if both are empty
    elif len(tuple_a) < 2:
        a, b = 0, 0

    # if first index is empty
    elif tuple_a[0] == '':
        a = 0
        b = tuple_a[1]
    else:
        a, b = tuple_a


    # Check Second tuple
    # if second index is empty
    if len(tuple_b) > 0 and len(tuple_b) < 2:
        d = 0
        c = tuple_b[0]
    # if both are empty
    elif len(tuple_b) < 2:
        c, d = 0, 0
    # if first index is empty
    elif tuple_b[0] == '':
        c = 0
        d = tuple_b[1]
    else:
        c, d = tuple_b

    # Return new tuple
    return (a + c, b + d)
