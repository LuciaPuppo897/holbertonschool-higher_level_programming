#!/usr/bin/python3
"""unction that returns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """returns json rep of a string"""
    return json.loads(my_str)
