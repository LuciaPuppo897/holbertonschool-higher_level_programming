#!/usr/bin/python3
def class_to_json(obj):
    """Check if obj is an instance of a class"""
    if not hasattr(obj, '__dict__'):
        raise ValueError("obj must be an instance of a class")

    obj_dict = vars(obj)

    json_dict = {}
    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
