#!/usr/bin/python3
"""Amodule that creates a python class"""


class Square:
    """A class with a private attribute

    Attribute:
        size(int): size"""

    def __init__(self, size):
        self.__size = size
