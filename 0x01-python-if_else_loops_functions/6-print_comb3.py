#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a != b and b > a:
            print("{}{}".format(a, b), end="")
            if (a + b) != 17:
                print(", ", end="")
            else:
                print("")
