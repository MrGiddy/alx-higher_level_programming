#!/usr/bin/python3
""" Defines a function that appends a string to a text file """


def append_write(filename="", text=""):
    """
    A function that appnds a string to a UTF8-encoded text file

    Args:
        filename (str): The file name/file path
        text (str): The text to append

    Return:
       chars_appended (int): The number of characters added to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        chars_appended = f.write(text)
        return (chars_appended)
