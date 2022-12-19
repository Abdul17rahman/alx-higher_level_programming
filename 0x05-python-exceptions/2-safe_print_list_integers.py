#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_of_element = 0  # Number of num_of_elementments
    try:
        if x == 0:
            print()
            return x
        for n in range(0, x):
            if type(my_list[n]) is not int:
                continue
            if my_list[n] != my_list[-1] and n != (x - 1):
                print("{:d}".format(my_list[n]), end="")
                num_of_element += 1
            else:
                # Add new line to the last element
                print("{:d}".format(my_list[n]))
                num_of_element += 1
        return num_of_element
    except BaseException:
        return
