#!/usr/bin/python3
"""A module that checks if the arguments are of the same instance"""


def is_kind_of_class(obj, a_class):
    """checks if obj is of the same instance as a_class"""
    return isinstance(obj, a_class)
