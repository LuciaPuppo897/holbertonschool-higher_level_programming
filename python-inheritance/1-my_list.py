#!/usr/bin/python3

"""class that inheritance from lookup"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        """public method that sorts a list"""
        sorted_list = sorted(self)
        print(sorted_list)
