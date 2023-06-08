#!/usr/bin/python3
import sys
argc = len(sys.argv)
if __name__ == "__main__":
    length = argc - 1
    total = 0
    if argc < 2:
        print("{}".format(length))
    else:
        for arg in range(1, argc):
            total += int(sys.argv[arg])
        print("{}".format(total))
