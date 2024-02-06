#!/usr/bin/python3
""" Function to check if object is exactly a class instance """


def is_same_class(obj, a_class):
    """
        Checks if an object is exactly an instance of a class

        Args:
            obj (object): Any python object
            a_class (type): The class to check if obj is instan of
    """
    if type(obj) == a_class:
        return True
    return False
