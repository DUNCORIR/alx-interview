# 0x02. Minimum Operations

## Description

This project focuses on a classic algorithmic problem involving two operations — **Copy All** and **Paste** — to achieve exactly `n` characters starting from a single character `'H'`. The goal is to calculate the **minimum number of operations** required to get `n` `'H'` characters on a text file using only those operations.

The challenge involves understanding and applying:
- **Prime Factorization**
- **Dynamic Programming**
- **Greedy Algorithms**
- **Code Optimization**

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All Python files must be executable and follow PEP 8 (version 1.7.x).
- The first line of each Python file should be `#!/usr/bin/python3`.

## Files

| Filename         | Description                                        |
|------------------|----------------------------------------------------|
| `0-minoperations.py` | Function that computes the minimum number of operations to reach `n` characters. |

## Function Prototype

```python
def minOperations(n):
    """Returns the minimum number of operations to reach exactly n H characters."""

Example:
python

minOperations(9)
# Output: 6

Explanation:

The prime factors of 9 are 3 and 3 → 3 + 3 = 6 operations.

Author
Duncan Korir - GitHub | LinkedIn | Portfolio