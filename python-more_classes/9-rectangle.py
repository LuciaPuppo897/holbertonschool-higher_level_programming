#!/usr/bin/python3
"""
    A class that define a rectangle correctly
    with height and width, and def the area
    and perimeter and print it
"""


class Rectangle:
    """a class that def a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """returns an informal,nicely printable string rep of an instance"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.height):
                rectangle_str += str(self.print_symbol) * self.width + "\n"
            return rectangle_str[:-1]

    def __repr__(self):
        """Instance method that returns an official str rep of an instance"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """instance that del a rectangle and prints a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a method that belong to a class and return the big rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method suqare based on wight and heigth"""
        return cls(size, size)
