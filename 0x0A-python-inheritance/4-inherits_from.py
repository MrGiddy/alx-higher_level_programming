#!/usr/bin/python3
"""
    An inherited class-checking function
"""


def inherits_from(obj, a_class):
    """
        Checks if an object is an instance of a class that
        inherited directly or indirectly from a specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
