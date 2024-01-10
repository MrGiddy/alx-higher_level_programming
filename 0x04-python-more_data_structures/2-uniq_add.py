#!/usr/bin/python3

def uniq_add(my_list: list = []) -> int:
    result = 0

    # iterate over unique elements in my_list
    for elem in set(my_list):
        result += elem

    return result
