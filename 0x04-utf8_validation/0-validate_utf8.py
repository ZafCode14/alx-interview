#!/usr/bin/python3
"""Module with a python script"""


def validUTF8(data):
    # Count of remaining bytes for the current character
    remaining_bytes = 0

    for byte in data:
        # Check if this byte is the start of a new character
        if remaining_bytes == 0:
            if byte >> 3 == 0b11110:  # 4-byte character
                remaining_bytes = 3
            elif byte >> 4 == 0b1110:  # 3-byte character
                remaining_bytes = 2
            elif byte >> 5 == 0b110:  # 2-byte character
                remaining_bytes = 1
            elif byte >> 7 == 0:  # 1-byte character
                remaining_bytes = 0
            else:
                return False  # Invalid starting byte

        else:
            # Check if this byte is a continuation byte
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            remaining_bytes -= 1

        # If there are negative remaining bytes,
        # it means there are too many continuation bytes
        if remaining_bytes < 0:
            return False

    # If there are remaining bytes after iterating through all data,
    # it means the data is incomplete
    return remaining_bytes == 0
