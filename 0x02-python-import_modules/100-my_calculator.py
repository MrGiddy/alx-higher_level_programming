#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def my_calculator(argv):
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if (operator == "+"):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (operator == "-"):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (operator == "*"):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif (operator == "/"):
        print("{} / {} = {:.0f}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    my_calculator(argv=sys.argv)
