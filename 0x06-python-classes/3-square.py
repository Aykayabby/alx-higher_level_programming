#!/usr/bin/python3
"""Amodule that creates a python class"""


class Square:
    """A class with a private attribute

    Attribute:
        size(int): size"""

    def __init__(self, size=0):
        """init method

        argument:
        size(int): size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns area of square"""

        return self.__size ** 2
