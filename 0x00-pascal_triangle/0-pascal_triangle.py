#!/usr/bin/env python3
"""This module contains a python script"""
from typing import List


def pascal_triangle(n):
    """This function creates the pascal trinagle"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(triangle[-1])-1):
            a = triangle[-1][j]
            b = triangle[-1][j+1]
            temp.insert(-1, a + b)
        triangle.append(temp)

    return triangle
