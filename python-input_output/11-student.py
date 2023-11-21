#!/usr/bin/python3
""" a class student that defines a student"""


class Student():
    """def a new class"""

    def __init__(self, first_name, last_name, age):
        """initializate the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictonary rep of the student with specifications """
        if attrs is None:
            return self.__dict__
        else:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

    
    def reload_from_json(self, json):
        """deserialized from json"""
        return self.__dict__.update(json)
                    