#!/usr/bin/python3
"""Amodule that creates a python class"""


class Square:
    """A class with a private attribute

    Attribute:
        size(int): size"""

    def __init__(self, size=0, position=(0, 0)):
        """init method

        argument:
        size(int): size"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple)\
                or not len(value) == 2\
                or not isinstance(value[0], int)\
                or not isinstance(value[1], int)\
                or not value[0] > 0 or not value[1] > 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of square"""

        return self.__size ** 2

    def my_print(self):
        """Prints a pattern"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print("" * self.position + "#" * self.__size)
