#!/usr/bin/python3
""" Defines a function that creates an object from a 'JSON file' """
import json


def load_from_json_file(filename):
    """
    A function that creates an Ovject from a "JSON file"

    Args:
        filename (str): The name of the JSON file

    Return:
        An Object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.load(f) 

    return obj 
