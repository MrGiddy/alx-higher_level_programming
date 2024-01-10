#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_copy = [row[:] for row in matrix]

    for idx, row in enumerate(matrix_copy):
        matrix_copy[idx] = list(map(lambda x: x**2, row))

    return matrix_copy
