# 0x08. Making Change

## 📚 Project Description

This project focuses on solving the classic **Coin Change Problem**, a fundamental challenge in algorithm design. The goal is to determine the **minimum number of coins** required to make up a given total amount, using a list of available coin denominations.

This problem explores both **Greedy Algorithms** and **Dynamic Programming**, evaluating the correctness, efficiency, and scalability of each approach.

---

## 🧠 Concepts Covered

- **Greedy Algorithms**: Fast but not always correct for arbitrary coin sets.
- **Dynamic Programming (DP)**: Reliable and optimal for all coin sets.
- **Time & Space Complexity**: Understanding algorithmic efficiency.
- **Problem Decomposition**: Breaking a complex problem into smaller, reusable subproblems.
- **Python Skills**: Efficient use of loops, conditionals, and list structures.

---

Task Requirements

Write a function:

```python
def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount.
    If the amount cannot be met by any combination of the coins, return -1.
    """
Input:
coins: a list of positive integers representing coin denominations

total: a positive integer representing the total amount

Output:
Minimum number of coins required to meet total, or -1 if impossible

 Example Usage
python

makeChange([1, 2, 25], 37)  # Output: 5 (25 + 10 + 1 + 1)
makeChange([2], 3)          # Output: -1
makeChange([1, 3, 4], 6)    # Output: 2 (3 + 3)

Algorithm Choice
Greedy: Fast but may give incorrect results for arbitrary coin sets.

Dynamic Programming: Chosen as the primary method due to guaranteed correctness and manageable time/space complexity:
Time = O(n × amount)
Space = O(amount)

How to Run
Ensure your file is executable:

bash

chmod +x 0-making_change.py
Then run using Python 3:

bash

./0-making_change.py
🧼 Code Style
Python 3.4.3

PEP 8 compliant (pycodestyle)

All files are executable

First line of each file: #!/usr/bin/python3

✅ Author
Project by: Duncan Korir
Part of the ALX/Holberton School curriculum