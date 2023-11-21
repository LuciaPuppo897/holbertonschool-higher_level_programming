#!/usr/bin/python3
"""def a method that returns a json dict"""


def class_to_json(obj):
    """return a json rep of an object"""
    return obj.__dict__
