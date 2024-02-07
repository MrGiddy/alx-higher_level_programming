#!/usr/bin/python3
""" Defines a function that returns rows of Pascal's Triangle """


def pascal_triangle(n):
    """
    A function that returns rows a a Pascal's triangle

    Args:
        n (int): The number of rows to return
    """
    if n == 0:
        return []

    triangle = [[1]]
    for i in range(n-1):
        temp = [0] + triangle[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j+1])
        triangle.append(row)
    return triangle
