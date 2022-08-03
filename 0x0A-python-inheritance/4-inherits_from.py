#!/usr/bin/python3
"""A module that checks if object is an instance of a class"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a_class"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
