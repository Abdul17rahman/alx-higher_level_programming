#!/usr/bin/python3
import hidden_4
# Get executed only if module is executed as main file
if __name__ == "__main__":
    # Loop through the sorted item lists
    # dir() returns a sorted list
    for name in dir(hidden_4):
        if name[0] != '_':
            print(name)
