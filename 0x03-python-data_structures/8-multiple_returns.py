#!/usr/bin/python3
def multiple_returns(sentence):
    """multiple_returns - returns a tuple from a string

    Args:
        sentence: string

    Returns:
        length: length of a string
        char: First character of a string
    """
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
