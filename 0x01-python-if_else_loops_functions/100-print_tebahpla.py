#!/usr/bin/python3
def print_tebahpla():
    """Print alphabet in reverse order, alternating upper and lower-case"""
    for index in range(122, 96, -1):
        copy = index
        if index >= 97:
            if index % 2 != 0:
                copy = index - 32
            print("{}".format(chr(copy)), end="")


print_tebahpla()
