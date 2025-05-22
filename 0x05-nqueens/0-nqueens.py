#!/usr/bin/python3
"""
The script Solves the N Queens problem using backtracking.
"""

import sys


def validate_input():
    """
    Validate and parse the command-line argument.

    - Ensures exactly one argument is passed.
    - Checks if the argument is an integer.
    - Ensures the integer is >= 4.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(queens, row, col):
    """
    Determine if a queen can be placed at (row, col)
    without being attacked by other queens.

    - No two queens can be in the same column.
    - No two queens can be on the same diagonal.
    """
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """
    Recursive backtracking function to solve the N Queens problem.

    - Places a queen in each row.
    - Checks if placement is valid using `is_safe`.
    - Backtracks by removing the queen if no valid solution found.
    - When `row == n`, a valid solution is found and added to `solutions`.
    """
    if row == n:
        solutions.append(queens[:])  # Deep copy of current solution
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])          # Place queen
            solve_nqueens(n, row + 1, queens, solutions)  # Recurse to next row
            queens.pop()                        # Backtrack


def print_solutions(solutions):
    """
    Print all the valid N Queens solutions.

    Each solution is printed as a list of [row, col] positions.
    One solution per line.
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    n = validate_input()
    solutions = []
    solve_nqueens(n, 0, [], solutions)
    print_solutions(solutions)
