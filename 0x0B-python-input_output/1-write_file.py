#!/usr/bin/python3
""" Defines a function that writes a string to a text file """


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file

    Args:
        filename (str): Name of the text file
        text (str): The string to write

    Returns:
        written (int): Number of characters written to file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        written = f.write(text)
        return (written)
