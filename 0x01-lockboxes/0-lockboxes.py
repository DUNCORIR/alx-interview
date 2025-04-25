#!/usr/bin/python3
"""
This module defines the canUnlockAll function to check
if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines whether all boxes can be opened starting from box 0.

    Args:
        boxes (list of list of int): Each box is a list
        containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Check if boxes is a valid list
    if not boxes or not isinstance(boxes, list):
        return False

    # Total number of boxes
    n = len(boxes)

    # Set to track visited/opened boxes (start with box 0)
    visited = set([0])

    # Stack for boxes to process (DFS strategy)
    stack = [0]

    # Loop until there are no more boxes left to explore
    while stack:
        current = stack.pop()  # Get the last added box (LIFO - DFS)

        # Loop through all keys found in the current box
        for key in boxes[current]:

            # Only consider the key if:
            # 1. It's a valid box index (0 <= key < n)
            # 2. The box hasn't been visited yet
            if 0 <= key < n and key not in visited:
                visited.add(key)     # Mark box as visited (opened)
                stack.append(key)    # Add box to stack for further exploration

    # After exploring, if we visited all boxes, return True
    return len(visited) == n
