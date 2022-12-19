#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    try:
        for i in range(0, list_length):
            div = my_list_1[i] / my_list_2[i]
            list[i] = int(div)
        return list
    except IndexError:
        print("Out of range")
    except ValueError:
        print("wrong type")
