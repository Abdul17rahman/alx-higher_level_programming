#!/usr/bin/python3
def no_c(my_string):
    """no_c removes all c and C

    Args:
        my_string: string that has c

    Returns:
        A new changed list
    """
    result = ""
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        result += my_string[i]
    return result
