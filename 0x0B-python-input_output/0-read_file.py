#!/usr/bin/python3
""" Defines a function that reads and prints a text file """


def read_file(filename=""):
    """
    Reads and prints a UTF8-encoded text file to stdout

    Args:
        filename (str): The name of the file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
