#!/usr/bin/python3

"""
This module implements Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]] # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1] # Start with 1
        for j in range(1, i):
            # Sum of two numbers above
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1) # End with 1
        triangle.append(row)

    return triangle
