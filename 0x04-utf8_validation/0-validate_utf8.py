#!/usr/bin/python3
"""Module with a python script"""


def validUTF8(data):
    expected_bytes = 0

    for byte in data:

        if expected_bytes == 0:
            if byte & 0b10000000 == 0:
                expected_bytes = 0
            elif byte & 0b11100000 == 0b11000000:
                expected_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                expected_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                expected_bytes = 3
            else:
                return False

        else:
            if byte & 0b11000000 != 0b10000000:
                return False

            expected_bytes -= 1

            if expected_bytes == 0:
                expected_bytes = 0

    return expected_bytes == 0
