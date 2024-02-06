#!/usr/bin/python3
"""
    Function that checks if an object is kind of a class
"""


def is_kind_of_class(obj, a_class):
    """
        Checks if an object is an instance of a class
        or an instance of a class that inherited from
        the specified class

        Args:
            obj (any): Any python object
            a_class (type): The specific class to check
    """
    if isinstance(obj, a_class):
        return True
    return False
