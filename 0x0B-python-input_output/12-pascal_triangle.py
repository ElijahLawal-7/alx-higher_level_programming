#!/usr/bin/python3
'''
file: 14-pascal_triangle.py
functions:
-> pascal_triangle
'''


def pascal_triangle(n):
    ''' Create a list of list representing pascal triangle '''

    triangle = []
    if n == 0:
        return triangle

    triangle.append([1])

    for i in range(1, n):
        before = triangle[-1]
        after = [1]
        for i in range(len(before) - 1):
            after.append(before[i] + before[i + 1])
        after += [1]
        triangle.append(after)

    return triangle
