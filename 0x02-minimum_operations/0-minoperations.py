#!/usr/bin/python3
"""Minimum Operations module"""


def minOperations(n):
    """Returns the fewest number of operations to result in n H characters"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations