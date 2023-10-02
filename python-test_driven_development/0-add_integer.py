#!/usr/bin/python3
""" deffine a class to add  two ints"""


def add_integer(a, b=98): 
    """ 
    add two values that must be int o float in
    case that not raise an TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer") 
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)
    return (a + b)