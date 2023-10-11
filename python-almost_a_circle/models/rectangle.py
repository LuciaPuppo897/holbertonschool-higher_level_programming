#!/usr/bin/python3
"""
class that inherit from base and define a rectangle
with width,heigth,y and x
"""
from models.base import Base


class Rectangle(Base):
    """new class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Call the super class constructor with id and initializate them"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    def area(self):
        """Public method that return the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the Rectangle"""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Override the __str__ method to return the specified format."""
        return (
        f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
        f"{self.__width}/{self.__height}"
    )
