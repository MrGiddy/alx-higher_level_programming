#!/usr/bin/python3
"""Defines a function, find_peak for a list of integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list): A list of unsorted integers
    Return:
        A peak value
    """
    nums = list_of_integers[:]

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        # if the right neighbour is greater
        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            left = mid + 1
        # if the left neighbour is greater
        elif mid > 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
        else:
            return nums[mid]
