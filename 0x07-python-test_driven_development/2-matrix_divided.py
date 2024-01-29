""" Has a function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    # Check if matrix is a list of lists of ints and/or floats
    if not matrix:
        raise TypeError(msg1)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg1)
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(msg1)

    # Check if each row of matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError(msg2)

    # Check if div is int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each num in row by div for all rows in matrix
    res_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return res_matrix
