#!/usr/bin/python3
"""function that append a string at the end of a file"""


def append_write(filename="", text=""):
    """appends a string in a file"""
    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(text)
