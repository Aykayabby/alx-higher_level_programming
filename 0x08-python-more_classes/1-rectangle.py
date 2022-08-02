#!/usr/bin/python3
"A module that defines a rectangle"


class Rectangle:
   """A rectangle class"""

    def __init__(self, width=0, height=0):
        """init method

        args:
            width: The width in int
            height: The height in int"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width of the property

        raises error when width is not and integer or is less than 0"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of the property

        raises error when the height is not an integer or is less than 0"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
