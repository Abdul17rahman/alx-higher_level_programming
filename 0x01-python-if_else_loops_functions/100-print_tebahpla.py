#!/usr/bin/python3


# Create all alphabet in alternate order
def alphabet():
    output = ""
    for i in range(65, 91):
        if i % 2 != 0:
            output += chr(i)
        else:
            output += chr(i + 32)
    return output

# Reverse the Alphabet

def reverse(alphabet):
    str = ""
    for letter in alphabet:
        str = letter + str
    return str

# Assign reverse to a variable
ralpha = reverse(alphabet())

# Print the output
print("{}".format(ralpha), end="")
