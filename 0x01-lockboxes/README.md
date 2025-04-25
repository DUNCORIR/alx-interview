# 0x01. Lockboxes

## 🧠 Project Description

This project is part of the **Algorithm curriculum** at ALX/Holberton School. It focuses on **graph traversal**, **depth-first search (DFS)**, and **set operations** using Python. The task is to determine whether all the boxes in a given list can be opened using the keys contained within them.

## 📋 Problem Statement

You have `n` number of locked boxes in front of you, each numbered from `0` to `n - 1`. Each box may contain keys to other boxes.

### Requirements:
- Box `0` is always unlocked.
- A key with the same number as a box opens that specific box.
- Keys may be duplicated or invalid (e.g., refer to non-existent boxes).
- Your goal is to determine if **all** boxes can be opened starting from box `0`.

## 🛠️ Function Prototype

```python
def canUnlockAll(boxes):
    """Determines whether all boxes can be opened."""

Arguments:
boxes: A list of lists. Each inner list contains integers representing keys in that box.

Returns:
True if all boxes can be opened.

False otherwise.

✅ Example Usage

>>> canUnlockAll([[1], [2], [3], [4], []])
True

>>> canUnlockAll([[1, 3], [3, 0, 1], [2], [0]])
True

>>> canUnlockAll([[1, 2], [3], [3], [], [0]])
False

🧪 How to Run
Make sure your script file is executable and has the correct shebang:

bash

chmod +x 0-lockboxes.py
Then run it with Python 3:

bash

./0-lockboxes.py
🧪 Testing
You can include your test cases in a separate Python file (e.g. main.py) or use the Python interpreter directly:

bash

python3 main.py
🧩 Concepts Covered
List and list manipulation

Graph traversal (DFS)

Recursion / Stack-based approaches

Set operations for tracking visited nodes

Algorithmic efficiency (O(n) time)

🧑‍💻 Author
Duncan Korir

GitHub: @duncorir

LinkedIn: linkedin.com/in/duncankorir