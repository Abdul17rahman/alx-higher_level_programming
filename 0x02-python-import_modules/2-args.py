#!/usr/bin/python3
import sys
argc = len(sys.argv)
if __name__ == "__main__":
    length = argc - 1
    if argc < 2:
        print("{} arguments.".format(length))
    elif argc == 2:
        print("{} argument:".format(length))
        print("{}: {}".format(length, sys.argv[length]))
    else:
        print("{} arguments:".format(length))
        for arg in range(1, argc):
            print("{}: {}".format(arg, sys.argv[arg]))
