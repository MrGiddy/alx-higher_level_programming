#!/usr/bin/python3
import sys


def printargs():
    if (len(sys.argv) == 1):
        print("{} arguments.".format(0))
    elif (len(sys.argv) == 2):
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    count = 1
    for arg in sys.argv:
        if (count < len(sys.argv)):
            print("{}: {}".format(count, sys.argv[count]))
        count += 1


if __name__ == "__main__":
    printargs()
