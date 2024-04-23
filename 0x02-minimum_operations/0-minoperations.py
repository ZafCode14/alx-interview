#!/usr/bin/python3
"""Module with a python script"""


def minOperations(n):
    """Function that calculates the number of operations needed"""
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1
    return nOpe
