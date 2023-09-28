#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy2 = {}
    for key, value in a_dictionary.items():
        copy2[key] = value * 2
    return copy2
