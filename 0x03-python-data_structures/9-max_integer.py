#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:

        biggest_int = my_list[0]

        for idx, elem in enumerate(my_list):
            if my_list[idx] > biggest_int:
                biggest_int = my_list[idx]

        return biggest_int
