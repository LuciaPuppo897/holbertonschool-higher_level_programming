#!/usr/bin/python3
"""Class that def a rectangle with width and height"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that def a rectangle"""
    def __init__(self, width, height):
        """inicitialize the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """returns an informal string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
