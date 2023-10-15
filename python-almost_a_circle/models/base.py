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

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        file_name = f"{cls.__name__}.json"
        with open(file_name, 'w') as file:
            json_string = (cls.to_json_string([obj.to_dictionary()
        for obj in list_objs]))
            file.write(json_string)
