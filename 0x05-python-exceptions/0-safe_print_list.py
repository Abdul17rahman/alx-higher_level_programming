#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    el = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            el += 1
        except:
            break
    print()
    return el
