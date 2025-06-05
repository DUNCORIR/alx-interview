#!/usr/bin/python3
""" This script implements the rotation of a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n * n matrix 90 degrees clockwise in place.


    Args:
    matrix (list of list of int): The matrix to rotate.
    """
    n = len(matrix)

    # step 1: Transposeing the matrix , swaping rows with columns.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
