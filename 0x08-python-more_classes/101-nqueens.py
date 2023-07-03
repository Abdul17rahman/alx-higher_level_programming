#!/usr/bin/python3

import sys

argc = len(sys.argv)

if argc != 2:
    print("Usage: nqueens N")
    exit(1)
N = sys.argv[1]
try:
    if int(N) < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)
