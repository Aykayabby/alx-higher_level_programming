#!/usr/bin/python3
"""A module which contains BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """Afunction that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that raises a TypeError and ValueError"""
        if type(value) != int:
            raise TypeError{"{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A rectangle class"""
    def __init__(self, width, height):
        "init method containing width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
