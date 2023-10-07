#!/usr/bin/python3
"""Function that returns a lits of obj and method of a class"""


def lookup(obj):
    """return a list of the dir """
    if obj is not None:
        return (dir(obj))
    else:
        return []
