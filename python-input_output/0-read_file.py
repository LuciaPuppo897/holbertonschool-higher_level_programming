#!/usr/bin/pyhton3


def read_file(filename=""):
    """reads a file"""
    with open(filename, 'r', encoding='utf-8') as myfile:
        print(myfile.read(), end='')

