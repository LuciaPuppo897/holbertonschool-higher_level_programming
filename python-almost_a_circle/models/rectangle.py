#!/usr/bin/python3
"""class that inherit from base and define a rectangle"""


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
        """set width value"""
        self.__width = value

    @height.setter
    def height(self, value):
        """sets heigth value"""
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x value"""
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y value"""
        self.__y = value
