#!/usr/bin/python3
"""defines int class"""


class Myint(int):
    """int class"""
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
