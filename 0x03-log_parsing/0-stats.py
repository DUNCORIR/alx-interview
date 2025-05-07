#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.strip().split()

        # Skip lines that don't have enough parts or are in an invalid format
        if len(parts) < 7:
            continue

        # Extract the status code and file size from the line
        try:
            # The second-to-last part is the status code
            status_code = int(parts[-2])
            file_size = int(parts[-1])    # The last part is the file size

            # Check if the status code is valid
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size

        except ValueError:
            # Skip lines where file_size or status_code is not an integer
            continue

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle graceful exit when interrupted
    print_stats()
    sys.exit(0)
