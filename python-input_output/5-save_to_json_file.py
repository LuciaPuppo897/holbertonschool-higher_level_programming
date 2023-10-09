#!/usr/bin/python3
""" function that writes an Obj to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """writes a json rep to a text file """
    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(json.dumps(my_obj))
