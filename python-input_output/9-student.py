#!/usr/bin/python3
""" a class student that defines a student"""

class Student():
    """def a new class"""

    def __init__(self, first_name, last_name, age):
        """initializate the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictonary rep of the student class"""
        return  self.__dict__