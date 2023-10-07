#!/usr/bin/python3
"""Function that returns a lits of obj and method of a class"""


def lookup(obj):
    if obj is not None:
        print(dir(obj))
