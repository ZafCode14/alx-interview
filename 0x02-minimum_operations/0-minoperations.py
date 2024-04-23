#!/usr/bin/python3
"""Module with a python script"""


def minOperations(n):
    """Function that calculates the number of operations needed"""
    if n <= 1:
        return n

    operations = 0
    copied_chars = 1
    buffer = 1

    while copied_chars < n:
        if n % copied_chars == 0:
            operations += 2
            buffer = copied_chars
            copied_chars += buffer
        else:
            operations += 1
            copied_chars += buffer

    return operations
