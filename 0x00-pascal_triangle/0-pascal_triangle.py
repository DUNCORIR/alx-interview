#!/usr/bin/python3
"""
This module implements Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of n.
    Raises TypeError if n is not an integer.
    """
    try:
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n <= 0:
            return []

        triangle = [[1]]

        for i in range(1, n):
            prev_row = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
            triangle.append(row)

        return triangle

    except TypeError as te:
        print(f"TypeError: {te}")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
