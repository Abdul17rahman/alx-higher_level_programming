#!/usr/bin/python3
from sys import argv
length = len(argv)


def infinite():
    add = 0
    # Argument index start from 0 while length from 1
    if length > 1:
        # Loop through arguments and add each to previous number
        for i in range(1, length):
            add += int(argv[i])
    else:
        add += 0
    return add

# Get execute only if module is import as main file
if __name__ == "__main__":
    print("{}".format(infinite()))
