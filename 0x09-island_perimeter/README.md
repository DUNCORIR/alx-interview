# 0x09. Island Perimeter

## Description

This project involves calculating the perimeter of an island represented in a 2D grid (matrix). The grid contains only **0s** (water) and **1s** (land), and the objective is to return the **perimeter** of the island by analyzing each land cell's contribution and interaction with adjacent cells.

### Key Constraints:
- Each cell is square with a side length of 1.
- Land cells (1) are connected **only horizontally or vertically**, not diagonally.
- The grid is completely surrounded by water.
- There is **only one island** or no land at all.
- The island does **not contain lakes** (i.e., no water cells enclosed by land).

---

## Files

| File Name              | Description                                   |
|------------------------|-----------------------------------------------|
| `0-island_perimeter.py` | Python script containing the main function to compute island perimeter. |
| `README.md`            | Project overview and documentation.           |

---

## Function Prototype

```python
def island_perimeter(grid):
    """
    Calculates the perimeter of an island described in a 2D grid.
    Args:
        grid (list of list of int): 2D grid where 1 represents land and 0 represents water.
    Returns:
        int: The perimeter of the island.
    """

Usage
To test the function manually, you can run the following:

bash

$ cat main.py
python

#!/usr/bin/python3
from 0-island_perimeter import island_perimeter

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print("Island Perimeter:", island_perimeter(grid))
Expected output:

bash

Island Perimeter: 16
How It Works
Each land cell contributes 4 edges to the perimeter. However, if it shares a side with another land cell (above or to the left), the shared edge does not count twice:

For every land cell:

Add 4 to the perimeter.

Subtract 2 for each adjacent land cell above.

Subtract 2 for each adjacent land cell to the left.

This avoids double-counting shared sides and results in an efficient calculation.

Example
For this input grid:

python

[
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
The perimeter is 16.

Requirements
Allowed editors: vi, vim, emacs

OS: Ubuntu 20.04 LTS

Python 3.4.3

No imports allowed

Must follow PEP 8 (version 1.7)

Each Python file must be executable

Must end with a new line

Include documentation for all functions

Author
Duncan Korir

Acknowledgements
Project part of the ALX Software Engineering Program.
Task inspired by algorithmic challenges involving 2D grid traversal, adjacency checks, and logical perimeter computation.