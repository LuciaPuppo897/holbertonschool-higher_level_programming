#!/usr/bin/python3
def class_to_json(obj):
    """Check if obj is an instance of a class"""
    return repr({key: value for (key, value) in obj.__dict__.items()
                if key in list(obj.__dict__.keys())})
