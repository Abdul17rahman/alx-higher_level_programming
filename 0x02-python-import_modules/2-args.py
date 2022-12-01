#!/usr/bin/python3
from sys import argv
length = len(argv)
# Only run if module is executed as main file
if __name__ == "__main__":
    # Argument index starts from 0 while its length from 1
    if length == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, argv[1]))
    elif length == 1:
        print("{} arguments.".format(0))
    elif length > 2:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
