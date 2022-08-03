#!/usr/bin/python3
"""A module containing MyList class"""


class MyList(list):
    """my_list class calling a list superclass"""
    def print_sorted(self):
        """prints MyList class in a sorted manner"""
        print(sorted(self))
