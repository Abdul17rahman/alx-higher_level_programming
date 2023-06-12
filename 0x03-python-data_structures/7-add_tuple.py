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
    max_len = max(len_a, len_b)
    min_len = min(len_a, len_b)
    tuple_sum = []
    for i in range(max_len):
        if i < min_len:
            tuple_sum.append(tuple_a[i] + tuple_b[i])
        elif len_a == max_len:
            tuple_sum.append(tuple_a[i])
        else:
            tuple_sum.append(tuple_b[i])
    return tuple(tuple_sum)
