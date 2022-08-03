#!/usr/bin/python3
"""A module containing a function that checks if object is of a class"""


def is_same_class(obj, a_class):
    """function that checks if obj is of a_class"""
    return type(obj) is a_class
