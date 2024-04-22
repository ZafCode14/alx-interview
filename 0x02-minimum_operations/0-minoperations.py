#!/usr/bin/python3
"""Module with a python script"""


def minOperations(n):
    """Function that calculates the number of operations needed"""
    if n <= 1:
        return 0

    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n] if min_ops[n] != float('inf') else 0
