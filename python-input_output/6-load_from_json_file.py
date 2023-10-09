#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""

import json


def load_from_json_file(filename):
    """writes a json rep to a text file """
    with open(filename, 'a', encoding='utf-8') as myfile:
        return (json.loads(myfile.read()))
