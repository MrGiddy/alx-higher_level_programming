#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is not None:
        new_list = my_list[:]
        for idx, elem in enumerate(new_list):
            if (elem % 2 == 0):
                new_list[idx] = True
            else:
                new_list[idx] = False
        return new_list
