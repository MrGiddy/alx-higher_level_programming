#!/usr/bin/python3
""" Has text_indentation function """


def text_indentation(text):
    """
        Prints a text with 2 new lines after each delimiter: '.' , '?' and ':'

        Skips all spaces folowing a delimiter

        Args:
            text (str): The input text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    after_delimiter = False

    for char in text.strip(' '):
        if char in ['.', '?', ':']:
            after_delimiter = True
            result += char
            result += '\n\n'
        elif char == '\n':
            result += char
            after_delimiter = True
        elif char == ' ' and after_delimiter:
            continue
        else:
            result += char
            after_delimiter = False

    print(result, end="")
