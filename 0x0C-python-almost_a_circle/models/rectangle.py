#!/usr/bin/python3
"""A module containing a Rectangle class"""


from .base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """override the print function"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height)

    def to_dictionary(self):
        """creates a dictionary"""
        return {"x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width}
