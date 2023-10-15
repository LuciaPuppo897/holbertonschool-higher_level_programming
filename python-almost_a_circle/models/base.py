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

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from the JSON string repr"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from a dictionary"""
        if cls.__name__ == "Rectangle":
            shape = cls(1, 1)
        elif cls.__name__ == "Square":
            shape = cls(1)
        else:
            shape = None

        shape.update(**dictionary)
        return shape
    
    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file"""
        file_name = f"{cls.__name__}.json" 

        try:
            with open(file_name, 'r') as file:
                json_string = file.read()
                dict_list = Base.from_json_string(json_string)
                instance_list = [cls.create(**d) for d in dict_list]
                return instance_list
        except FileNotFoundError:
            return []