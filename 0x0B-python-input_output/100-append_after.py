#!/usr/bin/python3
""" Defines a function that inserts line of text after specific line """


def append_after(filename="", search_string="", new_string=""):
    """
    A function that inserts a line of text after each line containing a
    specific string

    Args:
        filename (str): The name of a file
        search_string (str): The trigger string
        new_string (str): The string to insert after line with trigger string
    """
    contents = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            contents += line
            if search_string in line:
                contents += new_string

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(contents)
