#!/usr/bin/python3
"""base class for the project almost a circle"""
import json


class Base:
    """Private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initilizates the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a list of dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
