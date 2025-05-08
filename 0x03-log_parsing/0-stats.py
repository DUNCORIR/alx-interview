#!/usr/bin/python3
"""
This script reads log lines from stdin,
processes each line to extract information about
status codes and file sizes, and prints statistics periodically.

The input format is expected to be:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

- After every 10 lines and/or when interrupted by CTRL + C,
it prints the following statistics:
    1. Total file size: The sum of all file sizes encountered so far.
    2. Number of lines by status code: The count of occurrences
    for specific status codes.

- Status codes considered are: 200, 301, 400, 401, 403, 404, 405, 500.
- Any line not matching the expected format will be ignored.
"""
import sys
import signal
import re


# Valid status codes to track
VALID_STATUS_CODES = ['200', '301', '400', '401', '403', '404', '405', '500']

# Initialize counters
total_file_size = 0
status_code_counts = {}
line_counter = 0

# Precompiled regex pattern to match expected log format
log_pattern = re.compile(r'.+ "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')


def print_stats():
    """Prints the total file size and sorted status code counts"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys(), key=int):
        print("{}: {}".format(code, status_code_counts[code]))


try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if not match:
            continue  # Skip invalid lines

        status_code, file_size_str = match.groups()

        try:
            file_size = int(file_size_str)
        except ValueError:
            continue  # Skip lines with non-integer file size

        total_file_size += file_size

        if status_code in VALID_STATUS_CODES:
            status_code_counts[status_code] = (
                status_code_counts.get(status_code, 0) + 1
            )

        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

finally:
    print_stats()
