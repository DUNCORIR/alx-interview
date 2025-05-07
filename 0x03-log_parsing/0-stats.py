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

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the current statistics."""
    print_file_size()
    print_status_codes()


def print_file_size():
    """Print the total file size."""
    print(f"File size: {total_size}")


def print_status_codes():
    """Print the number of occurrences for each status code."""
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


def process_line(line):
    """Process a single line to update the total size and status code counts."""
    global total_size
    parts = line.strip().split()

    # Skip lines that don't have enough parts or are in an invalid format
    if len(parts) < 7:
        return

    try:
        status_code = int(parts[-2])  # The second-to-last part is the status code
        file_size = int(parts[-1])    # The last part is the file size

        # Check if the status code is valid
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += file_size

    except ValueError:
        return  # Skip lines where file_size or status_code is not an integer


def read_input():
    """Read input from stdin line by line."""
    global line_count
    for line in sys.stdin:
        process_line(line)
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()


def main():
    """Main function to set up signal handling and initiate log parsing."""
    signal.signal(signal.SIGINT, signal_handler)
    try:
        read_input()
    except KeyboardInterrupt:
        # Handle graceful exit when interrupted
        print_stats()
        sys.exit(0)


if __name__ == "__main__":
    main()
