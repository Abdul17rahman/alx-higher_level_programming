#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple - Adds values in tuples

    Args:
        tuple_a: Values in first tuple
        tuple_b: Values in second tuple

    Returns:
        New tuple with added values
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len_b < 2:
        if len_b == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
