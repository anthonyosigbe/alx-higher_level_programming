#!/usr/bin/python3
"""Establishes a matrix multiplication function utilizing NumPy."""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy and returns the resulting matrix.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        ndarray: The result of multiplying m_a and m_b as a NumPy array.

    Raises:
        ValueError: If m_a or m_b is empty or if they cannot be multiplied,
        due to incorrect dimensions.
    """
    return (np.matmul(m_a, m_b))
