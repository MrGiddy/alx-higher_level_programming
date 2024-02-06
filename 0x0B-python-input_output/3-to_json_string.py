#!/usr/bin/python3
""" Defines a function that JSON dumps """
import json


def to_json_string(my_obj):
    """
    A function that returns a JSON representation of
    an object

    Args:
        my_obj (any): The object to jsonify

    Return:
        The JSON representation of an object
    """
    return json.dumps(my_obj)
