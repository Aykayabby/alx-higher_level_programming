#!/usr/bin/python3
"""A module that contains a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """An init method that calls the super class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Overrides the print function"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""
        self.validator(value, "width")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """creates a dictionary"""
        retur {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
