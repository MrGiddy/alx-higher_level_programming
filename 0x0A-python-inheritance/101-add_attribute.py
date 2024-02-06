#!/usr/bin/python3
""" Defines a function that may add a new attribute to an object """


def add_attribute(obj, attr_name, attr_value):
    """
        Adds a new attribute to an object if possible
        Otherwise raises TypeError
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
