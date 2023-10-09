#!/usr/bin/pyhton3
"""function that append a string at the end of a file"""


def write_file(filename="", text=""):
    """appends a string in a file"""
    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(text)
