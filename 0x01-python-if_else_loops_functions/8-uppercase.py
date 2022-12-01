#!/usr/bin/python3
def uppercase(str):
    upper = ""
    # Loop through the string
    for each in str:
        if ord(each) >= 97 and ord(each) < 124:
            # convert to uppercase
            upper += chr(ord(each)-32)
        else:
            upper += each
    # Print using format method
    print("{}".format(upper))
