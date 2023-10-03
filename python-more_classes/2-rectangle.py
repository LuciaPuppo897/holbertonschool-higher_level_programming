#!/usr/bin/python3
"""
    A class that define a rectangle correctly
    with height and width, and def the area
    and perimeter
"""


class Rectangle:
    """a class that def a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """def priv atributte width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """def priv atributte height"""
        return self.__height

    @height.setter
    def height(self, value):
        """" set height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
