#!/usr/bin/python3
""" Defines a function that writes a JSON string to a text file """
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file, using a JSON
    representation

    Args:
        my_obj (any): The object to jsonify
        filename (str): The name of the text file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
