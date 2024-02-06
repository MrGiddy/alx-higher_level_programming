#!/usr/bin/python3
""" Defines a function that json loads """
import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (string): A JSON string

    Return:
        An object (Python data structure)
    """
    return json.loads(my_str)
