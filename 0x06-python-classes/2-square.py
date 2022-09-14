#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Instantiation with optional size
        size must be an integer
"""


class Square:
    """Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
