#!/usr/bin/python3
"""
A function that check is a
if the object is an instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """returns true if is an instance"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
