#!/usr/bin/python3

""" Text Indentation Module """


def text_indentation(text):

    """
    Function text_indentation - prints a text with 2 new lines

    Args:
        text: The string to print

    Raises:
        TypeError: if text is not a string

    Return:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        # Skip the spaces
        if text[i] == ' ' and (text[i-1] == '?' or text[i-1] == ':'
                                            or text[i-1] == '.'):
            continue
        print("{}".format(text[i]), end="")

        # print 2 line after puctuation
        if text[i] == '?' or text[i] == ':' or text[i] == '.':
            print("\n")
