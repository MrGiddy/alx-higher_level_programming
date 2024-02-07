#!/usr/bin/python3
"""
    Defines a function returning a dictionary description
    of the instance of a class for JSON serialization
"""


def class_to_json(obj):
    """
    Returns the dictionary description of the instance of a class
    for JSON serialization

    Args:
        obj : An instance of a class
    """
    return obj.__dict__
