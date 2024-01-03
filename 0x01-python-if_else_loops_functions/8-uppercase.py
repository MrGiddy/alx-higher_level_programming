#!/usr/bin/python3


def uppercase(string):
    count = 0

    for c in string:
        count += 1
        # if c is lowercase
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            # convert to uppercase
            c = chr(ord(c) - 32)
        # if the last character is not reached
        if (count != len(string)):
            print("{}".format(c), end="")
        # if last character is reached
        else:
            print("{}".format(c))
