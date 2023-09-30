#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """Private attribute def size"""
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area"""
        return self.__size ** 2
