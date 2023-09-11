#!/usr/bin/python3
"""MyList inherits from list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
