#!/usr/bin/python3
def uppercase(str):
    string = ''
    for char in str:
        if char.islower():
            string += chr(ord(char) - 32)
        else:
            string += char
    print("{}".format(string))
