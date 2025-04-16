📐 Pascal's Triangle - Python Implementation
🧠 Project Overview
This project is a Python implementation of Pascal’s Triangle, a mathematical structure in which each number is the sum of the two numbers directly above it. The project includes a single function pascal_triangle(n) that returns the triangle as a list of lists.

📊 What is Pascal’s Triangle?
Pascal’s Triangle is a triangular array of numbers where:

The first and last values of each row are always 1.

Every other number is the sum of the two numbers directly above it.

Example for n = 5:

csharp

    [1]
   [1, 1]
  [1, 2, 1]
 [1, 3, 3, 1]
[1, 4, 6, 4, 1]
🧩 Learning Objectives
By completing this project, you will:

Deepen your understanding of list manipulation in Python.

Practice writing clean and efficient functions.

Apply nested loops and arithmetic logic.

Build confidence in basic algorithm design.

🛠️ Technologies Used
Python 3

Standard Python modules only (no external libraries)

🔁 Function Description
def pascal_triangle(n):
Parameters:

n (int): The number of rows to generate in Pascal’s Triangle.

Returns:

A list of lists of integers representing the Pascal’s Triangle up to n rows.

Returns an empty list if n <= 0.

✅ Requirements
Must be implemented in a file named 0-pascal_triangle.py

Should be tested with different input values

Only standard Python features are allowed

📦 Usage Example
python

from 0-pascal_triangle import pascal_triangle

rows = 5
triangle = pascal_triangle(rows)
for row in triangle:
    print(row)
Output:

Copy code
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
🔎 Edge Case Handling
If n <= 0, the function returns an empty list:

python

print(pascal_triangle(0))  # Output: []
🧪 Testing Suggestions
Try the function with:

n = 1

n = 0

n = 10

Negative numbers

Very large values (performance test)

👨‍💻 Author
Duncan Korir

GitHub

LinkedIn

Portfolio
