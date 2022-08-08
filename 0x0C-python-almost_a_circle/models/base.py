#!/usr/bin/python3
"""This module contains a base class"""


class Base:
    """Base class with private attribute and class constructor"""
    __nb_objects = 0

    def __init__(self, id = None):
        """init method"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
