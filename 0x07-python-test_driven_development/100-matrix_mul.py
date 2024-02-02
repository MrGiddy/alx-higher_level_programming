#!/usr/bin/python3
""" Has definition for function matrix_mul that multiplies two matrices """


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists): Matrix a
        m_b (list of lists): matrix b
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    # Check that num cols m_a == num rows m_b
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply m_a and m_b
    new_matrix = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_ = 0
            for k in range(len(m_b)):
                sum_ += m_a[i][k] * m_b[k][j]
            new_row.append(sum_)
        new_matrix.append(new_row)

    return new_matrix
