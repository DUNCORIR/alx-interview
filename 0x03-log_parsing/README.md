# 0x03. Log Parsing

## Description

This project is part of the Holberton School Higher Level Programming curriculum. It focuses on building a Python script that processes incoming log data in real-time from standard input (`stdin`). The program parses the input line by line to extract HTTP status codes and file sizes, computes metrics, and prints summaries periodically and upon interruption.

---

## Requirements

- Ubuntu 20.04 LTS
- Python 3.4.3
- Code must follow [PEP 8](https://pep8.org/) style guidelines (version 1.7.x)
- All files are executable and end with a new line
- Script starts with `#!/usr/bin/python3`
- Use only the allowed editors: `vi`, `vim`, `emacs`

---

## Usage

```bash
cat access.log | ./0-stats.py

Input must be fed from a log file or piped in manually, and must follow this format per line:

php-template

<IP Address> - [<date>] "GET /path HTTP/1.1" <status code> <file size>
Example:

yaml

127.0.0.1 - [2023-05-05 12:00:00.000000] "GET /index.html HTTP/1.1" 200 1024
Functionality
Parses each line and extracts the status code and file size

Accumulates total file size and counts of each status 

Prints statistics every 10 lines and on keyboard interruption (CTRL+C)

Output format:

File size: <total size>
<status code>: <count>
...
Example:

yaml

File size: 23456
200: 5
404: 2
500: 1

## 📘 Concepts Needed

To successfully complete this project, you need to understand and apply several core Python concepts:

---

### 1. File I/O (Input and Output)

- Use of `sys.stdin` to read input line by line, simulating a real-time data stream.
- Efficient reading without loading all data into memory at once.

📚 **Key functions:** `sys.stdin`, `for line in sys.stdin`

---

### 2. Signal Handling

- Gracefully handling interruptions like `CTRL + C` (KeyboardInterrupt).
- Ensuring that metrics (like total file size and status code counts) are printed even if the script is interrupted.

📚 **Key modules:** `signal`, `sys.exit()`

---

### 3. Data Processing and String Manipulation

- Splitting lines into components and extracting relevant data (e.g., status code, file size).
- Validating line structure before processing.
- Accumulating and updating totals dynamically.

📚 **Key functions:** `.split()`, `.strip()`, list indexing

---

### 4. Regular Expressions (Optional but Useful)

- For validating the format of each log line.
- Ensuring that only correctly structured lines are parsed.

📚 **Key module:** `re`  
💡 Example pattern: `r'^\S+ - \[\S+ \S+\] "GET \S+ HTTP/1.1" \d{3} \d+$'`

---

### 5. Dictionaries in Python

- Storing and updating counts of HTTP status codes efficiently.
- Accessing and modifying dictionary values safely using `.get()`.

📚 **Key methods:** `.get()`, `in`, dictionary iteration

---

### 6. Exception Handling

- Preventing the script from crashing on unexpected or malformed input.
- Handling `ValueError`, `IndexError`, and other possible exceptions.

📚 **Key blocks:** `try-except`, `except Exception as e`

---

By mastering these topics, you'll be equipped to parse log entries in real-time, track metrics reliably, and write robust, production-grade Python scripts.


Author
Duncan Korir