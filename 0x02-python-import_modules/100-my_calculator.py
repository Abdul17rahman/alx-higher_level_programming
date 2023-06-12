#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

argc = len(sys.argv)
if __name__ == "__main__":
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(int(a), int(b))))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(int(a), int(b))))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(int(a), int(b))))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
