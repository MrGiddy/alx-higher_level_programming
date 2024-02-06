#!/usr/bin/python3
""" A child class """


class MyList(list):
    """
    Custom list class that inherits from the built-in list class
    """
    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """ Prints a sorted copy of MyList instance """
        print(sorted(self))
