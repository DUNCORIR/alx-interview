# 0x04. UTF-8 Validation

## Description

This project focuses on validating whether a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. Each character can be represented by 1 to 4 bytes, and this program uses bitwise operations in Python to verify the correctness of the encoding.

## Learning Objectives

- Understand how UTF-8 encoding works
- Apply bitwise operations to extract and validate byte patterns
- Implement logic to traverse and verify sequences of bytes
- Strengthen skills in boolean logic and data representation

## Requirements

- Language: Python 3
- Style: PEP 8 (version 1.7.x)
- OS: Ubuntu 20.04 LTS
- Editor: vi, vim, emacs
- All Python scripts must be executable and start with `#!/usr/bin/python3`

## Usage

The main function `validUTF8(data)` takes a list of integers (each representing a byte) and returns `True` if the data is a valid UTF-8 encoding, otherwise `False`.

### Example

```python
#!/usr/bin/python3
from validate_utf8 import validUTF8

data = [197, 130, 1]
print(validUTF8(data))  # Output: True

data = [235, 140, 4]
print(validUTF8(data))  # Output: False

File Structure
0-validate_utf8.py: Python script that defines the validUTF8 function.

README.md: Project documentation.

main.py (optional): Script to test various UTF-8 sequences.

How It Works
The algorithm iterates through the list of bytes.

It determines if the current byte is:

A 1-byte ASCII character,

A valid multi-byte character start,

Or a valid continuation byte.

It uses bitwise operations (>>, &) to inspect the leading bits of each byte.

It ensures the correct number and order of continuation bytes follow each start byte.

Bit Patterns
Byte Type	Bit Pattern
1-byte char	0xxxxxxx
2-byte start	110xxxxx
3-byte start	1110xxxx
4-byte start	11110xxx
Continuation	10xxxxxx

Author
Duncan Korir | GitHub: @duncorir