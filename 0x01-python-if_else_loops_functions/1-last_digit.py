#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    # Change to positive to get last number
    num = -number
    # Get the last number
    num %= 10
    # Return back to negative
    num = -num
else:
    num = number % 10

if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif num < 6:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
