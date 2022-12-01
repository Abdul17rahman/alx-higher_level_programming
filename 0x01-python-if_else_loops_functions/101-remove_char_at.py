#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    output = ""
    for i in str:
        if x == n:
            i = ""
        output += i
        x += 1
    return 
