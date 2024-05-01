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

    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    if nums[-1] > nums[-2]:
        return nums[-1]
    if nums[0] > nums[1]:
        return nums[0]

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
