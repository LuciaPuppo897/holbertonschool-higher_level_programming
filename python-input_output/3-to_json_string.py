#!/usr/bin/python3
"""a function that returns the JSON rep of an object (string)"""


import json


def to_json_string(my_obj):
    """returns json rep of a string"""
    return json.dumps(my_obj)
