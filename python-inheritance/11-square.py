#!/usr/bin/python3
"""Class that def a square with width and height as size and print a str"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that def a square"""
    def __init__(self, size):
        """initializate them"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area"""
        return self.__size ** 2

    def __str__(self) -> str:
        """returns an informal string"""
        return f"[Square] {self.__size}/{self.__size}"
