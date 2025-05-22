ddfff# 0x05. N Queens

## 📚 Project Description

The **N Queens** problem is a classic example of algorithmic problem-solving using **backtracking**. The objective is to place `N` chess queens on an `N×N` chessboard so that no two queens threaten each other. This means that no two queens share the same row, column, or diagonal.

This project is part of the **ALX Software Engineering Program** and focuses on implementing an efficient Python solution to the N Queens puzzle.

---

## 🎯 Learning Objectives

- Understand and implement a **backtracking algorithm**.
- Use **recursion** to explore all valid configurations.
- Apply **list manipulation techniques** to store board states.
- Handle **command-line arguments** in Python using `sys`.
- Follow **PEP 8** coding standards.
- Improve algorithmic thinking and debugging skills.

---

## 🛠️ Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files will be compiled/interpreted on Ubuntu 20.04 LTS using Python 3.4.3
- First line of every file: `#!/usr/bin/python3`
- Code must follow the PEP 8 style guide (version 1.7.*)
- All files must be executable
- Must handle invalid arguments (e.g., missing input, non-integer, N < 4)
- Output must be printed as a list of lists representing queen positions:

[[row1, col1], [row2, col2], ..., [rowN, colN]]

yaml


---

## 📄 File

- `0-nqueens.py`: The main script that solves the N Queens problem using backtracking.

---

## 🚀 Usage

1. Make the script executable:
 ```bash
 chmod +x 0-nqueens.py
Run the script with N as a command-line argument (N must be ≥ 4):

bash

./0-nqueens.py 4
Sample output:

lua

[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

⚙️ Algorithm Overview
The algorithm uses a backtracking approach:

Place one queen in each row.

For each row, try placing a queen in each column.

If the position is safe (no threats from existing queens), move to the next row.

If a conflict is found, backtrack and try the next possible column.

Repeat until all solutions are found.

📌 Example
For N = 4, the script prints 2 possible configurations:

lua

[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
Each configuration lists the position of a queen in every row.

🧑 Author
Duncan Korir

GitHub: Duncorir