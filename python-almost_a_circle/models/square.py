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

    def __str__(self):
        """Override the _str_ method to return the specified format Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
