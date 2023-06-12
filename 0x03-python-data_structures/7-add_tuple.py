#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """add_tuple - Adds values in tuples

    Args:
        tuple_a: Values in first tuple
        tuple_b: Values in second tuple

    Returns:
        New tuple with added values
    """
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
