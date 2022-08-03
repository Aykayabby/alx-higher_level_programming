#!/usr/bin/python3
"""A module which contains BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """Afunction that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that raises a TypeError and ValueError

        Args:
            name(str): name of the value
            value(int): value associated with the name

            Raises:
                TypeError: if value is not an integer
                ValueError: if value is not greater than zero."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
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

    def area(self):
        """A function that returns the areaof rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """overwrites the normal print function"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A square class"""
    def __init__(self, size):
        """An init method for Square class"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
