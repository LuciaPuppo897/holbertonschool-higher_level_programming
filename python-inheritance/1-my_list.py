#!/usr/bin/python3

"""class that inheritance from list"""


class MyList(list):
    """Mylist class"""
    def print_sorted(self):
        """public method that sorts a list"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
