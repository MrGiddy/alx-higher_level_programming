#!/usr/bin/python3
"""
Contains definition for function lazy_matrix_mul that multiplies two matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists of ints/floats): Matrix a
        m_b (list of lists of ints/floats): Matrix b
    """

    return (np.matmul(m_a, m_b))
