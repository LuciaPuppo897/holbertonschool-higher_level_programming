#!/usr/bin/python3
class Square:
    """A class that defines a Square"""
    def __init__(self, size=0):
        self.size = size  # Use the setter to validate and set size

    @property
    def size(self):
        """attribute def a size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area"""
        return self.__size ** 2
