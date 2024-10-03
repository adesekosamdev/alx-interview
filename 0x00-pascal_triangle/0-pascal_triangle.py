#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    t = []
    if n <= 0:
        return t
    t = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(t[i - 1]) - 1):
            curr = t[i - 1]
            temp.append(t[i - 1][j] + t[i - 1][j + 1])
        temp.append(1)
        t.append(temp)
    return t
