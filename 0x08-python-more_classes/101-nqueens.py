#!/usr/bin/python3
""" Program to solve the N queens puzzle """
import sys


def nqueens():
    """ Solves the N queens puzzle """
    if len(sys.argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
