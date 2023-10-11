#!/usr/bin/python3
"""class that inherit from base and define a rectangle
    with width,heigth,y and x"""


from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the super class constructor with id and initializate them"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """def priv attr width"""
        return self.__width

    @property
    def height(self):
        """def priv attr heigth"""
        return self.__height

    @property
    def x(self):
        """def x"""
        return self.__x

    @property
    def y(self):
        """def y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set width value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height value validator"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set x value validator"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set y value validator"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
