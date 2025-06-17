#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a 2D grid.

The grid is a list of list of integers:
- 0 represents water
- 1 represents land

Each cell is a square with a side length of 1.
Cells are connected only horizontally and vertically (not diagonally).
The grid is completely surrounded by water and contains only
one island (or nothing).
There are no lakes (no water completely enclosed by land).
"""


def island_perimeter(grid):
    """
    Calculate and return the perimeter of the island in the grid.

    Args:
        grid (list of list of int): 2D list representing the map
                                    0 = water, 1 = land

    Returns:
        int: The total perimeter of the island
    """
    if not grid or not grid[0]:
        return 0  # Handle empty grid edge case

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0  # Initialize perimeter counter

    # Iterate over every cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Land cell contributes 4 sides by default
                perimeter += 4

                # Check the cell above (top neighbor)
                # If the top neighbor is also land, subtract 2 (shared edge)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check the cell to the left (left neighbor)
                # If the left neighbor is also land, subtract 2 (shared edge)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    # After processing all cells, return the total perimeter
    return perimeter
