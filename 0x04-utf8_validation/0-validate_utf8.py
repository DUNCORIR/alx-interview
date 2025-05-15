#!/usr/bin/python3
"""
The script implements UTF-8 Validation.
"""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, else False"""
    n_bytes = 0

    for byte in data:
        # Only keep the last 8 bits
        byte = byte & 0xFF

        if n_bytes == 0:
            # Count leading 1s to determine character length
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                # Starts with 1 but doesn't match any valid leading byte
                return False
        else:
            # Must be a continuation byte (starts with '10')
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
