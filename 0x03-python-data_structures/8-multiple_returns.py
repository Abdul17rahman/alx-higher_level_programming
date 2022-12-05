#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) < 1:
        tuple = (length, None)
    else:
        tuple = (length, sentence[0])
    return tuple
