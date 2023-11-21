#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""

import json


def load_from_json_file(filename):
    """creates a rep from a json file"""
    with open(filename, 'r') as myfile:
        return json.load(myfile)
