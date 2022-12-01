#!/usr/bin/python3
for i in range(0, 100):
    i = str(i).zfill(2)
    if i == '99':
        print("{}".format(i))
    else:
        print("{}, ".format(i), end="")
