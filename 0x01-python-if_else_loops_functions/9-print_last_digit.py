#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        # convert negative number to positive num
        num = -number
        print("{}".format(num % 10), end="")
        return num % 10
    else:
        # Print if number is positive
        print("{}".format(number % 10), end="")
        return number % 10
