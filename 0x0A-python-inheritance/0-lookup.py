#!/usr/bin/python3
"""lookup function

returns the attributes of an object"""


def lookup(obj):
    """finds all attributes of an object

    Returns:
    all attributes specific to the object"""
    return dir(obj)
