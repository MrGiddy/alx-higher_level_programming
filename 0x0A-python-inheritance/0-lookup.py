#!/usr/bin/python3
""" Definition of lookup function """


def lookup(obj):
    """
        Returns the list of available attributes
        and methods of an object

        Args:
            obj (object): The object
    """
    return list(dir(obj))
