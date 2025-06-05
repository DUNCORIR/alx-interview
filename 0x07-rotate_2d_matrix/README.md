# 0x07. Rotate 2D Matrix

## 📌 Project Overview

This project focuses on implementing an **in-place algorithm** that rotates a square `n x n` 2D matrix **90 degrees clockwise** using only Python. The goal is to deepen understanding of **matrix manipulation**, **in-place operations**, and **nested looping** — key concepts in both interview questions and real-world algorithm design.

---

## ✅ Learning Objectives

- Understand how 2D matrices are represented and manipulated in Python.
- Perform in-place operations to optimize space complexity.
- Use matrix transposition and row-reversal to achieve matrix rotation.
- Practice writing clean, efficient, and well-documented Python code.

---

## 🧠 Key Concepts

- **Matrix Representation**: Python represents a 2D matrix as a list of lists.
- **In-place Algorithm**: Operations are performed directly on the input matrix without allocating extra memory.
- **Transpose**: Swap `matrix[i][j]` with `matrix[j][i]` for all `i < j`.
- **Reverse Rows**: After transposing, reverse each row to complete the 90° rotation.

---

## 🛠️ Function Prototype

```python
def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
    """
🧪 Example
Input:
python

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate_2d_matrix(matrix)
Output:
python

[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
🔄 Steps to Rotate Matrix
Transpose the matrix:

Convert rows into columns.

Reverse each row:

This simulates the 90° rotation.

💡 Constraints
Do not use additional data structures (no extra matrix allowed).

Must operate in-place.

Do not import any external modules.

Code must follow pycodestyle (version 2.8.0).

📂 File Structure
bash

.
├── 0-rotate_2d_matrix.py   # Main function file
├── README.md               # Project documentation
🔧 Environment
Language: Python 3.8.10

OS: Ubuntu 20.04 LTS

Editor: vi, vim, or emacs

Linter: pycodestyle 2.8.0

📚 References
GeeksForGeeks: In-place matrix rotation

Python Lists Documentation

Transpose a Matrix in Pytho