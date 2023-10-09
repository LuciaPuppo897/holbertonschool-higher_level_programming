#!/usr/bin/python3
"""function that writr a file"""


def write_file(filename="", text=""):
    """write an encoded file"""
    with open(filename, "w",) as myfile:
        return myfile.write(text)
