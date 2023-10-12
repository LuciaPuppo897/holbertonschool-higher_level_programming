#!/usr/bin/python3
"""
class that inherits from rectangle
def a squeare with same attributes and values
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that inhirits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """def prop size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size values"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the _str_ method to return the specified format Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assign arguments to attributes in a specific order"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
