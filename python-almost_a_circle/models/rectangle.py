#!/usr/bin/python3
"""class that inherit from base and define a rectangle
    with width,heigth,y and x"""


from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the super class constructor with id and initializate them"""
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """def width priv prop"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """def priv height prop"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value attributes"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """def priv x prop"""
        return self.__x

    @x.setter
    def x(self, value):
        """set value attributes"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """def y priv prop"""
        return self.__y

    @y.setter
    def y(self, value):
        """set value attributes"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
