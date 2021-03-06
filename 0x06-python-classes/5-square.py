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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square"""

        return self.__size ** 2

    def my_print(self):
        """Prints a pattern"""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
