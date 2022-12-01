#!/usr/bin/python3
def fizzbuzz():
    # Loop from 1 to 100
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            # Print FizzBuzz
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            # Print Fizz
            print("Fizz", end=" ")
        elif i % 5 == 0:
            # Print Buzz
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
