#!/usr/bin/pyhton3
"""function that writr a file"""


def write_file(filename="", text=""):
    """write an encoded file"""
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(text)