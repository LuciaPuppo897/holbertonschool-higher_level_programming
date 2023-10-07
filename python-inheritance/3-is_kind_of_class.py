#!/usr/bin/python3
"""a function that returns true is the objects is an exact istance of an obj"""


def is_kind_of_class(obj, a_class):
    """return true if exact instance or inherantce from other"""
    return isinstance(obj, a_class)
